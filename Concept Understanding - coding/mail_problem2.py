population_counts = [
    {"state": "Karnataka", "id": "112", "birth": "123775", "death": "23455"},
    {"state": "TamilNadu", "id": "112", "birth": "223421", "death": "45598"},
    {"state": "Karnataka", "id": "115", "birth": "19754", "death": "8658"}
]

# Find total number of deaths and births in each state

# ------------------------------------------------------------------------------------------------------------------


def final_dict_births_deaths(population_counts):
    final_dict = {}
    for item in population_counts:
        state_name = item["state"]
        birth_value = int(item['birth'])
        death_value = int(item["death"])

        if state_name not in final_dict:
            final_dict[state_name] = {"birth": birth_value, "death": death_value}
        else:
            final_dict[state_name] = {"birth": birth_value + final_dict[state_name]["birth"],
                                 "death": death_value + final_dict[state_name]["death"]}
    return final_dict


if __name__ == '__main__':
    final_list_of_dicts = final_dict_births_deaths(population_counts)
    print(final_list_of_dicts)