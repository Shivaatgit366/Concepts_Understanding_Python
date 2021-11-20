# Iterable means it's an object which can be set into a loop. For every iteration, this object gives one value.
# example: a list, a string, a tuple etc. can be an iterable.
# Iterators are the objects which does iterations on iterables. Iterators move from character to character.
# Every iterable has 2 functions, they are __iter__() and __next__().
# Phenomenon which occurs using the combination of these two functions is called iteration.


# The concept of Generators also similar. Generator function makes an iterator.
# This function is called indirectly. This function is called when __next function is called.
# Instead of return keyword, we use "yield" keyword for obtaining the value.
# Whatever the values obtained by this process is "in sequence". We get value one after another.
# Generators save memory of the computer because values are obtained sequentially.


# for i in range(2100000000000): # we get the values on the fly.
# RAM memory is less, still we get values one by one.
#     print(i)
# but, in generators, we get value only one time whenever we call it using __next function.
# we should call repeatedly to obtain all the values.
# yield keyword brings the values from that point where it has completed last time.


# def gen(n): # generators are the functions which makes an iterator.
#     for i in range(n):
#         yield i  # yield keyword will generate the values on the fly.
# m = gen(66655455545665445545565)
# print(m)  # <generator object gen at 0x0000024DB89FB900>  we get the location of the generator.


# below example shows how to get the values from the generators using next function.
# def gen(n):
#     for i in range(n):
#         yield i
# m = gen(5)
# print(m.__next__())
# print(m.__next__())
# print(m.__next__())
# print(m.__next__())
# print(m.__next__())
# print(m.__next__())  # we get the error message as "stop iteration".



# iter() creates iterator and next function brings character after character.
# h = "shiva" # string is an iterable which can be traversed through using an iterator.
# only in iterables, __iter or __getitem functions are defined.
# so, whenever the iter() function is used, iterators get generated.
# ie = iter(h) # iter function is applied on the iterable, so we get ie as iterator.
# print(ie.__next__())  # we get result as s h i v a and stop iteration.
# print(ie.__next__())
# print(ie.__next__())
# print(ie.__next__())
# print(ie.__next__())
# print(ie.__next__())


# --------------------------------*--------------------------------*-------------------------------------*-------

