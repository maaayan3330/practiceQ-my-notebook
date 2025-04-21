#Write a function that takes a string s, and returns True if it can be turned into a palindrome by changing at most one character.
#Return False if more than one change would be needed.

def can_be_palindrome_with_one_change(word):

    right = len(word) - 1
    left = 0
    mistake = 0

    while left < right :
        if word[right] != word[left]:
            if mistake > 0 :
                return False
            mistake += 1
        
        right -= 1
        left += 1
    
    return True

print(can_be_palindrome_with_one_change("abohjoca"))