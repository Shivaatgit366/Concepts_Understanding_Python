# Random module in Python used to generate random numbers, random items.
# It has many useful functions in it. Import the built in random module to use these functions.

# 1) choice() function used to generate random item from particular object such as list, tuple, string.
# See the below example. We print a random value from the list.
# import random
# list1 = [1, 2, 3, 4, 5, 6]
# print(random.choice(list1))  # put the object inside the choice function.


# 2) randrange(beg, end, step) :- This function takes start, end and step of increment.
# See the example, we want to generate random number between 20 and 50 with skipping 3 numbers every time.
# import random
# print("A random number between 20 and 50 with step size 3 is : ", end="")
# In Python print(), end character is "\n" by default. So, to print contents in a single line, we use end="".
# print(random.randrange(20, 50, 3))  # we get random number like 23, 20, 41, 47 etc.


# 3) random() :- this function generates a floating point number from this range (0, 1)
# See the example, we can see the random() function working.
# import random
# print("A random number between 0 and 1 is : ", end="")
# print(random.random())  # we get numbers like 0.7852769328708478, 0.5853121474846757, 0.9576469209655707 etc.


# 4) uniform(a, b) :- this function gives random floating number from the range (a, b)
# See the example below.
# import random
# print("the random floating number between 5 and 20 is : ", end="")
# print(random.uniform(5, 20))  # we get 6.108833237605949, 11.639805625799578, 15.295333840536285 etc.


# 5) randint(a, b) :- this function generates an integer in the range [a, b] where a and b are integers.
# See the example below. Here both "a" and "b" are included. This function available only in Python 3.
# import random
# print("The random integer between 5 and 20 is : ", end="")
# print(random.randint(5, 20))  # we get numbers like 19, 6, 20, 14 etc.

# --------------------------*-----------------------------*--------------------------------*-----------------------
