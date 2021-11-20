# Coroutines are similar to generators, generators give series of values.
# But in Coroutines, we wait for input values in every step.
# coroutines also give sequence of values but here we take input values every time.
# In coroutines, a variable is assigned for the yield value.
# Coroutines make use of next() and send() methods, input is given using send() in every step.
# coroutines are used in lengthy programmes such as machine learning and deep learning.
# In lengthy programmes, we have to execute the codes repetitively, in such case coroutines will be helpful.


# here is an example of coroutine.
def searcher():  # coroutine is being defined, it is a function.
    import time
    # some 4 seconds time consuming task is there.
    book = "This is a book named code with Harry and here we are learning about coroutines"  # a string.
    time.sleep(4)  # a book which is taking 4 seconds to read
    while True:  # infinite while loop is executed.
        text = (yield)  # yield value is stored as text.
        if text in book: # during the iteration, if "text" value is present in "book", then we say it is present.
            print("the text is present in the book")
        else:  # if "text" value is not present in "book", then we say it is not present.
            print("the text is not present in the book")
search = searcher()  # a variable is assigned with a coroutine function.
print("this line will be printed first, coroutine will start only after the next function")
# above line will be printed first, coroutine will start only after the next function.
next(search)  # next function should be used and that variable is sent as a parameter.
search.send("is")  # input is sent inside the send function.
input("give any input\n")
search.send("boo") # this string is present in the book.
input()
search.send("boo4") # this string is not present in the book.
search.close()  # this function closes the coroutine.
search.send("book2")  # if we send another input after closing coroutine, we get error message as "stopIteration".


# ----------------------*-------------------*-----------------------*----------------------------*-----------------

