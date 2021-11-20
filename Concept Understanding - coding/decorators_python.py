# write a program to demonstrate the concept of decorators.
# solution:-

# Consider a function which returns another function. Now, the main function is replaced by itself with some values.
# By replacing the function, behaviour of the function itself is changed.
# We can not get back the same function back again.


# def create_adder(x):    # create_adder is the decorator which will be replaced by itself.
#     def another_arg(y):    # another_arg is the wrapper function inside the decorator.
#         return x + y
#     return another_arg

# new2 = create_adder(100)  # new another_arg function is created with x as 100. Here, new2 becomes another_arg.
# print(new2(10))  # it gives the answer 110.

# create_adder = create_adder(100)  # this is called the decorator, means replacing the original function.
# print(create_adder(300))  # we are indirectly calling another_arg(300) by this technique.
# -------------------------------------------------------------------------------------------------------------

# write a program to demonstrate that decorators can change the behaviour.
# solution:-

# def hello_decorator(var):  # var is a function in this example. This var is passed as an argument for decorator.
#     def inner_wrapper1():
#         print("I am before the var function execution")
#         var()
#         print("I am after the var function execution")
#     return inner_wrapper1


# def func_for_var():
#     print("this is for var function which is used inside the inner wrap function")


# hello_decorator() will be replaced by another function. We can call that function directly.
# func_for_var = hello_decorator(func_for_var)


# func_for_var is assigned to inner_wrapper1 indirectly, now we can call func_for_var instead of decorator.
# func_for_var()  # it's enough to just call the decorator, it's behaviour is changed.
# -------------------------------------------------------------------------------------------------------------

# write a program to find out the execution time of a function using decorator.
# solution:-

# import time
# import math

# def time_calculate_decorator(fan):  # this is the decorator.
#     def inner_wrapper(*args, **kwargs):  # a function which takes any number of positional and keyword arguments.
#         begin = time.time()
#         fan(*args, **kwargs)  # this function will take some time to run.
#         end = time.time()
#         time_taken = end - begin
#         print(f"total time taken by the function is {time_taken} seconds")
#     return inner_wrapper


# @time_calculate_decorator  # it is same as writing      factorial = time_calculate_decorator(factorial)
# def factorial(num): # factorial function will replace the decorator.From next time, only this function will be called.
#     time.sleep(2)  # sleeps for 2 seconds.
#     print(math.factorial(num))  # gives the factorial of a number, takes two seconds to give the answer.


# directly we can call factorial function, factorial returns inner_wrapper.
# factorial(10)
# -------------------------------------------------------------------------------------------------------------

# Another program of decorators where argument function returns a value.

# def hello_decorator(var):  # var is a function, here it is an argument for the decorator.
#     def inner_wrap(*args, **kwargs):
#         print("I am before the execution")
#         stored_val = var(*args, **kwargs)  # argument var function is called and the value is stored in a variable.
#         print("I am after the execution")
#         return stored_val

    # return inner_wrap  # decorator returns the inner wrap function itself.


# @hello_decorator
# def sum_two_numbers(a, b):  # sum_two_numbers = hello_decorator(sum_two_numbers)
#     print("I m inside the function")
#     return a + b


# a = 20
# b = 40

# sum_two_numbers(a, b)  # sum_two_numbers = newly created inner_wrap function.
# print(sum_two_numbers(a, b))  # sum_two_numbers/inner wrap function returns 60.
# -------------------------------------------------------------------------------------------------------------

# Chaining decorators means decorating a function with multiple decorators. 2 decorators are used here.
# latest decorator will be replaced first, and then the other decorator will be taken care.
# solution:-

# def decor1(fan):
#     def inner_wrap():  # wrapped function can always use the outside function's argument.
#         x = fan()
#         return x * x
#     return inner_wrap


# def decor2(func):
#     def inner():
#         y = func()
#         return 2 * y
#     return inner


# @decor1  # num = decor1(num)
# @decor2  # num = decor2(num)
# def num():  # here, num replaces the second decorator first, num/newly created inner function will return 20.
#     return 10


# print(num())  # see above, num/inner function returns 20 already, now it goes inside decor1 and finally returns 400.
# ---------------------------------------------------------------------------------------------------------------
