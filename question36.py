print("Welcome to the Space Mission!")

choice1 = input("Do you want to go 'to the moon' or 'to Mars'? ").lower()

if choice1 == "to mars":
    print("Game Over")
elif choice1 == "to the moon":
    choice2 = input("Do you want to \n'land on the surface' \n'stay in orbit'? \n").lower()
    if choice2 == "land on the surface":
        print("Game Over")
    elif choice2 == "stay in orbit":
        choice3 = input("Choose between \n 'alien' \n 'asteroid' \n 'satellite':\n ").lower()
        if choice3 == "alien" or choice3 == "asteroid":
            print("Game Over")
        elif choice3 == "satellite":
            print("You Win")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")