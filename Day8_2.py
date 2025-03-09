# 2️⃣ Simulate a Simple Dice Roll Experiment and Calculate Probabilities

import random

def dice(n):
    rolls = [random.randint(1, 6) for i in range(n)]
    probablity = {i: rolls.count(i) / n for i in range(1, 7)}
    return probablity

print(dice(2000))
