# 2️⃣ Generate a Synthetic Dataset with a Given Mean and Standard Deviation
import random

def generate_data(x,y,z):
    return [round(random.gauss(y, z), 2) for _ in range(x)]

elements = 10
avg = 25
std = 20
print(generate_data(elements,avg,std))
