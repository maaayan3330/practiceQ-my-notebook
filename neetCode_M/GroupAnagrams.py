# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# to sort every word and put inside an dict - (n * k log k)
# sort every word and n for n words we do the sorting
def anagram(arrOfStr) :
    dict_seen = {}

    for word in arrOfStr:
        key = ''.join(sorted(word)) 
        if key in dict_seen:
            dict_seen[key].append(word)
        else:
            dict_seen[key] = [word]

    return list(dict_seen.values())

print(anagram(["hii","ddd", "ihi" , "gtg", "ggt"]))
        
