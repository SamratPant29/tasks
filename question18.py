city_data = input("Enter the name of a city: ").lower()
monuments_data = {
    "delhi": "Red Fort",
    "agra": "Taj Mahal",
    "jaipur": "Jal Mahal"
}
if city_data in monuments_data:
    print(f"The monument in {city_data.capitalize()} is {monuments_data[city_data]}.")
else:
    print("Sorry, no information available for that city.")