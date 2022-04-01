# 1) re.search() gives the matched object data and boolean also.
# 2) re.split() it splits the string at the given pattern and gives the list output.
# 3) re.findall() it gives the list of all the matches in the string.
# 4) * means any number of that pattern. Even zero also OK.
# 5) + means one or more number of that pattern.
# 6) ? means zero or one time available.
# 7) {} means the number of times pattern occurs.
# 8) {1,3} means one or three times pattern occured.
# 9) [sd]+ means a character "s" or "d" occurs one or more times.
# 10) we use carrot symbol ^ for the exclusion.
# 11) [^.!?]+ means any character ".!?" occured one/more times will be excluded from the string.
# 12) [a-z]+ means any character with "a to z" small letters, occurred one or more times will be selected.
# 13) [A-Z]+ means any character with "A to Z" big letters, occurred one or more times will be selected.


import re

def matched_items_returner(patterns, phrase):
    for pat in patterns:
        print("bro I am searching the pattern")
        print(re.findall(pat, phrase))
        print("\n")


test_phrase = "This is a string! it has punctuation. How are you??..ssssdddd..sddddssdddd..dd..ss....dddddsdd"

test_patterns = ["[a-z]+"]  # we should not put the blank spaces.

matched_items_returner(test_patterns, test_phrase)

# we use ^ for the exclusion.
# first only the simple things were seen. But in pattern, every character has it's own different value.
