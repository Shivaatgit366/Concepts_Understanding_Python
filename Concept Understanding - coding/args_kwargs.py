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

# we can define the *args during "defining the function" or during "calling the function".
# remember:- all the arguments in *args will be saved as "a tuple".

# in the below example, *args is defined during the function definition.
# def myfucn(*argv):
#     for arguments in argv:  # looping a tuple.
#         print(arguments)
#     print(argv)
#     return argv  # argv is a tuple containing all the arguments.


# mytuple = myfucn("hello", 445, "shiva", True)
# print(mytuple[:2])
# ------------------------------------*---------------------------------------------------*--------------------

# any additional arguments will be treated first.
# Below is the example which shows additional argument with args.
# *args is defined during the definition of a function.

# def myfucn(arg1, *argv):
#     print(f"first argument is {arg1}")
#     for argument in argv:
#         print(f"next argument through *argv is {argument}")
#     print(argv)  # excluding the first argument, a tuple will be printed.
#     return argv  # *argv is a tuple.


# print(myfucn("hello", 445, "shiva", True, False, 44.3252))
# --------------------------------------------*--------------------------------*---------------------------

# Remember:- keyword argument is a dictionary.
# **kwargs is a dictionary which contains all the keyword arguments.
# below is the example to demonstrate **kwargs.
# In the below example, **kwargs is defined during the definition of a function.

# def myfucn(**kwargs):
#     for keyword, value in kwargs.items():  # ".items() function" gives key, value as a tuple. We get list of tuples.
#         print((keyword, value))
#     print(kwargs)
#     return kwargs


# dict1 = myfucn(first="hello", second=445, third="shivanand", fourth=True)
# print(dict1)
# ---------------------------------------------*--------------------------------*---------------------------

# additional arguments should be written first.
# additional arguments will be treated first.
# below example shows **kwargs with additional arguments.

# def myfucn(arg1, **kwargs):
#     for key, value in kwargs.items():
#         print((key, value))
#     print(f"first argument is {arg1}")
#     print(f"other arguments will be in a dictionary: {kwargs}")
#     return kwargs  # kwargs is a dictionary.


# print(myfucn("hello", first=45, second="hi", third=True, fourth=84.65))
# ----------------------------*--------------------------------*-------------------------------------------

# Note:- *args and **kwargs can be used during "calling the function"/"function calling".
# below example shows how args, kwargs are used during "calling the function".

# def myfucn(arg1, arg2, arg3):  # to call this function, we need to use 6 arguments.
#     print(f"argument1 is {arg1}")
#     print(f"argument2 is {arg2}")
#     print(f"argument3 is {arg3}")


# Remember:- same number of arguments as per the function should be used.
# my_tuple = ("shiva", "is", "a good boy")  # we know that "args" is a tuple.
# my_dict = {"arg1": "hello", "arg2": 585757, "arg3": True}  # we know that "kwargs" is a dictionary.

# Important step:- since we know "args" is a tuple and "kwargs" is a dictionary, we can use same concept.
# same concept is used to call the function with args and kwargs.

# myfucn(*my_tuple)
# myfucn(**my_dict)
# ----------------------------------------*--------------------------------*---------------------------------

# We can use *args and **kwargs in same line to call a function.

# def myFun(*args, **kwargs):
#     print(f"args is {args}")  # we already know that "args" is a tuple.
#     print(f"kwargs is {kwargs}")  # we already know that "kwargs" is a dictionary.


# Important point to remember:- When we call any function, it's arguments will be expanded first.
# When any function is called, all of it's arguments will be expanded first.
# myFun('shiva', 'is', 'good', first="hello", mid="hi", last="how are you??")
# ---------------------------------------*---------------------------------*--------------------------------
