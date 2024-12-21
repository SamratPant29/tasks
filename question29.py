age = int(input("Enter your age: "))
if age >= 18:
    has_degree = input("Do you have a degree? (yes/no): ").lower()
    if has_degree == "yes":
        work_experience = float(input("Enter your work experience in years: "))
        if work_experience > 3:
            print("Highly Eligible.")
        elif 1 <= work_experience <= 3:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("Not Eligible (Degree is required).")
else:
    print("Not Eligible (Age is below 18).")