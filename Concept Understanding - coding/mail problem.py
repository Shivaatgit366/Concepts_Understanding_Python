population_counts = [
    {"state": "Karnataka", "id": "112", "birth": "123775", "death": "23455"},
    {"state": "TamilNadu", "id": "112", "birth": "223421", "death": "45598"},
    {"state": "Karnataka", "id": "115", "birth": "19754", "death": "8658"}
]


city_information = {
    "Karnataka": {"112": "Bengaluru", "115": "Mysuru", "116": "Hubli"},
    "TamilNadu": {"112": "Chennai", "115": "Madurai", "116": "Puduchery"},
}


# Find total number of deaths and births in each city
# Find total number of deaths and births in each state

# ------------------------------------------------------------------------------------------------------------------

def convert_data_city(state, id, city_information):
    for key, value in city_information.items():
        if key == state:
            for cityid, city in value.items():
                if cityid == id:
                    return city

# def convert_data_city2(state, id, city_information):
#     city_output = None
#     for key, value in city_information.items():
#         if key == state:
#             for cityid, city in value.items():
#                 if cityid == id:
#                     city_output = city
#                     break
#             if city_output != None:
#                 break
#     return city_output

def finaldict_deaths_births(population_counts, city_information):
    for_final = []
    for info_dict in population_counts:
        cityname = convert_data_city(info_dict["state"], info_dict["id"], city_information)
        for_final.append({"city": cityname, "birth": info_dict["birth"], "death": info_dict["death"]})
    return for_final


if __name__ == '__main__':
    final_list_of_dicts = finaldict_deaths_births(population_counts, city_information)
    print(final_list_of_dicts)