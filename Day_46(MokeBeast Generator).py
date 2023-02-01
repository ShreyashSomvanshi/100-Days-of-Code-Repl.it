'''
Program a full on Mokébeast Mokédex. Yep, think we're getting away with it so far...

Don't forget, you can reuse your code from Day 42 here.

Your Mokédex should:

Store multiple Mokébeasts using a loop.
Get user input of the beasts' details.
Add the details to a 2D dictionary.
Repeat until the user wants to stop.
Output the full Mokédex using a prettyPrint() function.

'''

import os, time

mokedex = {}

def prettyPrint():
  print(f"Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True:
  print("Add your Beast!")
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[name] = { "type": type, "hp": hp, "mp": mp}
  print("----------")
  print()
  prettyPrint()
