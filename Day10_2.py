# Data Aggregation - Sales Analysis
data = [
    {"CarModel": "BMW", "Price": 19440, "Quantity": 2},
    {"CarModel": "Audi", "Price": 80022, "Quantity": 5},
    {"CarModel": "RangeRovers", "Price": 15418350, "Quantity": 10},
    {"CarModel": "BMW", "Price": 1203320, "Quantity": 1},
    {"CarModel": "Audi", "Price": 802230, "Quantity": 2}
]
revenue = {}
for cars in data:
    CarModel = cars["CarModel"]
    total_sale = cars["Price"] * cars["Quantity"]
    
    if CarModel in revenue:
        revenue[CarModel] += total_sale
    else:
        revenue[CarModel] = total_sale
top_CarModel = max(revenue, key=revenue.get)
print(f"Total Revenue per CarModel: {revenue}")
print(f"Top CarModel: {top_CarModel}, with revenue of {revenue[top_CarModel]}")
