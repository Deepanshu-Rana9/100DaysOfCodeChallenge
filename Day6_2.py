# 1️⃣ Find Most Frequent Word in a Data
data = "Machine learning is good. Learning new things is fun. Learning never stops."

def most_frequent_word(str):
    words = str.lower().split()

    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    most_frequent = max(count, key=count.get)
    
    return most_frequent, count[most_frequent]


word, frequency = most_frequent_word(data)
print(f"Most Frequent Word is: '{word}' Appears {frequency} times.")
