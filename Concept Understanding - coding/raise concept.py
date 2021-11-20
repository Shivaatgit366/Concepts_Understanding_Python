# raise is a keyword in Python

# a = input("what is your name??\n")  # user should give a text. But if the user gives the number, then what happens??
# if a.isnumeric():  # this function checks whether the given value is numeric or not.
#     raise Exception("numbers are not allowed")  # Exception keyword we use it for normal errors.
# print(f"hello {a}")

# 1000 lines of code are written, imagine like that situation. It takes 1 hour to run the codes.
# There is already an error above in the input itself.
# Program will run completely, time will be wasted, resources will be wasted, in the end we get error.
# It gives load on the server also, and lot of time will be wasted. We should raise error in the beginning itself.
# so, it is possible to control the error and program by using the keyword "raise".
# If we search for built in exceptions in Python, we get list of so many types of errors in Python.


# Now we look for zero division error in Python. Below is an example of zero division error.
# a = input("what is your name??\n")
# b = int(input("How much do you earn??\n"))  # it converts the input string to an integer.
# if b == 0:
#     raise ZeroDivisionError("B is 0 so we are stopping the program")
# this is how we raise error and control the program.


# one more example on exceptions is given below. Here we are handling 2 exceptions.
# 2 types of exceptions we are handling in the example, one is except keyword and other one we use raise concept.
# c = input("What is your name??\n")
# try:
#     print(a)
# except Exception as e:
#     if c == "shiva":  # this exception we can raise only when shiva is entered, or else except keyword will handle.
#         raise ValueError("shiva is blocked in this company, don't enter the name shiva")
#     print("Exception is handled")  # if the name is not shiva, then except keyword will handle the error.

# ---------------------*----------------------*---------------------------*--------------------------*--------------
