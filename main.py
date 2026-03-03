 import time
import sys

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
