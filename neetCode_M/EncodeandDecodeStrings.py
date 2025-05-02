# Design an algorithm to encode a list of strings to a single string. 
# The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

# encode - return it all as one strind
# decode breack it again

def encode(strs):
    # to keep it all toghter
    result = []
    for word in strs:
        length = str(len(word))  
        result.append(length)
        result.append('#')
        result.append(word)
    return ''.join(result) 

print(encode(["hii","bye", "bro"]))

def decode(strs):
    arr = []
    i = 0
    while i < len(strs):
        j = i
        while strs[j] != '#':
            j += 1
        length = int(strs[i:j])  
        word = strs[j+1 : j+1+length]  
        arr.append(word)
        i = j + 1 + length  
    return arr

print(decode(encode(["hii","bye", "bro"])))

