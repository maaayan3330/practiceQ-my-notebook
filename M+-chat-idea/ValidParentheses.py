# Write a function that takes a string s containing only '(', ')', '{', '}', '[', ']'
# and returns True if the string has valid, properly nested parentheses.

def validP(str):
    # build a empty stack to store all
    stack = [] 
    # a dict to 
    pairs = {')': '(', '}': '{', ']': '['}

    # start to compare if it is a open - get in to the stack
    for ch in str:
        if ch not in pairs:
            stack.append(ch)
        else:
            # it is a closer so we need to check
            if not stack or stack.pop() != pairs[ch]:
                return False
            
    return not stack

            
        
print(validP("()"))           # ✅ True
print(validP("()[]{}"))       # ✅ True
print(validP("(]"))           # ❌ False
print(validP("([)]"))         # ❌ False
print(validP("{[]}"))         # ✅ True
print(validP("{{[(])}}"))     # ❌ False





        
        
