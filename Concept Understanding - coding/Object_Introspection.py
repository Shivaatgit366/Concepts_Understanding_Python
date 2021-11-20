# In Python, whatever we create, everything becomes an object. Python is an OOP language.
# For all the objects we create, Python already has built in Classes.
# Object Introspection means to get details of the objects in run time.
# Many object introspects (methods) by which we can do object introspection.


# In the following example, we can see complete code is copied from previous lesson.
# Here, we examine the object introspection.
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
# print(skillf.email)
print(type(skillf)) # type() is one of the introspects which is used to find out the class of the object.
# so, this object belongs to the class "__main__.Employee"
print(id("this is a string"))  # this id() gives the id of the object. Every object has unique id.

# now, we will test dir() introspect, dir() gives all the attributes and methods of the object as a list.
# o = "this is a string"
# print(dir(o))

import inspect  # inspect is a module in Python, which has very good introspect called getmembers()
print(inspect.getmembers(skillf))  # we use getmembers() to get the details of the object.
