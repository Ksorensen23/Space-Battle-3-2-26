import time
import sys
import random
import json
import os

filePath = "player_save.json"

# Default player
player = {
    "name": "Ace",
    "credits": 100,
    "location": "Earth",
    "fuel": 50,
    "max_weight": 100,
    "inventory": {"Tacos": 2, "Iron": 0, "Fuel": 5},
    "alive": True
}

# Load save if it exists
try:
    with open(filePath, "r") as file:
        player = json.load(file)
    print("Save file loaded.")
except FileNotFoundError:
    print("No save file found. Starting new game.")
except json.JSONDecodeError:
    print("Save file corrupted. Starting fresh.")

# =========================

def typewriter(text, sec):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sec)
    print()

def textCleanUp(inp):
    if inp.isdigit():
        return "error"
    return inp.upper()

# =========================

def save_game():
    print("\nSaving your progress...\n")

    with open("leaderboard.txt", "w") as file:
        file.write(str(player))

    with open("player_save.json", "w") as file:
        json.dump(player, file, indent=4)

    print("Game Saved!")

# =========================

def check_cargo(player):
    IronWEIGHT = 10
    FuelWEIGHT = 5
    TacosWEIGHT = 1

    CargoCheck = (
        IronWEIGHT * player["inventory"]["Iron"] +
        TacosWEIGHT * player["inventory"]["Tacos"] +
        FuelWEIGHT * player["inventory"]["Fuel"]
    )

    if CargoCheck >= player["max_weight"]:
        print("Cannot buy, over weight capacity!")
        return False

    return True

# =========================

def Shipyard():
    print("========== Shipyard ==========")
    print("Upgrade Cost: 200 Credits")
    print("Current Max Weight:", player["max_weight"])
    print("Your Credits:", player["credits"])

    choice = textCleanUp(input("Upgrade ship? (Y/N): "))

    if choice == "Y":
        if player["credits"] >= 200:
            player["max_weight"] += 50
            player["credits"] -= 200
            print("Upgrade successful!")
        else:
            print("Not enough credits.")

# =========================

def StatsBoard():
    print("\n===== PLAYER STATS =====")
    print("Name:", player["name"])
    print("Credits:", player["credits"])
    print("Location:", player["location"])
    print("Fuel:", player["fuel"])
    print("Max Weight:", player["max_weight"])
    print("Inventory:", player["inventory"])
    print("========================")

# =========================

def travel_event(player): # random event function
    Atmodes = ["You fly past a dying star...", "You pass by an abandoned satellite.", 
               "A comet goes by as you travel.", 
               "You pass through a solar system with two stars orbiting each other.", 
               "Another trader ship passes by, sharing their greetings.", 
               "A space whale floats close and looks at you curiously before floating away.", 
               "You witness a black hole feeding on a red giant as you travel.", 
               "You exit warp travel to refill your water on an ocean planet before continuing to your destination.", 
               "You narrowly miss a star eater's tail when you pass close by.", 
               "A ship called 'The Hamilton' offers to update your ships firmware before continuing on."] # the flavour text for traveling
    typewriter(Atmodes[random.randint(0, len(Atmodes)-1)], 0.04)
    if random.randint(0, 100) < 20: # 20% chance of happening
        typewriter("\n!!! ALERT: UNKNOWN VESSEL SPOTTED !!! Space Pirates have intercepted your ship! They demand a 20 Credit toll.", 0.04)
        while True:
            playerChoice = textCleanUp(input("\nDo you (F)ight, (B)ribe, or (R)un?)) # input for how they should act against the pirates
            if playerChoice == "F": # they choose to fight
                if random.randint(0, 100) < 30: # 30% chance of losing
                    creditLoss = random.randint(20, 35) # how many credits they should lose
                    typewriter(f"You attempt to defeat the pirates, but unfortunately are beaten down. You lose {creditLoss} credits", 0.04)
                    player["credits"] -= creditLoss # removes the lost credits from player inventory
                    break
                else: # 70% chance of winning
                    typewriter("You successfully fend off the Pirates! You continue on your way.", 0.04)
                    break
            elif playerChoice == "B": # they choose to bribe them
                while True: # runs the amount they wish to bribe with until they get a valid input
                    creditBribe = input("How many credits do you attempt to bribe the pirates with?") # they bribe
                    if creditBribe.isdigit(): # makes sure the bribe is a number
                        creditBribeInt = int(creditBribe) # turns it from str to int
                        if 0 <= creditBribeInt <= player["credits"]: # do they have enough money?
                            if random.randint(0, 20) < creditBribeInt: # this makes it so the higher the bribe, the chance of succeeding is higher
                                typewriter(f"The pirates accept your bribe and fly away. You lose {creditBribeInt} credits.", 0.04)
                                player["credits"] -= creditBribeInt # remove the bribe amount from inventory
                            else: #the check fails 
                                typewriter("The pirates don't accept your bribe and take 20 credits", 0.04)
                                player["credits"] -= 20 # deduct 20 credits for toll
                            break # stops the loop because they did everything right and the check was made. 
                                    # If we instead break after confirming the bribe is a valid answer, it would skip 
                                    # over the logic desiding if they convince the pirates and ho much money they lose
                        elif creditBribeInt > player["credits"]: # is the bribe invalid because they don't have enough money?
                            print("You don't have that much money!")
                        else: # number can only be non positive now
                            print("You need to put a positive number.")
                    else: # answer wasn't a number
                        print("It needs to be a number!")
                break
            elif playerChoice == "R": # they choose to run
                if player["fuel"] <= 10:
                    typewriter("You Don't have enough  fuel!")
                    
                elif random.randint(0, player["fuel"]) > 10: # the higher their fuel, the greater change of succeeding
                    fuelLoss = random.randint(3, 10) # they lose this much fuel for running
                    typewriter(f"Rolling engines... Success! You boosted past them, but used {fuelLoss} extra Fuel.", 0.04)
                    player["fuel"] -= fuelLoss # deduct the fuel from inventory
                    break
                else: # they lose the check for running
                    fuelLoss = random.randint(2, 6) # how much fuel they waste
                    if player["fuel"] < fuelLoss:
                        fuelLoss = player["fuel"]
                    creditLoss = random.randint(22, 30) # how much money they lose
                    if player["credits"] < fuelLoss:
                        creditLoss = player["credits"]
                    typewriter(f"Rolling engines... Failure. You attempt to outrun the pirates but they catch up. You waste {fuelLoss} fuel and lose {creditLoss} credits.", 0.04)
                    player["fuel"] -= fuelLoss #deduct lost fuel
                    player["credits"] -= creditLoss #deduct lost credits
                    break

# =========================
# Market system

BASE_PRICES = {

    "Earth": {
        "Fuel":10,
        "Tacos":5,
        "Iron":20
    },

    "Mars":{
        "Fuel":15,
        "Tacos":12,
        "Iron":5
    }

}

demand_modifier = {
    "Fuel":1.0,
    "Tacos":1.0,
    "Iron":1.0
}

def get_prices(planet):

    prices = {}

    print("\n===== MARKET PRICES =====")

    for item, base_price in BASE_PRICES[planet].items():

        price = base_price * demand_modifier[item]
        prices[item] = round(price, 2)

        print(item + ":", prices[item], "credits")

    print("=========================\n")

    return prices

def increase_demand(item):

    if item in demand_modifier:
        demand_modifier[item] *= 1.05

# =========================

def buy_item(player,item,price,quantity):

    if not check_cargo(player):
        return False

    total = price * quantity

    if player["credits"] < total:
        print("Not enough credits.")
        return False

    player["inventory"][item] += quantity
    player["credits"] -= total

    for _ in range(quantity):
        increase_demand(item)

    print("Purchased",quantity,item)

    return True

def sell_item(player,item,price,quantity):

    if player["inventory"][item] < quantity:
        print("Not enough items.")
        return False

    total = price * quantity

    player["inventory"][item] -= quantity
    player["credits"] += total

    print("Sold",quantity,item)

    return True

# =========================

def GameLoop():

    while player["alive"]:

        choice = textCleanUp(input("\n(T)rade (F)ly (S)tats (Q)uit: "))

        if choice == "T":
            prices = get_prices(player["location"])

            while True:

                trade = textCleanUp(input("(B)uy (S)ell (E)xit market: "))

                if trade == "B":

                    item = textCleanUp(input("Item to buy (Fuel/Tacos/Iron): "))

                    if item not in prices:
                        print("Item not sold here.")
                        continue

                    qty = input("Quantity: ")

                    if qty.isdigit():
                        qty = int(qty)
                        buy_item(player, item, prices[item], qty)

                elif trade == "S":

                    item = textCleanUp(input("Item to sell (Fuel/Tacos/Iron): "))

                    if item not in prices:
                        print("Item not traded here.")
                        continue

                    qty = input("Quantity: ")

                    if qty.isdigit():
                        qty = int(qty)
                        sell_item(player, item, prices[item], qty)

                elif trade == "E":
                    break

        elif choice == "F":

            travel_event(player)

        elif choice == "S":

            StatsBoard()

        elif choice == "Q":

            save = textCleanUp(input("Save game? (Y/N): "))

            if save == "Y":
                save_game()

            break

# =========================
# Main menu

while True:

    playPrompt = textCleanUp(input(f"\n(P)lay (D)elete Save (Q)uit: "))

    if playPrompt == "P":
        GameLoop()

    elif playPrompt == "D":

        confirm = textCleanUp(input("Press X to delete save: "))

        if confirm == "X":

            if os.path.exists(filePath):
                os.remove(filePath)
                print("Save deleted.")
            else:
                print("No save file found.")

    elif playPrompt == "Q":

        typewriter("Leaving Game...",0.03)
        break
