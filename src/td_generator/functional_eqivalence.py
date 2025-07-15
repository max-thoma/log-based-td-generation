import pandas as pd
from pandas import DataFrame
from pydantic_core import from_json

from classification_definitions import ExperimentResultList
from td import (
    compare_affordance,
    AffordanceType,
    AttributeType,
)


def analyze(file_name):
    with open(file_name) as exp_file:
        exp_dict = from_json(exp_file.read())
    exp_list = ExperimentResultList(**exp_dict)

    comparison_results_lst = []
    for result in exp_list.results:
        # positive instance, i.e., the TD generation was successful
        base_td = result.base_td.to_dict()
        for topic in base_td.keys():
            for llm_td in result.llm_td_lst:
                llm_td = llm_td.to_dict()
                base_name, base_affordance = base_td.get(topic)
                llm_name, llm_affordance = llm_td.get(topic)
                comp_res = compare_affordance(base_affordance, llm_affordance)
                comparison_results_lst.append(comp_res.model_dump())
                # if not comp_res.strong_equal:
                # print(base_name, llm_name)
                # print(explain_comparison(comp_res))

        # for each negative instance (i.e, the TD generation has failed), we force a negative comparison result
        for i in range(0, result.failed):
            for topic in base_td.keys():
                base_name, base_affordance = base_td.get(topic)
                # This forces a negative comparison result
                comparison_results_lst.append(
                    compare_affordance(base_affordance, None).model_dump()
                )

    return pd.DataFrame(data=comparison_results_lst)


def table(df):
    count_dict = {}

    for attribute_t in AttributeType:
        data = {}

        for affordance_t in AffordanceType:
            data[affordance_t] = (
                (df["src_affordance_type"] == affordance_t)
                & (df["src_attribute_type"] == attribute_t)
            ).sum() // 5
        count_dict[attribute_t] = data

    count_df = pd.DataFrame(count_dict)
    print(count_df.to_csv(index=True))


def print_error_results(df, f):
    total = len(df)
    # same_affordance_type: bool = False
    # same_data_type: bool = False
    # same_enum: bool = False
    # same_properties: bool = False
    not_same_affordance_type = (
        df[df["same_affordance_type"] == False]["src_affordance_type"]
        == AffordanceType.event
    ).sum()

    same_affordance_type = (
        df[df["same_affordance_type"] == True]["src_affordance_type"]
        == AffordanceType.event
    ).sum()
    not_same_data_type = len(df[df["same_data_type"] == False])
    not_same_enum = len(df[df["same_enum"] == False])
    not_same_properties = len(df[df["same_properties"] == False])
    print(
        not_same_affordance_type, not_same_data_type, not_same_enum, not_same_properties
    )
    print(not_same_affordance_type, same_affordance_type)


def print_results(df, f):
    total = len(df)
    yes_strong = df["strong_equal"].sum()
    yes_weak = df["weak_equal"].sum()
    weak_percent = round(100 * yes_weak / total, 2)
    strong_percent = round(100 * yes_strong / total, 2)
    print(
        f"Total number of Affordances: {total} of which weak equal: {yes_weak} ({weak_percent}%), of which strong equal {yes_strong} ({strong_percent}%)"
    )
    data = {}
    data["combined"] = {"weak_equal": weak_percent, "strong_equal": strong_percent}

    for t in AffordanceType:
        total = len(df[df["src_affordance_type"] == t])
        yes_strong = df[df["src_affordance_type"] == t]["strong_equal"].sum()
        yes_weak = df[df["src_affordance_type"] == t]["weak_equal"].sum()
        weak_percent = round(100 * yes_weak / total, 2)
        strong_percent = round(100 * yes_strong / total, 2)
        print(
            f"Total number of {t.value}: {total} of which weak equal: {yes_weak} ({weak_percent}%), of which strong equal {yes_strong} ({strong_percent}%)"
        )
        data[t] = {"weak_equal": weak_percent, "strong_equal": strong_percent}

    for t in AttributeType:
        total = len(df[df["src_attribute_type"] == t])
        yes_strong = df[df["src_attribute_type"] == t]["strong_equal"].sum()
        yes_weak = df[df["src_attribute_type"] == t]["weak_equal"].sum()
        weak_percent = round(100 * yes_weak / total, 2)
        strong_percent = round(100 * yes_strong / total, 2)
        print(
            f"Total number of {t.value}: {total} of which weak equal: {yes_weak} ({weak_percent}%), of which strong equal {yes_strong} ({strong_percent}%)"
        )
        data[t] = {"weak_equal": weak_percent, "strong_equal": strong_percent}

    result_table = pd.DataFrame(data)
    print(result_table.to_csv(f"{f}_correctness.csv"))


def print_results_graphs(df, f):
    print(f"% {f}")
    print(f"% accuracy scores strong equality")
    print("\\addplot coordinates {")
    for t in AffordanceType:
        total = len(df[df["src_affordance_type"] == t])
        yes_strong = df[df["src_affordance_type"] == t]["strong_equal"].sum()
        strong_percent = round(100 * yes_strong / total, 2)
        print(f"\t({t.value}, {round(strong_percent)})")

    total = len(df)
    yes_strong = df["strong_equal"].sum()
    strong_percent = round(100 * yes_strong / total, 2)
    print(f"\t(combined, {round(strong_percent)})")
    print("};")

    print(f"% {f}")
    print(f"% accuracy scores weak equality")
    print("\\addplot coordinates {")
    for t in AttributeType:
        total = len(df[df["src_attribute_type"] == t])
        yes_weak = df[df["src_attribute_type"] == t]["weak_equal"].sum()
        weak_percent = round(100 * yes_weak / total, 2)
        print(f"\t({t.value}, {int(weak_percent)})")

    total = len(df)
    yes_weak = df["weak_equal"].sum()
    weak_percent = round(100 * yes_weak / total, 2)
    print(f"\t(combined, {int(weak_percent)})")
    print("};")


if __name__ == "__main__":
    file_names = [
        "../../data/llm_results/gemini.json",
        "../../data/llm_results/gpt4o.json",
        "../../data/llm_results/cogito.json",
    ]

    for f in file_names:
        print("==============================")
        print(f)
        df = analyze(f)
        print_results(df, f)
        # table(df)
        print_results_graphs(df, f)
        df.to_csv(f"{f[0:-5]}_functional_equivalence.csv")
        print("==============================")
