# 2️⃣ Find Outliers Using IQR (Interquartile Range)
List1 = [5,27,9,10,1100,15,1,20,17,1000]

def detecting_outliers(data):
    data.sort()
    n = len(data)
    index1 = n//4
    index2 = (3*n)//4
    Q1 = data[index1]
    Q3 = data[index2]

    IQR = Q3-Q1
    lower = Q1-(1.5*IQR)
    upper = Q3+(1.5*IQR)
    outlier = []
    for i in data:
        if i<lower or i>upper:
            outlier.append(i)

    return outlier

print(detecting_outliers(List1))