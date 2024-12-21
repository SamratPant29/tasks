years_of_service_data = int(input("Enter the number of years of service: "))
salary_data = float(input("Enter the employee's salary: "))

if years_of_service_data > 10:
    bonus = salary_data * 0.10
elif 6 <= years_of_service_data <= 10:
    bonus = salary * 0.08
else:
    bonus = salary_data * 0.05

# Display the bonus amount
print(f"The bonus amount is: Rs {bonus:.2f}")