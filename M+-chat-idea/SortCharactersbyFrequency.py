#Write a function that takes a string s, and returns a new string 
#where the characters are sorted in descending order of their frequency.
#The most frequent character comes first (repeated accordingly), followed by the next frequent, etc.

def sortChar(word):
    # first i will make a dict val : frequentsy
    frqDict = {}

    for ch in word:
        frqDict[ch] = frqDict.get(ch, 0) + 1

    sorted_char = sorted(frqDict.items(), key=lambda x: x[1], reverse=True)

    result = ""
    for char, count in sorted_char:
        result += char * count

    return result

print(sortChar("tree"))


    
