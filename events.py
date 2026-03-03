import random

def travel_event(player):
    Atmodes = ["You fly past a dying star...", "You pass by an abandoned satellite", "
    
    if random.randint(0, 100) < 20: 
        typewriter("!!! ALERT: UNKNOWN VESSEL SPOTTED !!! Space Pirates have intercepted your ship! They demand a 20 Credit toll.", 0.04)
        playerChoice = textCleanUp(input("\nDo you (F)ight, (B)ribe, or (R)un? Print player(P)"))
    
        if playerChoice == "F":
          
            if random.randint(0, 100) < 30:
                creditLoss = random.randint(20, 35)
                typewriter(f"You attempt to defeat the pirates, but unfortunately are beaten down. You lose {creditLoss} credits", 0.04)
                player["credits"] -= creditLoss
            
            else:
                typewriter("You successfully fend off the Pirates! You continue on your way.", 0.04)


        
        elif playerChoice == "B":
            
            while True:
                creditBribe = input("How many credits do you attempt to bribe the pirates with?")
                
                if creditBribe.isdigit():
                    creditBribeInt = int(creditBribe)
                    
                    if 0 <= creditBribeInt <= player["credits"]:
                        
                        if random.randint(0, 20) < creditBribeInt:
                            typewriter(f"The pirates accept your bribe and fly away. You lose {creditBribeInt} credits.", 0.04)
                            player["credits"] -= creditBribeInt
                        
                        else: 
                            typewriter("The pirates don't accept your bribe and take 20 credits", 0.04)
                            player["credits"] -= 20
                        
                        break
                        
                    elif creditBribeInt > player["credits"]:
                        print("You don't have that much money!")
                    
                    else:
                        print("You need to put a positive number.")
                
                else:
                    print("It needs to be a number!")

       
        elif playerChoice == "R":
          
            if random.randint(0, player["fuel"]) >= 10:
                fuelLoss = random.randint(3, 10)
                typewriter(f"Rolling engines... Success! You boosted past them, but used {fuelLoss} extra Fuel.", 0.04)
                player["fuel"] -= fuelLoss
              
            else:
                fuelLoss = random.randint(2, 7)
                creditLoss = random.randint(22, 30)
                typewriter(f"Rolling engines... Failure. You attempt to outrun the pirates but they catch up. You waste {fuelLoss} fuel and lose {creditLoss} credits.", 0.04)
                player["fuel"] -= fuelLoss 
                player["credits"] -= creditLoss
              
