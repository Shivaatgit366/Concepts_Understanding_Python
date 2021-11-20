# Caching means to store the data outside the main memory and serve faster whenever required.
# computer assigns a cache memory, so it does not have to load it again and again from the main memory.

# here is an example which shows the need for function cache.
# import time
# def some_work(n):
#     time.sleep(n)  # sleep function will hold that many seconds in the brackets for execution of next code line.
#     return n
# if __name__ == '__main__':
#     print("Now running some work")
#     print(some_work(10))
#     print("OK done")
#     print(some_work(10))  # even though same function with argument is called, it still takes 10 seconds for output.
# so we need to make use of the concept "function caching".
# Next time same function with same argument is called, it gives the value quickly.


import time
from functools import lru_cache  # lru cache is a decorator. A function which takes function as an argument.
@lru_cache(maxsize = 4)  # this maxsize will take as many value as cache as we want. Here 4 values are cached.
def some_work(n):
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("some work is running now")
    print(some_work(10))
    print(some_work(10))  # this output will obtained within no time since the value is cached.
    print(some_work(20))
    print(some_work(10))  # this output will obtained within no time since the value is cached.
    print(some_work(8))
    print(some_work(20))  # this output will obtained within no time since the value is cached.
    print(some_work(8))   # this output will obtained within no time since the value is cached.

# -------------------------*----------------------*---------------------------*-----------------*-----------------


