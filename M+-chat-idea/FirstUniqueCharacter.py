# Write a function that takes a string s and returns the index of the
# first non-repeating character in the string.
# If there is no such character, return -1.

def firstchar(str):
    # empty dict
    dictfeq ={}


    for ch in str:
        dictfeq[ch] = dictfeq.get(ch , 0) + 1

    for i, ch in enumerate(str):
        if dictfeq[ch] == 1:
            return i
    
    return -1

print(firstchar("gghhju"))
    



