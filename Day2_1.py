# 3️⃣ Find the second largest number in a list.

list1 = [1,12,45,77,3,21,1,44,54]

def second_largest(list):
    list.sort()
    return list[-2]

print(second_largest(list1))
