'''
Some trainers have no fear. To them, this is just one more challenge".

Create a dictionary to store the details of your, ahem, MokéBeast.
Ask the user to input the following details: name, type (earth, fire, air, water or spirit), special move, starting HP and starting MP.
For now we're just taking in one set of values for one beast.
Output the beast's details.
Check the beast's type and change the color of the text accordingly. Fire is red, water is blue, air is white. You decide on the others.

'''

mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokéBeast")
print()

for name, value in mokedex.items():
  mokedex[name] = input(f"{name}:\t").strip().title()

if mokedex["Type"]=="Earth":
  print("\033[32m", end="")
elif mokedex["Type"]=="Air":
  print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
  print("\033[31m", end="")
elif mokedex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in mokedex.items():
  print(f"{name:<15}: {value}")

