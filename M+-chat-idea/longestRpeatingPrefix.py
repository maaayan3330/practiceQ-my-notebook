# Write a function that takes a string s and returns the length of the longest prefix that 
# also appears again somewhere else in the string (not as the prefix itself).
# The prefix cannot be the entire string.


def longest_repeating_prefix(s):
    max_len = 0

    for j in range(1, len(s)):
        i = 0
        current_len = 0
        
        while j < len(s) and s[i] == s[j]:
            current_len += 1
            i += 1
            j += 1

        max_len = max(max_len, current_len)

    return max_len

print(longest_repeating_prefix("ababab"))  
print(longest_repeating_prefix("abcabxyz"))  
print(longest_repeating_prefix("abcdef"))
print(longest_repeating_prefix("aaaaaa"))