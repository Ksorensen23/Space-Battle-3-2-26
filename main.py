import time
import sys
import random
import json

#Start of filechecker

filePath = "player_save.json";

try:
    with open(filePath, "r") as file:
        data = json.load(file);
    print("json file found and successfully loaded.");

    player = {
    "name": "Ace",
    "credits": 100,
    "location": "Earth",
    "fuel": 50,
    "max_weight": 100,
    "inventory": {"Tacos": 2, "Iron": 0, "Fuel": 5},
    "alive": True
    }

except FileNotFoundError:
    print("No file named", filePath, "was found.");

except json.JSONDecodeError:
    print("Error, failed to decode json from the file.");


#>End of filechecker=====================


Max_Weight = 50

CurrentWEIGHT = 0
IronWEIGHT = 10
FuelWEIGHT = 5
TacosWEIGHT = 1

alive == True
  while True:     
    def typewriter(str, time):
      for char in str
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(time)

    def textCleanUp(input):
      if input.isdigit():
        retVal = "error no answer selected"
      else:
        retVal = input.upper()
      return retVal
#>Asher's code===============================================
import json;
gameRun = True;

player = {
    "name": "Ace",
    "credits": 100,
    "location": "Earth",
    "fuel": 50,
    "max_weight": 100,
    "inventory": {"Tacos": 2, "Iron": 0, "Fuel": 5},
    "alive": True
}

#>=========================

def save_game():
    print("\nSaving your progress to the star-map...\n\n...");
        
    data = str(player);                                                                     #Turns the "credits" value in player into a string to be written to the text file

    with open("leaderboard.txt", "w") as file:                                              #Writes data to a .txt file for the player to look at
        file.write(data);
    
    with open("player_save.json", "w") as file:                                             #Writes data to a .json file that the game looks for on start
        file.write(json.dumps(data, indent=4));

    print("\nProgress saved!  Current top score:", player["name"], player["credits"]);
    print("\nYour stats can be found in the 'leaderboard.txt' file\n");

#>=========================
# Keagan's code

 # Add wherever you would buy items to check if your weight is too high
def check_cargo(__name__):
    global Max_Weight
    CargoCheck = Iron + Tacos + Fuel
    
    if CargoCheck >= Max_Weight:
        print("Cannot buy, over weight capacity!")
        print("Go to a shipyard to increase.")
    if CargoCheck < Max_Weight:
        print("continuing...")
        
def Shipyard():
    global Max_Weight
    global credits
    print("===================================================")
    print("| Welcome to the shipyard!                        |")
    print("|                                                 |")
    print("| Upgrade Cost: 200 Credits                       |")
    print("|  [Increases Max Weight by 50]                   |")
    print("|                                                 |")
    print("| Current Weight: " + str(Max_Weight) + "                              |")
    print("| Your Balance: " + str(credits) + "                               |")
    print("|                                                 |")
    input1 = input("| Would you like to upgrade you're ship (Y/N)?    |\n")
    
    if input1 == "Y":
        if credits >= 200:
            Max_Weight = Max_Weight + 50
            credits = credits - 200
            print("Upgrade Successful! Max Weight is now: " + str(Max_Weight))
            print("200 Credits deducted! Total Credits are now: " + str(credits))
            StatsBoard()
        else:
             print("Error, Not enough Money!")
             print("Now Exiting...")
             StatsBoard()
    if input1 == "N":
        print("Exiting...")
        StatsBoard()


def StatsBoard():
    array1 = []
    PlayerLife = "Alive"
    name = input("What is you're name?")
    credits = 100
    location = "temp"
    fuel = 50
    
    
    print("*******************************************************")
    print("* Player Statistics.                                  *")
    print("*                                                     *")
    print("*     Name:" + " " +  name + "                                         *")
    print("*     Credits:" + " " + str(credits) + "                                    *")
    print("*     Locations:" + " " + location + "                                 *")
    print("*     Fuel(gal):" + " " + str(fuel) + "                                   *")
    print("*     Max Weight(lb):" + " " + str(Max_Weight) + "                              *")
    print("*     Inventory:" + " " + str(array1) + "            *")
    print("*     Alive:" + " " + PlayerLife + "                                    *")
    print("*                                                     *")
    print("*******************************************************")
  #=================== 
  # Liam's code
def travel_event(player): # random event function
    Atmodes = ["You fly past a dying star...", "You pass by an abandoned satellite", "A comet goes by as you travel", "you pass through a solar system with two stars orbiting each other", "Another trader ship passes by, sharing their greetings", "A space whale floats close and looks at you curiously before floating away", "you witness a black hole feeding on a red giant as you travel", "you exit warp travel to refill your water on an ocean planet before continuing to your destination", "You narrowly miss a star eater's tail when you pass close by", "A ship called 'The Hamilton' offers to update your ships firmware before continuing on"] # the flavour text for traveling
    typewriter(f"Atmodes[random.randint(0, 9)]", 0.04)
    if random.randint(0, 100) < 20: # 20% chance of happening
        typewriter("!!! ALERT: UNKNOWN VESSEL SPOTTED !!! Space Pirates have intercepted your ship! They demand a 20 Credit toll.", 0.04)
        playerChoice = textCleanUp(input("\nDo you (F)ight, (B)ribe, or (R)un? Print player(P)")) # input for how they should act against the pirates
        if playerChoice == "F": # they choose to fight
            if random.randint(0, 100) < 30: # 30% chance of losing
                creditLoss = random.randint(20, 35) # how many credits they should lose
                typewriter(f"You attempt to defeat the pirates, but unfortunately are beaten down. You lose {creditLoss} credits", 0.04)
                player["credits"] -= creditLoss # removes the lost credits from player inventory
            else: # 70% chance of winning
                typewriter("You successfully fend off the Pirates! You continue on your way.", 0.04)
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
        elif playerChoice == "R": # they choose to run
            if random.randint(0, player["fuel"]) >= 10: # the higher their fuel, the greater change of succeeding
                fuelLoss = random.randint(3, 10) # they lose this much fuel for running
                typewriter(f"Rolling engines... Success! You boosted past them, but used {fuelLoss} extra Fuel.", 0.04)
                player["fuel"] -= fuelLoss # deduct the fuel from inventory
            else: # they lose the check for running
                fuelLoss = random.randint(2, 6) # how much fuel they waste
                creditLoss = random.randint(22, 30) # how much money they lose
                typewriter(f"Rolling engines... Failure. You attempt to outrun the pirates but they catch up. You waste {fuelLoss} fuel and lose {creditLoss} credits.", 0.04)
                player["fuel"] -= fuelLoss #deduct lost fuel
                player["credits"] -= creditLoss #deduct lost credits
              



'''
while(gameRun == True):
    playerChoice = textCleanUp(input("\nDo you want to (T)rade, (F)ly, or (Q)uit? "));

    if(playerChoice == "Q"):
        playerChoice = textCleanUp(input("\nWould you like to save your game? (Y/N) "));       <==== This probably needs to be adjusted ?

        if(playerChoice == "Y"):
            save_game();

        elif(playerChoice == "N"):
            print("\nClosing game...");
            gameRun = False;

'''
