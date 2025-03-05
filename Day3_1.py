# 5️⃣ Write a function that returns the most common element in a given list.

Given_list = [1,2,34,65,54,2,2,4,65,54,4,2,4,5,33,2,32,42,2,76]

def most_common(list):
    count_dict = {}
    for i in list:
        count_dict[i] = count_dict.get(i,0)+1
    most_frequent = max(count_dict, key=count_dict.get)
    return most_frequent

print(most_common(Given_list))