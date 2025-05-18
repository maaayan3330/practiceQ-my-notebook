# Longest Repeating Character Replacement
# You are given a string s consisting of only uppercase english characters and an integer k. 
# You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

def longest(s, k):
    count = {}
    left_pointer = 0
    res = 0
    max_ch_in_win = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0) + 1
        max_ch_in_win = max(max_ch_in_win, count[s[right]])

        while (right - left_pointer + 1) - max_ch_in_win > k :
            count[s[right]] -= 1
            left_pointer += 1
        
        res = max(res, right - left_pointer + 1)
        
    return res

print(longest("XYYX", 2))