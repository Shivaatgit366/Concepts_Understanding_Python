# try - this word is used only when we are in doubt that the code block will give an error.
# except - this word is used when an error/exception occurs in the programme.
# using the except statement, the error is popped up on the screen and the programme will continue execution.

# else - this statement is executed only when there is no error.
# if there is error, it will be taken care by except statement.


# here is an example which involves all the three statements.
# def divide(a, b):
#     try:  # the below statement is just tried for execution.
#         print(f"{a}/{b} is {a / b}")
#     except ZeroDivisionError as error:  # if we get any error, it will be displayed on the screen.
#         print(error)
#     else:  # if there is no exception, then the following message will be typed.
#         print("No error")
# divide(4, 3)  # function is called and it will be executed.


# finally : this statement executes anything whether we got error or not.
# finally code block will be executed in any condition.


# try block will be executed when there is no error.
# except block will be executed when there is error. Try block won't be executed.
# else block will be executed when there is no error, except block won't be executed in this case.
# finally block will be executed in any condition (error is present or not, it doesn't matter).


# here is an example involving all the 4 terms.
# f1 = open("function_caching.txt")  # an existing file is tried to open with file pointer f1
# try:
#     f = open("does.txt")  # even though file "does" is not existing, we tried to open does.
# if we get the error, it will be popped up in except block.
# except Exception as error:
#     print(error)
# else:
#     print("there is no error found")  # this code will not be executed since we got an error.
# finally:
#     print("Run this anyway....")
# we can't write    f.close()  # we can not write this line because f pointer doesn't exist.
# since there is no file "does", so file pointer f does not exist.
#     f1.close()  # this f1 pointer is closed.
# print("Important stuff")

# ------------------*---------------------*---------------------*-------------------------*------------------------

