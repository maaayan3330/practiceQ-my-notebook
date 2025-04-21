#Write a function that takes two strings s1 and s2, where the # character represents a backspace (deleting the character before it).
#Return True if both strings are equal after applying all backspaces. Otherwise, return False.

def deleteChar(wordOne, wordTwo):
    def process(word):
        stack = []
        for ch in word:
            if ch == '#':
                if stack:
                    stack.pop()  # מוחק את התו הקודם
            else:
                stack.append(ch)  # שומר את התו הנוכחי
        return ''.join(stack)

    return process(wordOne) == process(wordTwo)


    

print(deleteChar("ab#c", "ad#c"))             
