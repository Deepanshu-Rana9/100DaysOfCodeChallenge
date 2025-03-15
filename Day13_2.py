# Word Frequency Counter
import re
from collections import Counter

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words)) 

text = "I am currently pursuing a degree in Artificial Intelligence & Data Science, developing expertise in data analysis."

print(word_frequency(text))
