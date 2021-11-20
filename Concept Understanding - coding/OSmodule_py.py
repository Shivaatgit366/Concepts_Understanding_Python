# OS module is a built in module which has many operating system related functions in it.
# OS module helps us to do various works related to operating systems in programming.
# OS module is used to get directory details, rename folder, changing the directories, creating directories etc.

import os  # OS module is being imported.
# print(dir(os))  # using dir method, we get all the attributes and functions in list format.
# print(os.getcwd())  # it will give current working directory,  C:\Users\Shiva\PycharmProjects\Shiva Projects
# os.chdir("C://")  # this function will change the current working directory to C.
# print(os.listdir())  # this function gives all the files, folders present in that directory in list format.
# print(os.listdir("C://"))
# os.mkdir("This")  # this function creates a directory/a folder. "This" folder is created in this case.
# os.makedirs("This/That/What/Folder")  # creates directories at a time. Folders inside folder is created here.
# os.rename("function_caching.txt", "caching-function.txt")  # this function renames the existing file.
# print(os.environ.get("Path"))  # this function gives information related to environment variable.
# print(os.path.join("c://", "//function_caching.txt"))  # this function will join the path.
# print(os.path.exists("C://program files"))  # function gives boolean value "True" if the path exists.
# we get True because there is a folder "program files" inside C directory.


# print(os.path.isfile("c://program files"))  # function gives boolean value "True" if the path is a file.
# since the above path leads to a directory/folder (which is not a file), we get result as False.

# ------------------*--------------------*---------------------*--------------------*-------------------*----------
