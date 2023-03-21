from getpass import getpass as input


#Summary text function
def winner1():
  print("\033[1;37m\nPlayer 1:", player1, "\033[1;32m  /VS/ ", "\033[1;37m Player 2:", player2)
  print("\n", "🥁"*12, "\n\nPlayer 1 is a winner! 🥳🥳🥳 ")

def winner2():
  print("\033[1;37m\nPlayer 1:", player1, "\033[1;32m  /VS/ ", "\033[1;37m Player 2:", player2)
  print("\n", "🥁"*12, "\n\nPlayer 2 is a winner! 🥳🥳🥳 ")

def tie():
  print("\033[1;37m\nPlayer 1:", player1, "\033[1;32m  /VS/ ", "\033[1;37m Player 2:", player2)
  print("\n", "🥁"*12, "\n\nThe game ended in a tie. Try again guys!")

def invalidMove():
    print("\n", "🥁"*12, "\n\nSomeone made invalid move. 🧐 Try again guys! ")



  
  
#Selecting options - R P or S


print("*"*7, " SPECTACULAR GAME -", "🗿 📃 ✂️ ", "*"*7, "\n")


player1_score = 0
player2_score = 0


while True:

  player1 = input("\nPlayer 1: \nPlease select one of the following: R or P or S\n\n")
  
  player2 = input("\nPlayer 2: \nPlease select one of the following: R or P or S\n\n")
  
  print("\n", "*"*7, "Battle time", "*"*7)

  
  

  #Battle time:
    
  #Player 1 is winning
  if (player1 == "r" or player1 == "R") and (player2 == "s" or player2 == "S"):
    winner1()
    player1_score += 1
  
  elif (player1 == "p" or player1 == "P") and (player2 == "r" or player2 == "R"):
    winner1
    player1_score += 1
  
  elif (player1 == "s" or player1 == "S") and (player2 == "p" or player2 == "P"):
    winner1()
    player1_score += 1
  
    
  #Player 2 is winning
  elif (player2 == "r" or player2 == "R") and (player1 == "s" or player1 == "S"):
    winner2()
    player2_score += 1
  
  elif (player2 == "p" or player2 == "P") and (player1 == "r" or player1 == "R"):
    winner2()
    player2_score += 1
  
  elif (player2 == "s" or player2 == "S") and (player1 == "p" or player1 == "P"):
    winner2()
    player2_score += 1
  
  
  #The gaime is a tie. Try again!
  elif (player2 == "r" or player2 == "R") and (player1 == "r" or player1 == "R"):
    tie()
  
  elif (player2 == "p" or player2 == "P") and (player1 == "p" or player1 == "P"):
    tie()
  
  elif (player2 == "s" or player2 == "S") and (player1 == "s" or player1 == "S"):
    tie()

  else:
    invalidMove()
    continue

  if player1_score == 3 or player2_score == 3:
    print("\n\nPlayer 1 has", player1_score, "wins. Player 2 has:", player2_score, "wins.")
    print("\nThanks for playing")
    exit()
  
    


