# Algorithm Challenge - Number Sequence Analysis
list1 = [55,77,44,33,22,54,54,23,65]

def temperature(temps):
    n = len(temps)
    result = [0] * n
    stack = [] 
  
    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            prev_index = stack.pop() 
            result[prev_index] = i - prev_index  
        stack.append(i)  
    return result

print(temperature(list1))