# 1️⃣ Implement Min-Max Normalization

data = [10, 20, 30, 40, 50]

def normalization(list1):
    result = []
    for i in list1:
        maxi = max(list1)
        mini = min(list1)
        normal = float((i - mini)/(maxi - mini))
        result.append(normal)
    return result

print(normalization(data))