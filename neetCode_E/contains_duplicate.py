# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# my first idea - i can move all over the array one time and count on other array according to the index , Time complexity = o(n) but space complexity o(n)
# naive algorithem is to - move all over the array for one index evey time - o(n^2)
# my best idea is - is likt the first one - just esier to compelte

# this ia an idea with exetra place o(n)
def duplicate(nums):
    # empty set
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

print(duplicate([3,5,6,7]))
print(duplicate([3,5,3,7]))
print(duplicate([3,5,6,7,7]))

