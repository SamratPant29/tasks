weather = input("What is the weather like today? (sunny/rainy): ").lower()

if weather == "sunny":
    print("Its sunny so what about you go for a hike or having a picnic?")
elif weather == "rainy":
    has_umbrella = input("Do you have a raincoat or umbrella? (yes/no): ").lower()
    if has_umbrella == "yes":
        print("You can visit a nearby mall or museum. Enjoy your lovely day")
    else:
        print("It's best to stay home and watch movies.")
else:
    print("No recommendation for this weather")