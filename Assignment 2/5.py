import math

def unit_price(diameter, price):
    radius = diameter / 2
    area_m2 = math.pi * (radius ** 2) / 10000  # cm² to m²
    return price / area_m2

def compare_pizzas():
    print("Enter details for Pizza 1:")
    d1 = float(input("Diameter (cm) of the first pizza: "))
    p1 = float(input("Price (USD) of the first pizza: "))
    
    print("Enter details for Pizza 2:")
    d2 = float(input("Diameter (cm) of the second pizza: "))
    p2 = float(input("Price (USD) of the second pizza: "))
    up1 = unit_price(d1, p1)
    up2 = unit_price(d2, p2)
    
    print(f"Pizza 1 unit price: ${up1:.2f}/m²")
    print(f"Pizza 2 unit price: ${up2:.2f}/m²")
    
    if up1 < up2:
        print("Pizza 1 offers better value for money.")
    elif up2 < up1:
        print("Pizza 2 offers better value for money.")
    else:
        print("Both pizzas offer the same value.")
compare_pizzas()