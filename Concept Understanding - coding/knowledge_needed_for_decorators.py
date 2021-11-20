# Functions in Python are called "First class objects" because functions can be sent as arguments for other function.

# summary:-
# 1) function can be treated as an object.
# 2) function can be used as an argument inside another function.
# 3) function can return another function.
# ---------------------------------------------------------------------------------------------------------------

# Write a program to demonstrate that a function can be treated as an object.
# solution:-

# def upper_converter(text):
#     return text.upper()  # returns the string in uppercase.

# shout = upper_converter  # a variable is assigned for the name of the function. Thus, it becomes the object.

# if a variable is assigned for the "name of the function", then it becomes an object. It is same as that function.
# shout is the object which is created by "upper_converter" function.

# print(shout("hello"))
# print(upper_converter("hello"))
# ---------------------------------------------------------------------------------------------------------------

# write a program to demonstrate functions can be used as arguments inside other functions.
# solution:-

# def upper_converter(text):
#     return text.upper()

# def lower_converter(text):
#     return text.lower()

# def greet(abc):  # we will use arguments as functions.
#     text = abc("hello world, I am created by a function abc which is an argument")
#     print(text)

# greet("I am from the earth")  # it gives an error because string is not callable. Argument should take function only.
# greet(upper_converter)  # function is passed as an argument.
# greet(lower_converter)  # function is passed as an argument.
# --------------------------------------------------------------------------------------------------------------

# write a program to demonstrate function can return another function.
# solution:-

# def create_adder(x):
#     def another_arg(y):
#         return x + y
#     return another_arg

# new1 = create_adder
# print(new1(20)(10))  # new1(20) will be executed first, it creates a separate function by taking value of x as 20.
# then another_arg(10) will give 30 as the answer.

# new2 = create_adder(100)  # new another_arg function is created with x as 100. Here, new2 becomes another_arg.
# print(new2(10))  # it gives the answer 110.
# -------------------------------------------------------------------------------------------------------------
