# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

def findmin(nums):
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer < right_pointer:
        mid = (left_pointer + right_pointer) // 2

        # אם האיבר גדול מהאמצע האיבר חייב להיות מצד ימין
        if nums[mid] > nums[right_pointer]:
            left_pointer = mid + 1
        else:
            right_pointer = mid

    return nums[left_pointer]