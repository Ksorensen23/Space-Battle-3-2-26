import random

def travel_event(player):
  
  if random.randint(0, 100) < 20:
    typewriter("!!! ALERT: UNKNOWN VESSEL SPOTTED !!! Space Pirates have intercepted your ship! They demand a 20 Credit toll.", 20)
    playerChoice = input("Do you (F)ight, (B)ribe, or (R)un?")
    
    if playerChoice == "F":
      
      if random.randint(0, 100) < 30:
        typewriter("You successfully fend off the Pirates! You continue on your way.", 20)
        
      else:
        %loss = random.randint(20, 35)
        typewriter("You attempt to defeat the pirates, but unfortunately are beaten down. You lose" + %loss + "credits", 20)
        player["credits"] -= %loss

    elif playerChoice == "B":
      print("wow")
    elif playerChoice == "R":
        if random.randint(0, player["fuel"]) >= 10:
          %loss = random.randint(2, (player["fuel"]/2)
          typewriter("Rolling engines... Success! You boosted past them, but used" + %loss + "extra Fuel.", 20)
          
          
        
