correct_username = "samratpant29"
correct_password = "febraury17"

username_data = input("Enter your username: ")


if username_data == correct_username:
    password_data= input("Enter your password: ")
    if password_data == correct_password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")