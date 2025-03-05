# 6️⃣ Implement a function to check if two given lists have any common elements.

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,14,15,16,9,2,19,20]

def common(a,b):
    for i in a:
        if i in b:
            print("There is a common element in both lists:",i)

common(list1,list2)