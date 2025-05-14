# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.
# Follow-up: Could you solve it in O(n) time without using the division operation?

# first answer with divtion
# def sumS(nums) :
#     sums = 1
#     for i in nums:
#         sums = sums * i
    
#     arr = []

#     for i in range(len(nums)):
#         arr.append(int(sums / nums[i]))
    
#     return arr

# print(sumS([1,2,4,6]))


# the other way without divide

# Input: nums = [1,2,4,6]   -  output - [48 , 24, 12 , 8] - מה שבלבל אותי זה שפה בעצם שומרים את כל ההכפלות עד האיבר ולא כולל ולכן זה יוצא כמו שאני רושמת ליד
def sumSpecial(nums) :
    n = len(nums)
    front_to_back = [1] * n      # everything before i    [1, 1, 1, 1]
    back_to_front = [1] * n      # everything after i     [1, 1, 1, 1]
    output = [0] * n             #                        [0 ,0 ,0 , 0]

    for i in range(1,n): # this is till n becuese as i said we dont calculte the i it self just till him
        front_to_back[i] = front_to_back[i - 1] * nums[i - 1]   # [1 ,1 ,2 ,8]

    for i in range(n - 2, -1, -1):
        back_to_front[i] = back_to_front[i + 1] * nums[i + 1]  #  [48 ,24 ,6 ,1]
    
    for i in range(n):
        output[i] = front_to_back[i] * back_to_front[i]

    return output

print(sumSpecial([1, 2, 4, 6]))