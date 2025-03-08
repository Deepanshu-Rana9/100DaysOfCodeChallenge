# 1️⃣ Compute Moving Average of a List

list1 =[10,20,30,40,50,60,70,80,90]
interval = 3
average = []

def moving_average(data,weight):
    for i in range(len(data)-weight+1):
        new_list = data[i:i + weight]
        avg = sum(new_list)/weight
        average.append(avg)
    return average

print(moving_average(list1,interval))
