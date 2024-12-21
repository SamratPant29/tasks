income = float(input("Enter your annual income: "))

if income > 50000:
    credit_score = int(input("Enter your credit score: "))
    if credit_score > 700:
        print("Loan approved with standard interest rate.")
    elif 600 <= credit_score <= 700:
        print("Loan approved with a higher interest rate.")
    else:
        print("Loan rejected due to low credit score.")
else:
    print("Loan rejected due to insufficient income.")