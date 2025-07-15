import argparse
import logging
import os
import time
from datetime import datetime
from pathlib import Path

import dotenv
import google.generativeai as genai
import instructor
from openai import OpenAI

import generate
from classification_definitions import (
    ClassificationAffordance,
    ThingDescriptionSkeleton,
    ClassificationObject,
    ClassificationTD,
    ExperimentResult,
    ExperimentResultList,
)
from message_log import MessageLogList, DeviceMessageLog
from mock import generate_device_message_log
from td import (
    AttributeType,
    ThingDescription,
)

dotenv.load_dotenv()


logging.basicConfig(level=logging.INFO)
# logging.getLogger("instructor").setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)


def classify_object(
    affordance_message_log: MessageLogList,
    client,
    number_of_retries,
    llm_model,
    temperature,
    think,
) -> (ClassificationObject, str):
    payload_lst = affordance_message_log.to_enum()
    payloads = ""
    for p in payload_lst:
        payloads += f"{p}\n"

    prompt = f"""
Given is the following list of message payloads from an IoT device:

{payloads}
Determine the types of the attributes in the object!
"""
    if think:
        prompt += "\n/think"
    logger.debug(prompt)
    try:
        if "gemini" in llm_model:
            model = client.chat.completions.create(
                # model=llm_model,
                response_model=ClassificationObject,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_retries=number_of_retries,
                # temperature=temperature,
            )
        else:
            model = client.chat.completions.create(
                model=llm_model,
                response_model=ClassificationObject,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_retries=number_of_retries,
                temperature=temperature,
            )
    except Exception as e:
        logger.error(f"Error occurred with LLM {e}")
        return ClassificationObject(properties={})

    return model, prompt


def classify_affordance(
    context_message_log: DeviceMessageLog,
    affordance_message_log: MessageLogList,
    client,
    number_of_retries,
    llm_model,
    temperature,
    think,
) -> (ClassificationAffordance, str):
    prompt = f"""
Given is the following MQTT message log of an IoT device:\n

{context_message_log}

For this the following part of the message log:

{affordance_message_log}

Determine what kind of affordance this is!
"""
    if think:
        prompt += "\n/think"

    logger.debug(prompt)
    try:
        if "gemini" in llm_model:
            model = client.chat.completions.create(
                response_model=ClassificationAffordance,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_retries=number_of_retries,
            )
        else:
            model = client.chat.completions.create(
                model=llm_model,
                response_model=ClassificationAffordance,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_retries=number_of_retries,
                temperature=temperature,
            )
    except Exception as e:
        logger.error(f"Error occurred with LLM {e}")
        model = None
    return model, prompt


def classify_td(
    td_skeleton: ThingDescriptionSkeleton,
    client,
    number_of_retries,
    llm_model,
    temperature,
    think,
) -> (ClassificationTD, str):
    prompt = f"""
Give is the following partial Thing Description (TD)
{td_skeleton.model_dump_json(
                    exclude_none=True,
                    by_alias=True,
                    indent=4,
                    exclude={"properties": {"*": "title"}},
                )}

Determine for what kind of device this Thing Description models!
"""
    if think:
        prompt += "\n/think"

    logger.debug(prompt)
    try:
        if "gemini" in llm_model:
            model = client.chat.completions.create(
                response_model=ClassificationTD,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_retries=number_of_retries,
            )
        else:
            model = client.chat.completions.create(
                model=llm_model,
                response_model=ClassificationTD,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_retries=number_of_retries,
                temperature=temperature,
            )

    except Exception as e:
        logger.error(f"Error occurred with LLM {e}")
        model = None
    return model, prompt


def classify(
    client,
    device_message_log: DeviceMessageLog,
    number_of_retries,
    llm_model,
    temperature,
    think,
):
    prompt_lst = []
    skeleton_affordances = ThingDescriptionSkeleton()

    for affordance_log in device_message_log.logs:
        res, prompt = classify_affordance(
            device_message_log,
            affordance_log,
            client,
            number_of_retries,
            llm_model,
            temperature,
            think,
        )
        prompt_lst.append(prompt)
        # The derived form attribute is the same for any of the logs
        form = affordance_log.logs[0].to_td_form()
        enum_lst = affordance_log.to_enum()

        if res.type == AttributeType.object:
            # if the affordance is of type object, the 'subtypes' i.e. the types of the
            # object's attributes needs to be classified.
            res_obj, prompt = classify_object(
                affordance_log, client, number_of_retries, llm_model, temperature, think
            )
            prompt_lst.append(prompt)
            skeleton_affordances.add_affordance(
                res, form, enum_lst, res_obj.convert().properties
            )
        else:
            skeleton_affordances.add_affordance(res, form, enum_lst)

    skeleton_description, prompt = classify_td(
        td_skeleton=skeleton_affordances,
        client=client,
        number_of_retries=number_of_retries,
        llm_model=llm_model,
        temperature=temperature,
        think=think,
    )
    prompt_lst.append(prompt)

    # The final TD is assembled from the description and affordance skeletons
    td = ThingDescription(
        **(
            skeleton_description.model_dump(by_alias=True)
            | skeleton_affordances.model_dump(by_alias=True)
        )
    )
    return td, prompt_lst


def run_experiment(
    base_url, llm_model, temperature, iterations_per_td, number_of_retries, think
):
    start_program = time.time()

    out_path = Path("out")
    out_path.mkdir(exist_ok=True)

    if base_url is not None:
        client = instructor.from_openai(
            OpenAI(api_key="asdf", base_url=base_url),
            mode=instructor.Mode.JSON,
        )
    else:
        client = instructor.from_openai(
            OpenAI(api_key=os.environ.get("OPENAI_API_KEY")),
            # mode=instructor.Mode.TOOLS_STRICT,
            mode=instructor.Mode.JSON,
        )
        if "gemini" in llm_model:
            genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

            client = instructor.from_gemini(
                client=genai.GenerativeModel(
                    model_name=llm_model,
                ),
                mode=instructor.Mode.GEMINI_JSON,
            )

    things_list = generate.thing_list()
    # things_list = things_list[:1]
    progress_counter = 0
    number_of_steps = iterations_per_td * len(things_list)

    experiment_lst = []

    for thing in things_list:
        td = thing.td()
        device_message_logs = generate_device_message_log(thing)

        llm_td_lst = []
        success_count = 0
        fail_count = 0

        prompts = []

        for _ in range(iterations_per_td):
            try:
                llm_out, prompts = classify(
                    client=client,
                    device_message_log=device_message_logs,
                    number_of_retries=number_of_retries,
                    llm_model=llm_model,
                    temperature=temperature,
                    think=think,
                )
            except Exception as e:
                logger.error(f"Error occurred with LLM {e}")
                llm_out = None

            if llm_out is not None:
                llm_td_lst.append(llm_out)
                success_count += 1
            else:
                logger.error("A faulty model was returned")
                fail_count += 1

            progress_counter += 1
            experiment_time = time.time() - start_program
            logger.info(
                f"Elapsed time {round(experiment_time, 2)} [s], {progress_counter} of {number_of_steps}, TD have been created. Estimated remaining time: {round(((number_of_steps - progress_counter) * (experiment_time/progress_counter))/60, 0)} [min]"
            )

        assert success_count + fail_count == iterations_per_td
        experiment_lst.append(
            ExperimentResult(
                base_td=td,
                llm_td_lst=llm_td_lst,
                prompts=prompts,  # The prompts will be the same for all runs. If all runs are faulty, we do not get the prompts, which is 'fine'
                msg_log=str(device_message_logs),
                successful=success_count,
                failed=fail_count,
            )
        )

    experiment_time = time.time() - start_program
    logger.info(f"Elapsed time {experiment_time}")

    with open(
        f"out/results_{datetime.now().strftime("%Y_%m_%d_%H:%M")}_{llm_model.replace("/", "_")}.json",
        "w",
    ) as out_file:
        experiment_results_lst = ExperimentResultList(
            model=llm_model,
            iterations_per_td=iterations_per_td,
            number_of_retries=number_of_retries,
            time_elapsed=experiment_time,
            temperature=temperature,
            think_enabled=think,
            results=experiment_lst,
        )
        out_file.write(experiment_results_lst.model_dump_json(indent=2, by_alias=True))

    print(f"Experiment completed in : {experiment_results_lst.time_elapsed}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Classification experiment for TD generation."
    )
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        choices=[
            "gpt-4o",
            "deepcoder:14b",
            "deepcoder:14b-preview-q8_0",
            "cogito:70b",
            "cogito-deepthink:latest",
            "cogito:32b-v1-preview-qwen-q8_0",
            "qwq",
            "qwq:32b-q8_0",
            "gemma3:27b",
            "granite3.2-vision:2b-q8_0",
            "qwen2.5-coder:7b",
            "qwen3:30b-a3b",
            "qwen3:30b-a3b-q8_0",
            "qwen3:32b",
            "llama3.3",
            "qwen2.5-coder:14b",
            "llama3.2",
            "llama3.2-vision:11b-instruct-q8_0",
            "lennyerik/zeta",
            "deepseek-r1:32b-qwen-distill-q8_0",
            "deepseek-r1:70b",
            "deepseek-r1:32b-42k",
            "models/gemini-2.0-flash",
            "models/gemini-2.0-flash-lite",
            "models/gemini-2.5-flash-preview-04-17",
            "models/gemini-2.5-pro-preview-05-06",
        ],
        required=True,
    )
    parser.add_argument("-t", "--temperature", type=float, required=True)
    parser.add_argument("-i", "--iterations_per_td", type=int, required=True)
    parser.add_argument("-r", "--number_of_retries", type=int, required=True)
    parser.add_argument("-b", "--base_url", type=str, required=False, default=None)
    parser.add_argument("--think", required=False, type=bool, default=False)

    args = parser.parse_args()

    run_experiment(
        base_url=args.base_url,
        llm_model=args.model,
        temperature=args.temperature,
        iterations_per_td=args.iterations_per_td,
        number_of_retries=args.number_of_retries,
        think=args.think,
    )
