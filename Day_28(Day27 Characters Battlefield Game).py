'''
Use Day 27's character generator for this project...to build an automated game battle system!

Add return functions to your character's health and strength statuses from Day 27's project.
Generate two different characters and store their data (health and strength stats, character type, name, etc.).
Use a while True loop to simulate those two characters battling.
Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
The winner of that round (the one who rolled the higher number) will give damage to the other character by doing the following:
Find the difference between the strength of both opponents and add one.
Take that amount away from the loser's health.
At the end of each round, check the stats of each character to ensure neither of them have died yet.
When one character dies (they run out of health), declare a winner of the battle!
To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the screen clears between battles.
'''

import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat


print("⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()

c2Name = input("Name your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(c1Strength - c2Strength) + 1

  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first blow")
    else:
      print(c1Name, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(c1Name)
  print("HEALTH:", c1Health)
  print()
  print(c2Name)
  print("HEALTH:", c2Health)
  print()

  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    

time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
