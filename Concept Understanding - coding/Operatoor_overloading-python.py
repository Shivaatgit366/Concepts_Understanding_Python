# Operator Overloading means giving extra meaning to the existing operators.
# For example operator + is used to add two integers as well as join two strings and merge two lists.

# Question : What if we want to add two objects in Python?
# Answer : In this case, we use operator overloading concept.

# concept : using the in built magic functions, behaviour of the existing operators are changed.
#           so, later these operators are used for different works.


# Dunder Method/Magic method in Python :
# Dunder means “Double Underscores”. Dunder methods are used for operator overloading.
# Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
# These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.

# Look at the below examples, two objects are created and we try to perform various operations with their arguments.
# Inorder to perform those type of operations with the objects, we should use magical methods.
# These magical methods/dunder methods help in operator overloading.
# There is no rule that dunder methods always do operator overloading, dunder methods can do different works.
# In init function, they do the work of constructors.

# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     def __add__(self, other): # this method is used to add the arguments of the objects.
#         return self.salary + other.salary  # self.salary is the property which is to be added.
# so we write self.salary (required attribute) with magic method argument (that is other.salary).
# emp1 = Employee("Harry", 345, "Programmer")
# emp2 = Employee("Rohan", 55, "Cleaner")
# print(emp1 + emp2)  # we get the result as    400


# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     def __truediv__(self, other):  # this method is used for true division.
#         return 750  # this value is given by the user.
# emp1 = Employee("Harry", 345, "Programmer")
# emp2 = Employee("Rohan", 55, "Cleaner")
# print(emp1 / emp2)  # objects are used for true division. Return value is 750.


# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     def __truediv__(self, other):  # this method is used for true division.
#         return self.salary / other.salary  # object property which is used for true division is defined.
# emp1 = Employee("Harry", 345, "Programmer")
# emp2 = Employee("Rohan", 55, "Cleaner")
# print(emp1 / emp2)  # output is 6.27272727275


# Now, we have to look for "str" and "repr" dunder methods.
# Without the repr method if we print the object, we only get location of the object. See the example below.
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     def __truediv__(self, other):
#         return 750
# emp1 = Employee("Harry", 345, "Programmer")
# print(emp1) # this prints location of the object. Result is  <__main__.Employee object at 0x00000000006F6970>


# With the use of repr dunder method, we get the required output just by printing the object.
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     def __truediv__(self, other):
#         return 750
#     def __repr__(self): # repr method helps us to get the required output when we print the object.
#         return self.printdetails() # this is returning the above function.
# above command is same as return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
# emp1 = Employee("Harry", 345, "Programmer")
# print(emp1)


# another example of repr method can be seen below.
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     def __truediv__(self, other):
#         return 750
#     def __repr__(self):
#         return f"Employee(\"{self.name}\", {self.salary}, \"{self.role}\")"
# emp1 = Employee("Harry", 345, "Programmer")
# print(emp1)


# str method is used to define/summarize the object.
# In the below example, we have both str and repr methods. Just see how they behave.
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#     def __truediv__(self, other):
#         return 750
#     def __repr__(self):
#         return f"Employee(\"{self.name}\", {self.salary}, \"{self.role}\")"
#     def __str__(self):  # when str and repr both methods are used, str method sustains.
#         return f"The name is {self.name} and my salary is {self.salary} and I am a {self.role}"
# emp1 = Employee("Harry", 345, "Programmer")
# print(emp1) # we get the output of str method.
# Note: If we call repr method by writing print(repr(emp1)), then only we get repr method output.


