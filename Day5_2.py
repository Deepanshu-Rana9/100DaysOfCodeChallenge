# 1️⃣ Implement a Function to Compute the Median Absolute Deviation (MAD)

import statistics
data = [9, 3, 5, 100, 1, 11, 7]

def mad(list1):
    result = []
    median_value1 = statistics.median(list1)
    for i in list1:
        value = i - median_value1
        value = abs(value)
        result.append(value)
    Mad = statistics.median(result)
    return Mad

print(mad(data))
    