# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# first idea it is sort  - nlogn
# seconed idea put in dict - freq: num - o(n) BETTER

def topK(nums , k) :
    freq = {}

    # put in dict by - val : freq
    for num in nums:
        freq[num] = freq.get(num , 0) + 1

    # array of list
    arr = [[] for _ in range(len(nums) + 1)]

    # arr[3] = numbers that freq are 3
    for key , value in freq.items():
        arr[value].append(key)

    res = []
    for i in range(len(arr) - 1, 0, -1): # start, stop ,step
        for num in arr[i]:
            res.append(num)
            if len(res) == k:
                return res
            
print(topK([1,3,4,4,42,2,3,3,6,5,7], 3))

        
    
