# notes:-

# In the decorator concept, a function takes another "function name" as a parameter.
# In this concept, only the "function name" is used as a parameter inside another function. We are not calling the function in the parameter, we are only using the name of the function as a parameter in another function.
# a function can be defined and called inside the another function.
# function name can be assigned to another variable.
# when a function name is sent inside the another function, then the functionality of the major function changes/lost.


"""
def my_major_func(shiva):
    return shiva()

def param_func():
    return "hello"

print(my_major_func(param_func))
# major function lost the functionality, function in the parameter is indirectly called.
# using the function as a variable inside the other function.
"""


"""
def new_decorator(shiva):

    def wrap_func():
        print("code here before executing the func")
        shiva()
        print("shiva() has been called")

    return wrap_func  # we didn't call the function, simply we are calling the name of the function.


def func_needs_decorator():
    print("this function is in need of a decorator")


func_needs_decorator = new_decorator(func_needs_decorator)  # it returns only the name of the function "wrap_func".
# func_needs_decorator = wrap_func

func_needs_decorator()
"""


def new_decorator(shiva):  # we didn't call the "shiva()" function in the parameter, we used only the "function name shiva".

    def wrap_func():
        print("code here before executing the func")
        shiva()
        print("shiva() has been called")

    return wrap_func  # we didn't call the function, simply we are calling the name of the function.


@new_decorator
def func_needs_decorator():
    print("this function is in need of a decorator")


func_needs_decorator()
