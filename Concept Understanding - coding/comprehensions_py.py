# Comprehension in Python : It means to write any code in a short and more accurate way.
# Due to this, 5 to 6 code lines will be reduced to 1 line code.

# listA = []  # an empty list is written first, we need to fill the list with proper values.
# for item in range(50):
#     if item % 5 == 0:  # condition is applied
#         listA.append(item) # all the values which satisfies the conditions, will be appended in the list.
# print(listA)

# so, these codes can be reduced into a single line of code in the following way.

# this is an example of list comprehension.
# listA = [item for item in range(50) if item % 5 == 0] # first write the name of the item you want inside the list.
# later, apply the conditions but don't use commas or colons.
# print(listA)

# here is an example of set comprehension.
# alpha = {alpha for alpha in ["a", "a", "b", "c", "c", "d", "d"]} # in set comprehension curly brackets are used.
# in sets, we don't get repeated items and also result is not ordered.
# print(alpha) # we get the out put as {'a', 'b', 'c', 'd'}, even we get {'a', 'd', 'c', 'b'} also.

# here is an example of dictionary items.
# mydict = {
#     0 : "item0",
#     1 : "item1",
#     2 : "item2",
#     3 : "item3",
#     4 : "item4",
#     5 : "item5",
#     6 : "item6"
# }
# print(mydict)  # a simple dictionary is prepared just by typing everything, it takes more time in typing.
# using dict comprehension technique it is easy to generate a dictionary in one line.
# compdict = {items for items in mydict}  # it only gives "keys" of the dictionary.
# print(compdict)
# reqdict = {i: f"item{i}" for i in range(7)} # item word is added using f string.
# print(reqdict)

# here is an example of dictionary items.
# mydict = {
#     0 : "item0",
#     1 : "item1",
#     2 : "item2",
#     3 : "item3",
#     4 : "item4",
#     5 : "item5",
#     6 : "item6"
# }
# print(mydict)
# using dict comprehension technique it is easy to reverse the key value items. we can see below.
# reqdict = {value:key for key,value in mydict.items()} # item word is added using f string.
# Remember : always write key,value in for loop
# Note: .items() method will give all the items of the dictionary.
# print(reqdict)


# we can even use comprehension technique for the case of generators also.
# In the case of generator comprehension, we use paranthesis/normal brackets.
# instead of writing "def" keyword, and "yield" keyword, we can make generator using comprehension technique.
# evens = (i for i in range(100) if i%2==0)  # this is the way we can make generator using comprehension.
# print(evens)  # we get the location of the generator    <generator object <genexpr> at 0x000001EC984F9510>
# print(evens.__next__())  # __next function brings only one value
# print(evens.__next__())
# print(evens.__next__())  # __next function brings only one value
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# __next function gives the sequence of values, one after another.
# for item in evens:
#     print(item)


# -------------------------*----------------------------*------------------*----------------------*---------------

