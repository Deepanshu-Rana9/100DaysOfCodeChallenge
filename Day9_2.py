# 1️⃣ Identify Customers Likely to Churn
customers = [
    ("Ichigo Kurosaki", 10),
    ("Rukia kuchiki", 5),
    ("Renji Abarai", 12),
    ("Yasutora Sado", 9),
    ("Orihime Inoue", 1),
    ("Uryu Ishida", 7)
]
minimum = 6 

def identify_churn(customers, minimum):
    churn = []
    
    for name, last_purchase in customers:
        if last_purchase > minimum:
            churn.append(name)    
    return churn

print(identify_churn(customers, minimum))