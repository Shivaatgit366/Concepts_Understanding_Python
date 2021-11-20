# In other languages, "else" can be used only if the "if" word is used.
# But in Python, "else" can be used even without the word "if".

# "else" word is used inside the for loop without the "if" word.
# "else" code block is considered if there is no "break" word.

# the following example shows the usage
# for i in [0,2,4,8,10]:
#     print(i)  # after the completion of all iterations, else code block is implemented.
# else:
#     print("operation successfully completed")


# here is another example below which shows how to use for loop with else statement.
# khana = ["roti", "Sabzi", "chawal"]
# for item in khana:
#     if item == "rotiroll":
#         break
#     else:  # remember this else statement is inside the loop, below line will be printed 3 times.
#         print("Your item was not found")
# else:  # this statement will be executed immediately after the successful execution of the loop.
#     print("Your item has not been found, loop completed successfully")

# Note: Imagine item == "roti" was written in the "if" statement, both "else" code blocks would not be executed.
# "else" code block will be executed only after the completion of for loop.
# if the code is broken using break statement in between, then "else" code block will not be executed.

# ----------------*--------------------*------------------------*----------------------------*-----------------*---
