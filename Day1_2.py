# 2️⃣ Count the occurrences of each character in a string.

def count_chars(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_chars("Hello Connections"))