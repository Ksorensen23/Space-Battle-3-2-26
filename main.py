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

def travel_event(player):

    events = [
        "You fly past a dying star...",
        "You pass an abandoned satellite.",
        "A comet streaks past your ship.",
        "You see a binary star system.",
        "Another trader greets you in passing."
    ]

    typewriter(random.choice(events), 0.03)

    if random.randint(0,100) < 20:

        typewriter("!!! PIRATES ATTACK !!! They demand 20 credits.",0.03)

        while True:

            choice = textCleanUp(input("(F)ight (B)ribe (R)un: "))

            if choice == "F":

                if random.randint(0,100) < 30:
                    loss = random.randint(20,35)
                    player["credits"] -= loss
                    print("You lost the fight. Lost",loss,"credits")
                else:
                    print("You defeated the pirates!")

                break

            elif choice == "B":

                amount = input("Bribe amount: ")

                if amount.isdigit():

                    amount = int(amount)

                    if amount <= player["credits"]:

                        if random.randint(0,20) < amount:
                            print("Pirates accept bribe.")
                            player["credits"] -= amount
                        else:
                            print("Pirates reject bribe and take 20 credits.")
                            player["credits"] -= 20

                        break

            elif choice == "R":

                if player["fuel"] <= 10:
                    print("Not enough fuel to run!")
                    break

                if random.randint(0,player["fuel"]) > 10:

                    fuelLoss = random.randint(3,10)
                    player["fuel"] -= fuelLoss

                    print("You escaped! Lost",fuelLoss,"fuel")

                else:

                    fuelLoss = random.randint(2,6)
                    creditLoss = random.randint(22,30)

                    fuelLoss = min(fuelLoss, player["fuel"])
                    creditLoss = min(creditLoss, player["credits"])

                    player["fuel"] -= fuelLoss
                    player["credits"] -= creditLoss

                    print("Failed escape! Lost",fuelLoss,"fuel and",creditLoss,"credits")

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
