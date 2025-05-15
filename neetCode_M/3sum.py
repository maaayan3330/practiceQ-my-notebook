# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

def sum3(nums):
    sort_nums = sorted(nums)
    result = []

    for i in range(len(sort_nums)):
        # דילוג על כפילויות
        if i > 0 and sort_nums[i] == sort_nums[i - 1]:    # so we dont need to do the process for them twice it is the same number
            continue

        pointer_start = i + 1
        pointer_end = len(sort_nums) - 1

        while pointer_start < pointer_end:
            total = sort_nums[i] + sort_nums[pointer_start] + sort_nums[pointer_end]

            if total == 0:
                result.append([sort_nums[i], sort_nums[pointer_start], sort_nums[pointer_end]])

                # דילוג על כפילויות
                while pointer_start < pointer_end and sort_nums[pointer_start] == sort_nums[pointer_start + 1]:
                    pointer_start += 1
                while pointer_start < pointer_end and sort_nums[pointer_end] == sort_nums[pointer_end - 1]:
                    pointer_end -= 1

                pointer_start += 1
                pointer_end -= 1

            elif total < 0:
                pointer_start += 1
            else:
                pointer_end -= 1

    return result

        
      

print(sum3([-1,1,2,-1,3,-2]))
