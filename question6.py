a=int(input("enter marks of 1st subject: "))
b=int(input("enter marks of 2nd subject: "))
c=int(input("enter marks of 3rd subject: "))
d=int(input("enter marks of 4th subject: "))
total_marks= a+b+c+d
percentage=(total_marks/400)*100
if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First Division"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print("\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")