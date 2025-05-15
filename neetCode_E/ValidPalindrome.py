# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. 
# It is also case-insensitive and ignores all non-alphanumeric characters.

# keep it in one string - move in window - o(n)

def poli(s):
    full_s = [ch.lower() for ch in s if ch.isalnum()]
    # עוברת על כל תו ומוודא שהוא מסספר או אתיות ואז הופכת גם לאותיות קטנות
    
    pointer_to_start = 0
    pointer_to_end = len(full_s) - 1

    while pointer_to_start < pointer_to_end:
        if full_s[pointer_to_start] == full_s[pointer_to_end]:
            pointer_to_start += 1
            pointer_to_end -= 1
        else:
            return False
    
    return True

print(poli("A man, a plan, a canal: Panama"))  # True
print(poli("race a car"))                      # False