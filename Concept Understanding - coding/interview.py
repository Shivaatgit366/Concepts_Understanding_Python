# Write a program to give the expected output from the given inputs
# INPUTS
sales_count = [
    {"channel": "amazon", "id": "123", "sale": "10", "returns": 2},
    {"channel": "target", "id": "213", "sale": "10", "returns": 2},
    {"channel": "nirma", "id": "231", "sale": "10", "returns": 2},
]

company_items = {
    "AMAZON": {"123": "soap", "456": "brush"},
    "NIRMA": {"231": "paste"},
    "TARGET": {"213": "soap"},
}

# Expected Output
# sales_by_item_name = [{"name": "soap", "sales": 16, "returns": 4}, {"name": "paste", "sales": 8, "returns": 2}]

# -------------------*----------------------------*--------------------------*-------------------------*-------------
# -------------------*----------------------------*--------------------------*-------------------------*-------------

amazon_id_item = {x: company_items["AMAZON"][x] for x in company_items["AMAZON"]}
print(amazon_id_item)
target_id_item = {x: company_items["TARGET"][x] for x in company_items["TARGET"]}
print(target_id_item)
nirma_id_item = {x: company_items["NIRMA"][x] for x in company_items["NIRMA"]}
print(nirma_id_item)


amazon_id = [item for item in amazon_id_item]
print(amazon_id)
target_id = [item for item in company_items["TARGET"]]
print(target_id)
nirma_id = [item for item in company_items["NIRMA"]]
print(nirma_id)

# solution :-

sale_amazon = list(sales_count[0].items())
sale_target = list(sales_count[1].items())
sale_nirma = list(sales_count[2].items())

id_amazon = list(company_items["AMAZON"].items())
id_nirma = list(company_items["NIRMA"].items())
id_target = list(company_items["TARGET"].items())

# for m in sales_count:
#     for n in company_items:
#         if m["channel"] == n.lower():
#             if m["id"] == amazon_id[0]:
#                a = {"name": "soap", "sales": f"n["sale"]"}



