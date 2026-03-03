 import time
import sys

Max_Weight = 50

CurrentWEIGHT = 0
IronWEIGHT = 10
FuelWEIGHT = 5
TacosWEIGHT = 1
credits = 300
Iron = 10
Tacos = 1
Fuel = 50

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





'''
while(gameRun == True):
    playerChoice = input("\nDo you want to (T)rade, (F)ly, or (Q)uit? ");

    if(playerChoice.upper() == "Q"):
        playerChoice = input("\nWould you like to save your game? (Y/N) ");       <==== This probably needs to be adjusted ?

        if(playerChoice.upper() == "Y"):
            save_game();

        elif(playerChoice.upper() == "N"):
            print("\nClosing game...");
            gameRun = False;

'''
