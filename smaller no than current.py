def smaller_numbers_than_current(nums):
    result = []
    for i in range(len(nums)):
        count = sum(1 for j in range(len(nums)) if j != i and nums[j] < nums[i])
        result.append(count)
    return result

nums = [8, 1, 2, 2, 3]
output = smaller_numbers_than_current(nums)
print(output)
