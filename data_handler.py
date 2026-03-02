player = {
    "name": "Ace",
    "credits": 100,
    "location": "Earth",
    "fuel": 50,
    "max_weight": 100,
    "inventory": {"Tacos": 2, "Iron": 0, "Fuel": 5},
    "alive": True
}


playerChoice = input("Do you want to (T)rade, (F)ly, or (Q)uit?")

if(playerChoice.upper() == "Q"):

    print("\nSaving your progress to the star-map...\n");
