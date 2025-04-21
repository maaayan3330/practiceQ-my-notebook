#Write a function that takes a string s and returns the length of the longest 
# contiguous substring in which all characters are unique (no duplicates).


def longest(word):
    seen = set()
    left = 0
    maxlen = 0

    for right in range(len(word)):
        while word[right] in seen:
            seen.remove(word[left])
            left += 1
        seen.add(word[right])
        maxlen = max(maxlen, right - left + 1)

    return maxlen

print(longest("abcabcbb"))  # ➜ 3
