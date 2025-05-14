# over again for croed strike

# problem 1 E - Contains Duplicate
# def cotain(nums):
#     seen = set()

#     for i in nums:
#         if i in seen:
#             return True
#         seen.add(i)
    
#     return False

#  good i did by myself 10/10

#####################################################
# problem 2 E - Valid Anagram
# sort - nlogn
# dict - o(n) : dictionery by freq
# def valid_anagram(str1, str2):
#     dict1 = {}
#     dict2 = {}
    
#     for i in str1:
#         dict1[i] = dict1.get(i, 0) + 1
    
#     for i in str2:
#         dict2[i] = dict2.get(i, 0) + 1
    
#     return dict2 == dict1

# print(valid_anagram("ggft" , "tfgg"))
# print(valid_anagram("ggft" , "tfhhhgg"))
# print(valid_anagram("ggft" , "tfg"))

# good i did it by my self 10/10
###################################################
# problem 3 E - two sum
# def twosum(nums , target):
#     seen = {}

#     for i , num in enumerate(nums):
#         result = target - num 
#         if result in seen:
#             return [seen[result],i]
#         seen[num] = i
    
# print(twosum([5,7,6,2,4,8] , 8))
# print(twosum([5,7,6,2,4,8] , 690))
# print(twosum([5,7,6,2,4,8] , 6))

# good
######################################################
# problem 4 M - Group Anagrams

# def group_anagram(strs):
#     dictBySort = {}

#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in dictBySort:
#             dictBySort[sorted_word].append(word)
#         else:
#             dictBySort[sorted_word] = [word]
        
#     return list(dictBySort.values())
# print(group_anagram(["hii","ddd", "ihi" , "gtg", "ggt"]))

#########################################################
# problem 5 M - Top K Frequent Elements
# sort is esey and - nlogn 
# better idea in o(n) - do a dict by freq - amd then put in an array in this Legality - arr[the placement == freq] = the value
 
# def topK(nums , k):
#     result = []
    
#     dict_by_freq = {}
#     for num in nums:
#         dict_by_freq[num] = dict_by_freq.get(num, 0) + 1
    
#     arr = [[] for _ in range(len(nums) + 1)]

#     for num , freq in dict_by_freq.items():
#         arr[freq].append(num)

#     for i in range(len(arr) - 1, -1, -1):
#             for num in arr[i]:
#                 if len(result) < k:
#                     result.append(num)
#                 else:
#                     return result

#     return result
# print(topK([1,3,4,4,42,2,3,3,6,5,7], 3))
##############################################################################
# probkem 6 M - Encode and Decode Strings

# def encode(strings):
#     result = []
#     for str in strings:
#         len_of_word = str(len(str))
#         result.append(len_of_word)
#         result.append("#")
#         result.append(str)
#     return ''.join(result)


# def decode(strs):
#     arr = []
#     i = 0
#     while i < len(strs):
#         j = i
#         while strs[j] != '#':
#             j += 1
#         length = int(strs[i:j])  
#         word = strs[j+1 : j+1+length]  
#         arr.append(word)
#         i = j + 1 + length  
#     return arr
        



