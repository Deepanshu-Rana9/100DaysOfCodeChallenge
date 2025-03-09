# 2️⃣ Implement a function to generate all permutations of a given list of numbers.
numbers = [6,9,0]

def generate_permutations(list1, start=0):
    if start == len(list1) - 1:
        print(list1)
        return
    
    for i in range(start, len(list1)):
        list1[start], list1[i] = list1[i], list1[start]
        generate_permutations(list1, start + 1)
        list1[start], list1[i] = list1[i], list1[start]

generate_permutations(numbers)
