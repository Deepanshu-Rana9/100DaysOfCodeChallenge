# Longest Consecutive Sequence
num = [100, 4, 200, 1, 3, 2]
def longest_con(nums):
    nums.sort()  
    longest, current = 0, 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        if nums[i] == nums[i - 1] + 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1 

    return max(longest, current) 

print(longest_con(num))
