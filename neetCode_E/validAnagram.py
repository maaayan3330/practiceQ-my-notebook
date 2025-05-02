# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# my idea - do two dicts by freq and compare -  time complexity  - o(n) - move one time one the string ,compre is also o(n) so  === o(n)

def compare(str1 , str2):
    # empty dicts
    freq1 = {} 
    freq2 = {}

    for ch in str1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in str2:
        freq2[ch] = freq2.get(ch, 0) + 1

    return freq1 == freq2

print(compare("ggft" , "tfgg"))
print(compare("ggft" , "tfhhhgg"))
print(compare("ggft" , "tfg"))