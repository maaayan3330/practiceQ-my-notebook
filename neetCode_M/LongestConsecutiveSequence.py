# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# even more naive - consider every element from the array as the start of the sequence and count the length of the sequence formed with that starting element. This would be an O(n^2) solution.
# first way - the naive - sort + move all over it - nlogn
# better way - get all inside in set - o(n)
#             - בעצם המספר נכנ סלwhile רק אם הוא הראשון ברצף ולכן לא כולם בכלל נכנסים לתנאי השני ואז זה רק המעבר עם ה for

# בעצם הפואנטה שלומדים מהשאל הזו שבגלל שמחפשים את ההכי ארוך צריך לבדוק תחיליות אין  מה לעבור שום על המספרים שכבר ראינו באמצע הסדרה
def longest(nums):
    set_of_nums = set(nums)
    result = 0

    for num in set_of_nums:
        # check if this num is a start
        if (num - 1) not in set_of_nums:
            lenght = 1
            current = num

            while (current + 1) in set_of_nums:
                current += 1
                lenght += 1
            
            if result < lenght:
                result = lenght
    
    return result
print(longest([1,4,3,8,5,2,21]))

