# the Big Task: Manage Weight. Every item needs a weight (e.g., Iron=10, Tacos=1). Write a check_cargo(player) function that prevents 
# a player from buying more if they hit their max_weight.
# The Dashboard: Create a beautiful text-based UI that shows the player’s stats in a box made of * or = symbols.
# Upgrades: Create a "Shipyard" menu where players can pay 200 credits to increase their max_weight by 50.

Max_Weight = 50


CurrentWEIGHT = 0
IronWEIGHT = 10
FuelWEIGHT = 5
TacosWEIGHT = 1
credits = 300
Iron = 10
Tacos = 1
Fuel = 50

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
    Shipyard()




if __name__ == "__main__":
    Shipyard()
