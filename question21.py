total_days = int(input("Enter the total number of days:\n "))
absent_days = int(input("Enter the number of days you were absent:\n "))

attended_days = total_days - absent_days

attendance_percentage = (attended_days / total_days) * 100
print(f"Your attendance percentage is: {attendance_percentage:.1f}%")

if attendance_percentage >= 75:
    print("You are eligible to sit in the exam.")
else:
    print("You are not eligible to sit in the exam due to insufficient attendance.")