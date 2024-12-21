days = int(input("Enter the number of days the book is kept: "))


if days <= 5:
    charge = days * 2
elif 6 <= days <= 10:
    charge = (5 * 2) + ((days - 5) * 3)
elif 11 <= days <= 15:
    charge = (5 * 2) + (5 * 3) + ((days - 10) * 4)
else:  # days > 15
    charge = (5 * 2) + (5 * 3) + (5 * 4) + ((days - 15) * 5)

print(f"The total library charge is: Rs {charge}")