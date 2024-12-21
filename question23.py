age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
days_worked = int(input("Enter the number of days worked: "))

if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850
else:
    print("Invalid age or gender input")

if wage_per_day > 0:
    total_wages = wage_per_day * days_worked
    print(f"Your total wages are: {total_wages}")
else:
    print("Your total wage is 0")