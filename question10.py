marks_data = float(input("Enter your marks: "))

if marks_data < 25:
    grade = "D"
elif 25 <= marks_data <= 45:
    grade = "C"
elif 45 < marks_data <= 50:
    grade = "B"
elif 50 < marks_data<= 60:
    grade = "B+"
elif 60 < marks_data<= 80:
    grade = "A"
else:
    grade = "A+"


print(f"Your grade is: {grade}")