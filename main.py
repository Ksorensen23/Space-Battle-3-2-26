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

BASE_PRICES = {
    "Earth": {
        "Fuel": 10,
        "Tacos": 5,
        "Iron": 20
    },
    "Mars": {
        "Fuel": 15,
        "Tacos": 12,
        "Iron": 5
    }
}
        
demand_modifier = {
    "Fuel": 1.0,
    "Tacos": 1.0,
    "Iron": 1.0
}
#Start of filechecker
'''
DEPRECIATED
filePath = "player_save.json";

try:
    with open(filePath, "r") as file:
        data = json.load(file);
    print("json file found and successfully loaded.");

except FileNotFoundError:
    print("No file named", filePath, "was found.");

except json.JSONDecodeError:
    print("Error, failed to decode json from the file.");
DEPRECIATED
'''
def load_game():
    file_path = "player_save.json";

    print("Any other input will start a new game");
    temp = input("Press x to open your previous save. ");    #< this will open from the player_save.json

    if(temp.upper() == "X"):

        with open(file_path, "r") as file:
            player = json.load(file);

        print(player);



def save_game():
    file_path = "player_save.json"
    data = player;

    nameChange = input("what is your name? ");
    player["name"] = nameChange;

    temp = input("Press s to save your game, or d to wipe your save. ");

    if(temp.upper() == "S"):
        with open(file_path, "w") as file:
            file.write(json.dumps(data, indent=4));
    
        print("Game has been saved to:", file_path);

    elif(temp.upper() == "D"):
        player = player;
        print("save has been reverted to default");
#>End of filechecker=====================

def typewriter(str, sec):
  for char in str
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(sec)

def textCleanUp(inp):
  if inp.isdigit():
    retVal = "error no answer selected"
  else:
    retVal = inp.upper()
  return retVal
#>Asher's code===============================================



#>=========================
'''
def save_game(player):
    print("\nSaving your progress to the star-map...\n\n...");
        
    data = str(player);                                                                     #Turns the "credits" value in player into a string to be written to the text file

    with open("leaderboard.txt", "w") as file:                                              #Writes data to a .txt file for the player to look at
        file.write(data);
    
    with open("player_save.json", "w") as file:                                             #Writes data to a .json file that the game looks for on start
        file.write(json.dumps(data, indent=4));

    print("\nProgress saved!  Current top score:", player["name"], player["credits"]);
    print("\nYour stats can be found in the 'leaderboard.txt' file\n");
'''
#>=========================
# Keagan's code

 # Add wherever you would buy items to check if your weight is too high
def check_carg(player):
    
    IronWEIGHT = 10   
    FuelWEIGHT = 5   
    TacosWEIGHT = 1   
    
    CargoCheck = (IronWEIGHT * player["inventory"]["Iron"]) + (TacosWEIGHT * player["inventory"]["Tacos"])  + (FuelWEIGHT * player["inventory"]["Fuel"])
    
    if CargoCheck >= player["max_weight"]:
        print("Cannot buy, over weight capacity!")
        print("Go to a shipyard to increase.")
    if CargoCheck < player["max_weight"]:
        print("continuing...")
        
def Shipyard(player):
    
    print("===================================================")
    print("| Welcome to the shipyard!                        |")
    print("|                                                 |")
    print("| Upgrade Cost: 200 Credits                       |")
    print("|  [Increases Max Weight by 50]                   |")
    print("|                                                 |")
    print("| Current Weight: " + str(player["max_weight"]) + "                              |")
    print("| Your Balance: " + str(player["credits"]) + "                               |")
    print("|                                                 |")
    input1 = input("| Would you like to upgrade you're ship (Y/N)?    |\n")

    if input1 == "Y":
        if player["credits"] >= 200:
            player["max_weight"] = player["max_weight"] + 50
            player["credits"] = player["credits"] - 200
            print("Upgrade Successful! Max Weight is now: " + str(player["max_weight"]))
            print("200 Credits deducted! Total Credits are now: " + str(player["credits"]))
            StatsBoard()
        else:
             print("Error, Not enough Money!")
             print("Now Exiting...")
             StatsBoard()
    if input1 == "N":
        print("Exiting...")
        StatsBoard()


def StatsBoard(player):
    print("*******************************************************")
    print("* Player Statistics.                                  *")
    print("*                                                     *")
    print("*     Name:" + " " +  player["name"] + "                                         *")
    print("*     Credits:" + " " + str(player["credits"]) + "                                    *")
    print("*     Locations:" + " " + player["location"] + "                                 *")
    print("*     Fuel(gal):" + " " + str(player["fuel"]) + "                                   *")
    print("*     Max Weight(lb):" + " " + str(player["max_weight"]) + "                              *")
    print("*     Inventory:" + " " + player["inventory"] + "            *")
    print("*     Alive:" + " " + player["alive"] + "                                    *")
    print("*                                                     *")
    print("*******************************************************")
  #=================== 

  #>Liam - The Encounter Specialist (Event Designer)=================================

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
            playerChoice = textCleanUp(input("\nDo you (F)ight, (B)ribe, or (R)un?")) # input for how they should act against the pirates
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
                
#>===============================================================================


def get_prices(planet):
    prices = {}
    for item, base_price in BASE_PRICES[planet].items():
        modified_price = base_price * demand_modifier[item]
        prices[item] = round(modified_price, 2)

    return prices


def increase_demand(item):
    if item in demand_modifier:
        demand_modifier[item] *= 1.05

def buy_item(player, item, price, quantity):
    
    total_cost = price * quantity
    
    if player["credits"] < total_cost:
        print(">>> Not enough credits for this purchase.")
        return False

    player["inventory"][item] += quantity
    
    player["credits"] -= total_cost
    
    for _ in range(quantity):
        increase_demand(item)

    print(f"Purchase Complete: Spent {total_cost} Credits.")
    return True

def sell_item(player, item, price, quantity=1):
    if item not in player["inventory"]:
        print(">>> Item does not exist.")
        return False

    if player["inventory"][item] < quantity:
        print("You do not have enough of that item to sell.")
        return False

    total_value = price * quantity

    player["inventory"][item] -= quantity

    player["credits"] += total_value

    print(f" Sold {quantity} {item} for {total_value} Credits.")

    return True

def planetShop(player, planet):
    get_prices(planet)
    
#>====================================================================

def GameLoop(player): 
    while(player["alive"] == True):
        playerChoice = textCleanUp(input("\nDo you want to (T)rade, (F)ly, or (Q)uit? "));

        if(playerChoice == "Q"):
            playerChoice = textCleanUp(input("\nWould you like to (S)ave your game? "));
    
            if(playerChoice == "Y"):
                save_game();
            typewriter("\nClosing game...", 0.04);
            break;
                
        if(playerChoice == "T"):
           planetShop(player["location"])

        if playerChoice == "F":
            playerChoice = textCleanUp(input("\nDo you want go to the (S)hipyard, (E)arth, or (M)ars"));




while True:
    playPrompt = textCleanUp(input(f"Would you like to (P)lay as {player["name"]}, (D)elete {player["name"]}, or (Q)uit?"))
    
    if playPrompt == "P":
        GameLoop()

    if playPrompt == "D":
        confirm = textCleanUp(input("Are you Sure? Press (X) to continue with deletion. Press anything else to go back."))
        if confirm == "X":
            save_game(wipe)
    if playPrompt == "Q":
        typewriter("Leaving Game............", 0.04)
        break
