weight = float(input("Enter the weight of the package in kg: "))
urgent = input("Is the delivery urgent? (yes/no): ").lower()
if weight < 5:
    delivery_cost = 5
elif 5 <= weight <= 20:
    delivery_cost = 10
else:
    delivery_cost = 20

if urgent == "yes":
    delivery_cost += 5

print(f"The total delivery cost is: Rs.{delivery_cost}")