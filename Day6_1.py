# 1️⃣ Encode Categorical Data (One-Hot Encoding)

categories = ["Red", "Blue", "Red", "Green", "Blue"]

def encode(list1):
    new_list = list(set(list1))

    encoded = [[1 if category == unique else 0 for unique in new_list] for category in list1]

    for data,value in zip(new_list,encoded):
        print(f"{data}:{value}")
    

encode(categories)