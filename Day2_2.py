# 4️⃣ Remove duplicates from a list while maintaining order.

list1 = [1,12,45,77,3,21,1,44,54,77,54]
def remove_dup(list):
    result = []
    for i in list:
        if i in result:
            pass
        else:
            result.append(i)
    return result  

print(remove_dup(list1))
