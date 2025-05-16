# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

# o(n^2)
def longest(s):
    max_val = 0
    len_s = len(s)

    for i in range(len_s):
        seen = set()
        sum = 0
        j = i
        while j < len_s:
            if not(s[j] in seen):
                seen.add(s[j])
                sum += 1
                j += 1
                max_val = max(sum, max_val)
            else:
                odd = s[j]
                break
        
        while i < len_s and s[i] != odd:
            i += 1

        i += 1
    
    return max_val

print(longest("zxywxs"))

def longestBetter(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

        

    

                



