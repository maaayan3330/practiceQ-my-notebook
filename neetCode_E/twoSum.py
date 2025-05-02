# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# my idea - to do set and mive all over the array once    נגיד אני על 5 אז אני מורידה את המטרה ובודקת אם המשלים כבר ראיתי אותו - 0
# o(n) that to go all over the array 
# get in and out from the dict it is o(1) --- so o(n)

def sumTwo(nums, target):
    seen = {}

    for i , num in enumerate(nums):
        cal = target - num
        if cal in seen:
            return [seen[cal], i]
        seen[num] = i

print(sumTwo([5,7,6,2,4,8] , 8))
print(sumTwo([5,7,6,2,4,8] , 690))
print(sumTwo([5,7,6,2,4,8] , 6))