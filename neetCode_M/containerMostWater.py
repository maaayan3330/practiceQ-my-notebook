# You are given an integer array heights where heights[i] represents the height of the i bar 
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# כאיללו תעבור אחד אחד וכל אחד שאתה עובר כבר בעצם עשית לא צריך לבדוק את הקודם
###########################################################################
# - my soultion - o(n^2)
def water(heights):
    max_water = 0
    length = len(heights)

    for i in range(length):
        for j in range(i + 1, length):
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            max_water = max(max_water, area)

    return max_water


print(water([1,7,2,5,4,7,3,6]))
##########################################################################
# other solution - in o(n)

def max_water(heights):
    left = 0
    right = len(heights) - 1
    max_water = 0

    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        area = height * width
        max_water = max(max_water, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

