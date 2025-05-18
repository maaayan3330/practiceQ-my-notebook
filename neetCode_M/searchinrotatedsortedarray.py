# You are given an array of length n which was originally sorted in ascending order.
# It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
# You may assume all elements in the sorted rotated array nums are unique,
# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

def search_target(nums , target):
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer < right_pointer:
        mid = (right_pointer + left_pointer) // 2

        if nums[mid] == target:
            return mid

        if nums[left_pointer] <= nums[mid]:
            if nums[left_pointer] <= target < nums[mid]:
                right_pointer = mid - 1
            else:
                left_pointer = mid + 1

        else:
            if nums[mid] < target <= nums[right_pointer]:
                left_pointer = mid + 1   # ממשיכים בצד ימין
            else:
                right_pointer = mid - 1  # ממשיכים בצד שמאל
        
    return -1
            