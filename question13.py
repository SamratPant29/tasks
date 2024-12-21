salary_data = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the number of years of service: "))
if years_of_service > 5:
    bonus = salary_data * 0.05
else:
    bonus = 0

print(f"The net bonus amount is: Rs {bonus:.0f}")