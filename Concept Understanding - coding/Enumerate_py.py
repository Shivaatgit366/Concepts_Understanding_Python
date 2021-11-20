# Enumerate function gives numbering to all the items in the list,tuple etc.
# syntax is    enumerate(iterable, start=0)

# below is an example of enumerate function on list.
# shiva = ["apple", "banana", "cherry", "ducks"]  # a list.
# enumshiva = enumerate(shiva, 5)  # items in shiva will be numbered from 5.
# print(enumshiva)  # it gives the location of the object. It should be converted using type casting.
# print(list(enumshiva))  # data converted into list with index number starting from 5.


# We can loop through string, tuple or objects using enumerate()
# below is the example how enumerate() method is used in for loop.
# shiva = ["apple", "banana", "cherry", "ducks"]
# for index, item in enumerate(shiva):
#     if index % 2 == 0:  # % means mod function operator.
#         print(item)  # we get the result as   apple and cherry


# here is another example.
# l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]
# conventional method, index value fixed to 1 outside the loop, incremental statement given inside for loop.
# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

# enumerate method, serial number is automatically assigned from 0.
# for index, item in enumerate(l1):
#     if index % 2 == 0:
#         print(f"Jarvis please buy {item}")

# ---------------------*---------------------*------------------*--------------------*----------------*------------

