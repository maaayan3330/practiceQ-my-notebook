# Given a string s, return the longest palindromic substring in s.



def longestPalindrome(s):
    # if the 
    if len(s) == 0:
        return ""
    # index to keep the start and end of the biggest poli
    start = 0
    end = 0

    # move char char
    for i in range(len(s)):
        # we will check the two possible opttion 
        len1 = expand_from_center(s, i, i)     # odd
        len2 = expand_from_center(s, i, i + 1) # even
        max_len = max(len1, len2)

        # if we found a bigger poli 
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + (max_len) // 2
    # the str 
    return s[start:end + 1]


def expand_from_center(s, left, right):
    # start from inside outside
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
