#Given a list of strings, write a function that returns the longest common prefix shared by all the strings in the list.
#If there is no common prefix, return an empty string "".
#If the input list is empty, also return an empty string.

def compareList(words):
    # first check  list not empty
    if not words:
        return ""
    
    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

words = ["flower", "flow", "flight"]
print(compareList(words)) 