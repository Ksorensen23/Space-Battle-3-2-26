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

while(gameRun == True):
    playerChoice = input("\nDo you want to (T)rade, (F)ly, or (Q)uit? ");

    if(playerChoice.upper() == "Q"):
        playerChoice = input("\nWould you like to save your game? (Y/N) ");

        if(playerChoice.upper() == "Y"):
            save_game();

        elif(playerChoice.upper() == "N"):
            print("\nClosing game...");
            gameRun = False;

        




'''
On game start: look for json file to load player stats.
If it does not find the correct filename, define player manually.
On game exit, ask the player if they want to save their game.
If yes, write to the json file.
'''
