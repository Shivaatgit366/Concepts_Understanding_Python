# concept:- *args (positional arguments can be any number) and **kwargs (keyword arguments can be any number)

# --------------------------------------------------------------------------------------------------------------

# def print_names(*students):  # * means any number of arguments can be passed
#     print(students[0:2])  # *args means arguments
#
# print_names("shiva", "ananda", "vinod", "sada", "kumar")
# --------------------------------------------------------------------------------------------------------------

# def print_names_2(*students, leader):  # individual arguments should be written first, it gives error.
#     print(leader)
#     print(students)

# print_names_2("shiva", "ananda", "vinod", "sada", "kumar")
# --------------------------------------------------------------------------------------------------------------

# def print_names_3(name, price=100):  # default is 100, if nothing is given then 100.
#     print(name)
#     print(price)

# print_names_3("phone", 200)
# --------------------------------------------------------------------------------------------------------------

# def print_names_4(name, price=100, company="mi", location="delhi", **kwargs):  #
#     print(name)
#     print(price)
#     print(company)
#     print(location)
#     print(kwargs)

# print_names_4("phone", company="samsung", location="bangalore", owner= "shiva")
# ---------------------------------------------------------------------------------------------------------------

# def print_names_5(name, price=100, **kwargs):  # keyword arguments
#     print(name)
#     print(price)
#     print(kwargs)

# print_names_5("phone", "tv", rate= 500, company="samsung", location="bangalore", owner= "shiva")
# --------------------------------------------------------------------------------------------------------------

# def print_names_6(*args, **kwargs):  # combination of args and kwargs
#     print(args)
#     print(kwargs)

# print_names_6("phone", "tv", rate= 500, company="samsung", location="bangalore", owner= "shiva")
# -------------------------------------------------------------------------------------------------------------

# def do_division(**kwargs):
#     print(kwargs)    # {'dividend': 10, 'divisor': 5, 'city': 'bangalore', 'name': 'shiva'}
#     return kwargs['dividend'] / kwargs['divisor']  # 2 is the answer

# print(do_division(dividend=10, divisor=5, city="bangalore", name="shiva"))
# -------------------------------------------------------------------------------------------------------------

# def do_division_2(*, dividend, divisor, **kwargs):
#     print(kwargs)
#     return dividend/divisor

# print(do_division_2(dividend=10, divisor=5, myname='shiva', city= "mysore"))
# ------------------------------------------------------------------------------------------------------------