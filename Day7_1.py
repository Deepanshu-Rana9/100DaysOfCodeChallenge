# 2️⃣ Implement a function to flatten a nested list.
list1 = [109, [287, 85, [123, 99]], 69, [[77], 80], 10]
def flatten(nested_list):
    flat_list = []
    
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
            
    return flat_list

print(flatten(list1))
