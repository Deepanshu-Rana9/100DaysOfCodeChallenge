# Find Missing Number

def missing_number(nums):
    n = len(nums)
    exp_sum = n * (n + 1) // 2
    act_sum = sum(nums)
    return exp_sum - act_sum

nums = [1,0,3]
print(missing_number(nums))
