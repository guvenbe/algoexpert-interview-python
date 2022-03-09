def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}  # hasmap to store if number has explored

    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        curentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            curentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            curentLength += 1
            right += 1
        if curentLength > longestLength:
            longestLength = curentLength
            bestRange = [left + 1, right - 1]
        return bestRange

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))