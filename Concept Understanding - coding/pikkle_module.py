# pickling concept:-
# Pickling is a process of storing list, tuple or any objects in a file with binary format. It preserves objects.
# The binary data is stored in main memory as a file. Later, the file can be retrieved using pickle module.

# First step, we should make a file with .pkl extension to store the object in binary format.
# Second step, file pointer is assigned and should be opened in "wb" mode for writing binary mode files.
# Third step, both the object and file pointer should be sent as arguments inside dump() function.

# here is an example of pickling concept.
# import pickle
# cars = ["Audi", "BMW", "shivaCar", "Mercedes", "Bugatti"]  # a list object.
# "mycar" is a pickle which is not yet created. We want to send the above list object into the "mycar" pickle file.
# my_file = open("mycar.pkl", 'wb')  # this is a file pointer which opens file in write binary mode.
# pickle.dump(cars, my_file)  # using dump(), both object and file pointer are sent.
# my_file.close()  # file pointer is also known as file object. All the opened file pointers should be closed.
# after running the code, "mycar.pkl" file will be created. But it can not be read as it is in binary mode.


# Unpickling concept:-
# If a file is in binary format, we can't read it. So, we should open file in "rb" mode to read the binary file.
# In Unpickling, we use load() function to retrieve the original object.
# For example, if we send a list while pickling, the return result will also be a list while unpickling.

# here is an example of unpickling concept.
# import pickle
# myfile = open("mycar.pkl", "rb")  # To open any file in a program, file pointer is required.
# py_list = pickle.load(myfile)  # file pointer is sent inside load() function to retrieve back the object.
# myfile.close()  # file pointer is closed.
# print(py_list)  # we get back the original list or object by unpickling method.


# 2 more examples on pickling and unpickling are given below.

# another Pickling example is given below.
# import pickle
# list1 = ["abacus", "bugatti", "hhdd22", "mercedes"]
# var = "mycar2.pkl"
# file_point = open(var, "wb")
# pickle.dump(list1, file_point)
# file_point.close()


# another Unpickling example is given below.
# import pickle
# var2 = "mycar2.pkl"
# myfile = open(var2, "rb")
# original_object = pickle.load(myfile)
# myfile.close()
# print(original_object)

# ------------------------*------------------------*---------------------------*---------------------*-------------

