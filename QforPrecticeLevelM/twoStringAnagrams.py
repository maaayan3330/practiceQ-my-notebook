#Write a function that takes two strings s1 and s2, and returns True if they are anagrams of each other —
# meaning they contain the same letters, with the same frequencies, possibly in a different order.
#Otherwise, return False.

def anagrams(stringFirst, stringSeoned):
    dicForStract = {}
    stringFirst = stringFirst.lower()
    stringSeoned = stringSeoned.lower()

     # Quick length check – if not same length, can't be anagrams
    if len(stringSeoned) != len(stringFirst):
        return False

    for i in stringFirst:
        dicForStract[i] = dicForStract.get(i, 0) + 1
    
    for i in stringSeoned:
        if i not in dicForStract or dicForStract[i] == 0:
            return False
        
        if i in dicForStract:
            dicForStract[i] -= 1
    
    return True

print(anagrams("aayamn", "maayan"))
        