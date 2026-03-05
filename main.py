import time
import sys
import random
import json

player = {                         
    "name": "Ace",
    "credits": 100,
    "location": "Earth",
    "fuel": 50,
    "max_weight": 100,
    "inventory": {"Tacos": 2, "Iron": 0, "Fuel": 5},
    "alive": True
}


default_player = {                         
    "name": "Ace",
    "credits": 100,
    "location": "Earth",
    "fuel": 50,
    "max_weight": 100,
    "inventory": {"Tacos": 2, "Iron": 0, "Fuel": 5},
    "alive": True
    }

# ==================== File Save/Load ====================
def load_game():
    file_path = "player_save.json"
    print("Any other input will start a new game")
    temp = input("Press x to open your previous save: ")

    if temp.upper() == "X":
        with open(file_path, "r") as file:
            player_data = json.load(file)
            player.update(player_data)
        print(player)

def save_game(argument):
    file_path = "player_save.json"
    global player

    nameChange = input("what is your name? ");
    player["name"] = nameChange;

    temp = input("Press s to save your game, or d to wipe your save. ");

    if(argument == "save"):
        with open(file_path, "w") as file:
            file.write(json.dumps(player, indent=4));
    
        print("Game has been saved to:", file_path);

    elif(argument == "wipe"):
        player = default_player;
        print("save has been reverted to default");
# ==================== Utility Functions ====================
def typewriter(text, sec):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sec)
    print("")

def textCleanUp(inp):
    if inp.isdigit():
        return "ERROR: no answer selected"
    return inp.upper()

def check_carg(player):
    IronWEIGHT = 10   
    FuelWEIGHT = 5   
    TacosWEIGHT = 1   

    CargoCheck = (IronWEIGHT * player["inventory"]["Iron"]) + \
                 (TacosWEIGHT * player["inventory"]["Tacos"]) + \
                 (FuelWEIGHT * player["inventory"]["Fuel"])

    if CargoCheck >= player["max_weight"]:
        print("Cannot buy, over weight capacity! Go to a shipyard to increase.")
        return False
    return True

# ==================== Shipyard & Stats ====================
def Shipyard(player):
    print("===================================================")
    print("| Welcome to the shipyard!                        |")
    print("| Upgrade Cost: 200 Credits                       |")
    print("|  [Increases Max Weight by 50]                   |")
    print("| Current Weight:", player["max_weight"], "                              |")
    print("| Your Balance:", player["credits"], "                               |")
    input1 = input("| Would you like to upgrade your ship (Y/N)?     |\n")

    if input1.upper() == "Y":
        if player["credits"] >= 200:
            player["max_weight"] += 50
            player["credits"] -= 200
            print("Upgrade Successful! Max Weight is now:", player["max_weight"])
            print("200 Credits deducted! Total Credits:", player["credits"])
            StatsBoard(player)
        else:
            print("Error, Not enough Money! Now Exiting...")
            StatsBoard(player)
    elif input1.upper() == "N":
        print("Exiting...")
        StatsBoard(player)

def StatsBoard(player):
    print("*******************************************************")
    print("* Player Statistics.                                  *")
    print("*     Name:", player["name"], "                                   *")
    print("*     Credits:", player["credits"], "                                *")
    print("*     Location:", player["location"], "                              *")
    print("*     Fuel(gal):", player["fuel"], "                                 *")
    print("*     Max Weight(lb):", player["max_weight"], "                        *")
    print("*     Inventory:", player["inventory"], "                *")
    print("*     Alive:", player["alive"], "                                  *")
    print("*******************************************************")

# ==================== Travel Events ====================
def travel_event(player):
    Atmodes = [
        "You fly past a dying star...",
        "You pass by an abandoned satellite.",
        "A comet goes by as you travel.",
        "You pass through a solar system with two stars orbiting each other.",
        "Another trader ship passes by, sharing their greetings.",
        "A space whale floats close and looks at you curiously before floating away.",
        "You witness a black hole feeding on a red giant as you travel.",
        "You exit warp travel to refill water on an ocean planet before continuing.",
        "You narrowly miss a star eater's tail when you pass close by.",
        "A ship called 'The Hamilton' offers to update your ship's firmware."
    ]
    typewriter(Atmodes[random.randint(0, len(Atmodes)-1)], 0.04)
    
    if random.randint(0, 100) < 20:  # 20% chance
        typewriter("\n!!! ALERT: UNKNOWN VESSEL SPOTTED !!! Space Pirates demand a 20 Credit toll.", 0.04)
        while True:
            playerChoice = textCleanUp(input("\nDo you (F)ight, (B)ribe, or (R)un? "))
            if playerChoice == "F":
                if random.randint(0, 100) < 30:
                    creditLoss = random.randint(20, 35)
                    typewriter(f"You are defeated and lose {creditLoss} credits.", 0.04)
                    player["credits"] -= creditLoss
                else:
                    typewriter("You fend off the Pirates successfully!", 0.04)
                break
            elif playerChoice == "B":
                while True:
                    creditBribe = input("Enter bribe amount: ")
                    if creditBribe.isdigit():
                        creditBribeInt = int(creditBribe)
                        if 0 <= creditBribeInt <= player["credits"]:
                            if random.randint(0, 20) < creditBribeInt:
                                typewriter(f"The pirates accept your bribe. You lose {creditBribeInt} credits.", 0.04)
                                player["credits"] -= creditBribeInt
                            else:
                                typewriter("Bribe rejected. Pirates take 20 credits.", 0.04)
                                player["credits"] -= 20
                            break
                        else:
                            print("You don't have that much money!")
                    else:
                        print("It needs to be a number!")
                break
            elif playerChoice == "R":
                if player["fuel"] <= 10:
                    typewriter("Not enough fuel to escape!", 0.04)
                elif random.randint(0, player["fuel"]) > 10:
                    fuelLoss = random.randint(3, 10)
                    typewriter(f"Success! You escape but use {fuelLoss} extra fuel.", 0.04)
                    player["fuel"] -= fuelLoss
                else:
                    fuelLoss = min(player["fuel"], random.randint(2, 6))
                    creditLoss = min(player["credits"], random.randint(22, 30))
                    typewriter(f"Failure! You waste {fuelLoss} fuel and lose {creditLoss} credits.", 0.04)
                    player["fuel"] -= fuelLoss
                    player["credits"] -= creditLoss
                break
    print(f"\n[CURRENT LOCATION] {player["location"]}\n")

# ==================== Market System ====================
def market(player):
    # Set planet-specific prices randomly
    prices = {
        "Tacos": random.randint(5, 15),
        "Iron": random.randint(20, 50),
        "Fuel": random.randint(10, 25)
    }

    while True:
        print(f"\n=== Welcome to {player['location']} Market ===")
        print(f"Your Credits: {player['credits']}")
        print(f"Inventory: {player['inventory']}")
        print("Current Prices: ", prices)
        choice = textCleanUp(input("Do you want to (B)uy, (S)ell, or (E)xit? "))

        if choice == "E":
            print("Exiting Market...")
            break

        elif choice == "B":
            item = textCleanUp(input("Buy (T)acos, (I)ron, or (F)uel? "))
            if item == "T":
                item_name = "Tacos"
            elif item == "I":
                item_name = "Iron"
            elif item == "F":
                item_name = "Fuel"
            else:
                print("Invalid item!")
                continue

            amount = input(f"How many {item_name} would you like to buy? ")
            if not amount.isdigit():
                print("Invalid number!")
                continue
            amount = int(amount)
            total_cost = amount * prices[item_name]

            if total_cost > player["credits"]:
                print("Not enough credits!")
                continue

            # Check weight
            IronWEIGHT = 10   
            FuelWEIGHT = 5   
            TacosWEIGHT = 1   
            current_weight = (IronWEIGHT * player["inventory"]["Iron"] + 
                              FuelWEIGHT * player["inventory"]["Fuel"] +
                              TacosWEIGHT * player["inventory"]["Tacos"])
            added_weight = amount * (TacosWEIGHT if item_name=="Tacos" else IronWEIGHT if item_name=="Iron" else FuelWEIGHT)
            if current_weight + added_weight > player["max_weight"]:
                print("Cannot buy, exceeds cargo capacity!")
                continue

            player["inventory"][item_name] += amount
            player["credits"] -= total_cost
            print(f"Bought {amount} {item_name} for {total_cost} credits.")

        elif choice == "S":
            item = textCleanUp(input("Sell (T)acos, (I)ron, or (F)uel? "))
            if item == "T":
                item_name = "Tacos"
            elif item == "I":
                item_name = "Iron"
            elif item == "F":
                item_name = "Fuel"
            else:
                print("Invalid item!")
                continue

            amount = input(f"How many {item_name} would you like to sell? ")
            if not amount.isdigit():
                print("Invalid number!")
                continue
            amount = int(amount)

            if amount > player["inventory"][item_name]:
                print("You don't have that many!")
                continue

            total_gain = amount * prices[item_name]
            player["inventory"][item_name] -= amount
            player["credits"] += total_gain
            print(f"Sold {amount} {item_name} for {total_gain} credits.")

# ==================== Game Loop ====================
def GameLoop(player):
    while player["alive"]:
        playerChoice = textCleanUp(input("\nDo you want to (F)ly, (S)hipyard, (T)rade, or (Q)uit? "))

        if playerChoice == "Q":
            playerChoice = textCleanUp(input("\nWould you like to (S)ave your game? "))
            if playerChoice == "Y":
                save_game()
            typewriter("\nClosing game...", 0.04)
            break
        elif playerChoice == "S":
            Shipyard(player)
        elif playerChoice == "T":
            market(player)  # <-- Market is now fully accessible
        elif playerChoice == "F":
            playerChoice = textCleanUp(input("\nGo to (E)arth or (M)ars? "))
            if playerChoice == "E":
                player["location"] = "Earth"
            elif playerChoice == "M":
                player["location"] = "Mars"
            travel_event(player)

# ==================== Main ====================
while True:
    playPrompt = textCleanUp(input(f"Would you like to (P)lay as {player['name']}, (D)elete {player['name']}, or (Q)uit? \n"))

    if playPrompt == "P":
        GameLoop(player)
    elif playPrompt == "D":
        confirm = textCleanUp(input("Are you sure? Press (X) to delete, anything else to go back. "))
        if confirm == "X":
            save_game("wipe")  # optional: implement wipe logic here
    elif playPrompt == "Q":
        typewriter("Leaving Game............", 0.04)
        break
