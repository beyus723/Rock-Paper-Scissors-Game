from getpass import getpass as input

#Selecting options - R P or S

print("*"*7, "🗿 📃 ✂️", " GAME", "*"*7, "\n")

player1 = input("Player 1: Select: R or P or S\n")
player2 = input("Player 2: Select: R or P or S\n")

print("\n", "*"*7, "Battle time 🥁🥁🥁", "*"*7)

#Summary text function
def winner1():
  print("\033[1;37m\nPlayer 1:", player1, "\033[1;32m  /VS/ ", "\033[1;37m Player 2:", player2)
  print("\nPlayer 1 is a winner! 🥳🥳🥳 ")
def winner2():
  print("\033[1;37m\nPlayer 1:", player1, "\033[1;32m  /VS/ ", "\033[1;37m Player 2:", player2)
  print("\nPlayer 2 is a winner! 🥳🥳🥳 ")
def tie():
  print("\033[1;37m\nPlayer 1:", player1, "\033[1;32m  /VS/ ", "\033[1;37m Player 2:", player2)
  print("The game ended in a tie. Try again guys!")
def invalidMove():
    print("\nSomeone made invalid move. 🧐 Try again guys! ")

  
  
#Battle time:
  
#Player 1 is winning
if (player1 == "r" or player1 == "R") and (player2 == "s" or player2 == "S"):
  winner1()
elif (player1 == "p" or player1 == "P") and (player2 == "r" or player2 == "R"):
  winner1()
elif (player1 == "s" or player1 == "S") and (player2 == "p" or player2 == "P"):
  winner1()

  
#Player 2 is winning
elif (player2 == "r" or player2 == "R") and (player1 == "s" or player1 == "S"):
  winner2()
elif (player2 == "p" or player2 == "P") and (player1 == "r" or player1 == "R"):
  winner2()
elif (player2 == "s" or player2 == "S") and (player1 == "p" or player1 == "P"):
  winner2()


#The gaime is a tie. Try again!
elif (player2 == "r" or player2 == "R") and (player1 == "r" or player1 == "R"):
  tie()
elif (player2 == "p" or player2 == "P") and (player1 == "p" or player1 == "P"):
  tie()
elif (player2 == "s" or player2 == "S") and (player1 == "s" or player1 == "S"):
  tie()

else:
  invalidMove()
  
    


