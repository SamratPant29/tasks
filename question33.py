print("Welcome to the Haunted House")

data_1= input("Do you want to go 'upstairs' or 'downstairs'? ").lower()

if data_1 == "downstairs":
    print("Game Over")
elif data_1 == "upstairs":
    choice1_data = input("Do you want to \n'enter the room'\n 'stay outside'\n? ").lower()
    if choice1_data == "enter the room":
        print("Game Over")
    elif choice1_data == "stay outside":
        choice2_data = input("Choose between \n'ghost'\n 'vampire'\n  'werewolf': \n").lower()
        if choice2_data == "ghost" or choice2_data == "vampire":
            print("Game Over")
        elif choice2_data == "werewolf":
            print("You Win")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")