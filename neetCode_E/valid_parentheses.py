# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

def valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != mapping.get(ch):
                return False
            stack.pop()

    return len(stack) == 0
