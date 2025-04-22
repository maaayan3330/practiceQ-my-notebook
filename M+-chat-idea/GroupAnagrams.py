#Write a function that takes a list of strings and groups the anagrams together.
#Return the result as a list of lists.

def groupAnagrams(listOfString):
    # make empty dict that -  sortword : word
    dictOfWords = {}

    for word in listOfString:
        # sort the word to know where to put it in the dict
        sortWord = ''.join(sorted(word))
        if sortWord not in dictOfWords:
            dictOfWords[sortWord] = []
        dictOfWords[sortWord].append(word)

    return list(dictOfWords.values())


print(groupAnagrams(["se" , "ed" , "es"]))