#Write a function that takes a string s and returns a new string in which any consecutive duplicate characters are reduced to a single character.
#That means – if a character appears multiple times in a row, only one instance is kept.


def removeDup(word):
    if not word:
        return "" 
    
    result = [word[0]]
    for char in word[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)



print(removeDup("aaallllaakkc"))