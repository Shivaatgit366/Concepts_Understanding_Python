# "==" this is used for value equality. Two objects have the same value.
# "is" keyword is used for reference equality, which is based on memory location. Two references have same object.

# console means command prompt, which is similar to microsoft powershell.
# Console method is the oldest method of accessing and writing codes in the computer for the execution of things.
# It is c language compiler, if we write variable "a" and hit enter, we get the list. No need to write print().

a = [5, 7, 8, "hello"]
b = [5, 7, 8, "hello"]
print(b is a)  # we get result as False
print(b == a)  # we get result as True

# ---------------------------*-------------------------*---------------------------*---------------------------------

