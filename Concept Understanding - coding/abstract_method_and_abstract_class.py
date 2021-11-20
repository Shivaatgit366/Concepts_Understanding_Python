# Concept : Abstract class is the parent/base class and many child/sub classes are derived from it.
# Abstract class has an abstract method which plays very important role. Note: abstractmethod is a decorator.
# All the child/sub classes of Abstract class should have same Abstract method with same name in all of them.

# abc is a module which has all in built abstract base classes.
# So we import abstract class and abstract method from that module.

from abc import ABC, abstractmethod
# abstract method is a decorator. Similar to class method which was also a decorator.
# ABC/ABCMeta is the abstract class. In the new version, name of ABCMeta is reduced to ABC.
# Instead of argument metaclass = ABCMeta, we can simply write ABC.
class Shape(ABC): # Shape class is the base/abstract class now, it gives instructions to all the classes.
    @abstractmethod  # abstract method means this method is same for all the child classes of the Shape class.
    def printarea(self): # this method should be defined in all the derived classes.
        return 0
class Rectangle(Shape):  # A class is being defined from base class.
    type = "Rectangle"
    sides = 4
    def __init__(self):  # constructor is used to define the attributes.
        self.length = 6
        self.breadth = 7
    def printarea(self):  # this method should be compulsorily used in all the classes otherwise we get error.
        return self.length * self.breadth  # this method can be defined however we want.
rect1 = Rectangle()
print(rect1.printarea()) # result is   42.

# So, using the metaclass, base class can give instructions to all the child classes.
# Remember : We can not create an object using abstract class.
# object22 = Shape()  # this is an error since abstract class can not instantiate.

