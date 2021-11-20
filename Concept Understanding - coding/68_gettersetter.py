# As we know that Decorators are nothing but replicas/copy of some functions.
# Decorators are functions which take functions as arguments.
# Decorators will modify the other/original function without changing it.
# In case of OOP, these decorators modify init function's arguments indirectly without touching it.
# Remember : when we create property decorator, it becomes a property of an object.

# Property Decorators are built in function which is made of getter, setter, deleter and 1 docstring/comment.

# Setting/changing the values of object property/parameter is depending on setter method.
# Setters use encapsulation concept.
# we write setter as @function_name.setter    (here the function is property decorator)
# setter method will set the object property/attribute.

# Deleter can delete the value of the parameter. It sets the variable equal to "None".
# Setter can set and change the value, but Deleter deletes value and variable value becomes "None".
# we write deleter as @function_name.deleter    (here the function is property decorator)

# Using Property Decorators we can access instance/object attributes with the help of getter, setter, deleter.
# This will avoid accessing the data or modifying the data directly.


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):  # here, email is the property decorator which is being created.
# email itself is a property of the object.
# so, this property decorator displays the object's property with the following conditions.
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        else:
            return f"I am {self.fname}.{self.lname}@codewithharry.com"

# now, we want to make use of user input to set/access the attributes of objects.
# so, we make use of setter and deleter.
    @email.setter
    def email(self, string):   # here we are defining the setter function
        print("Setting now...")
        jj = string.split("@")[0]
        self.fname = jj.split(".")[0]
        self.lname = jj.split(".")[1]

    @email.deleter
    def email(self):          # here we are defining the deleter function
        self.fname = None
        self.lname = None

hindustani_supporter = Employee("Hindustani", "Supporter")

print(hindustani_supporter.email)  # email is the property of the object.

hindustani_supporter.fname = "US"  # object's property is changed.

print(hindustani_supporter.email)  # it gets updated in the function which we have created.

hindustani_supporter.email = "this.that@codewithharry.com"  # this user input is taken by the setter
# setter sets the values

print(hindustani_supporter.fname)  # we get the result as     this

del hindustani_supporter.email    #  this "email" variable/attribute is being deleted.
# this user input is taken by deleter. Deleter sets the variable values to none.

print(hindustani_supporter.email)  # we get the output to set the fname and lname values.

hindustani_supporter.email = "Harry.Perry@codewithharry.com"   # this is the new user input being given to "email"
print(hindustani_supporter.email)

print(Employee.email)
# this "email" is a property of the object and object location is so and so.

