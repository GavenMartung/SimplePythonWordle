import os
import random
from colorama import Fore,Back,init
init()

emptyWords = ["_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _"]
words = ["FEIGN","GHOST","MOURN","CHICK","STORE"]#Add Words Here
rchoice = random.randint(0,len(words)-1)
word = words[rchoice]
displayWord = word
word = list(word)
letterCount = 0
win = False

print("Welcome to Python Wordle\nYou have 6 tries to guess the 5 letter word.\nThe letters you guess that are in the right position appear green,\nthe ones you guess that are in the wrong position appear yellow. \nGood Luck.")

for i in range(0,6):
  print("\n +WORDLE\n")
  if letterCount == 5:
      win = True
      break
  print(letterCount)
  letterCount = 0
  for x in emptyWords:
    print(x)
  guess = input("Your Guess: ").upper()
  while len(guess) != 5:
    guess = input("Invalid Input,Your Guess must be under 5 Letters: ").upper()

  guess = list(guess)

  for r in range(0,len(guess)):

    if guess[r] == word[r]:
      letterCount+=1
      guess[r] = Fore.GREEN + guess[r] + Fore.RESET
    
    for l in range(0,len(word)):
      if guess[r] == word[l]:
        guess[r] = Fore.YELLOW + guess[r] + Fore.RESET
    
  
  emptyWords[i]= f"{guess[0]} {guess[1]} {guess[2]} {guess[3]} {guess[4]}"
  os.system('clear')


if win == True:
  print("Great Job! The Word was " + Fore.GREEN + displayWord + Fore.RESET)
else:
  print("Nice try...Better luck next time!")
