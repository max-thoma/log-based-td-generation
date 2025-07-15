import csv
import os

from numpy import dot
from openai import OpenAI
from pydantic_core import from_json

from classification_definitions import ExperimentResultList


# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def get_embedding_similarity(src, dst, model="text-embedding-3-large"):
    """
    Inspired from https://platform.openai.com/docs/guides/embeddings
    """
    src = src.replace("\n", " ")
    dst = dst.replace("\n", " ")
    src_embedding = client.embeddings.create(input=[src], model=model).data[0].embedding
    dst_embedding = client.embeddings.create(input=[dst], model=model).data[0].embedding

    return dot(src_embedding, dst_embedding)


def analyze(file_name):
    with open(file_name) as exp_file:
        exp_dict = from_json(exp_file.read())
    exp_list = ExperimentResultList(**exp_dict)

    csv_file = open(
        f"comparison_td_title_description_{file_name.split("/")[-1]}.csv", "w"
    )
    csv_file_desc = open(f"comparison_affordances_{file_name.split("/")[-1]}.csv", "w")
    comparison_writer_description = csv.writer(csv_file_desc)
    comparison_writer = csv.writer(csv_file)
    for result in exp_list.results:
        base_td_dict = result.base_td.to_dict()
        for llm_td in result.llm_td_lst:
            llm_td_dict = llm_td.to_dict()

            comparison_writer.writerow(
                [
                    result.base_td.type,
                    llm_td.type,
                    result.base_td.title,
                    llm_td.title,
                    result.base_td.description,
                    llm_td.description,
                    "x",
                    #get_embedding_similarity(
                    #    f"{result.base_td.type}, {result.base_td.title}: {result.base_td.description}",
                    #    f"{llm_td.type}, {llm_td.title}: {llm_td.description}",
                    #),
                ]
            )

            for topic, (name, affordance) in llm_td_dict.items():
                base_name, base_affordance = base_td_dict.get(topic)

                base_description = (
                    f"{base_affordance.title}: {base_affordance.description}"
                )
                llm_description = f"{affordance.title}: {affordance.description}"
                comparison_writer_description.writerow(
                    [
                        topic,
                        base_affordance.model_dump_json(indent=2),
                        affordance.model_dump_json(indent=2),
                        "x",
                        #get_embedding_similarity(base_description, llm_description),
                    ]
                )
            # We only evaluate the first set of TDs
            break
    csv_file_desc.close()
    csv_file.close()


if __name__ == "__main__":
    file_names = [
        "../../data/llm_results/gemini.json",
        "../../data/llm_results/gpt4o.json",
        "../../data/llm_results/cogito.json",
    ]

    for f in file_names:
        print("==============================")
        print(f)
        analyze(f)
        print("==============================")
