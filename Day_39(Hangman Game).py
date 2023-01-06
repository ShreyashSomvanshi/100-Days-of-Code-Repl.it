'''
Once the word has been picked, the following things need to happen:
Prompt the user to type in a letter.
Check if the letter is in the word.
If it does, output the word with all blanks apart from the letter(s) they've already guessed.
Keep a running list of the letters they've used.
Count how many times they've picked a letter that isn't in the word - more than 6 and they lose.
Output a 'win' message if they reveal all the letters.
🥳 Extra points for using ASCII art to draw the hangman as the player makes incorrect guesses.
'''

import random, os, time

listOfWords = ["apple", "orange", "grapes", "pear"]
letterPicked = []
lives = 6

word = random.choice(listOfWords)

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Choose a letter: ").lower()
  
  if letter in letterPicked:
    print("You've tried that before")
    continue
    
  letterPicked.append(letter)
  
  if letter in word:
    print("You found a letter")
  else:
    print("Nope, not in there")
    lives -= 1
  
  allLetters = True
  print()
  for i in word:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print(f"You won with {lives} left!")
    break

  if lives<=0:
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left")
