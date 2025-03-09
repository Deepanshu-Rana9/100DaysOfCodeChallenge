# 2️⃣ Extract Numeric Data from a Noisy Text and Compute Average using (re).
import re

data = "Ratings of this Show on different platforms are 9.8, 8.4 and 9.7 stars."

def average(str):
    numbers = re.findall(r'\d+\.?\d*',str)
    numbers = [float(num) for num in numbers]
    avg = sum(numbers)/len(numbers)
    return round(avg,2)
print(average(data))