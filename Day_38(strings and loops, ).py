'''
Code the rainbow!

Ask the user to input any sentence (string).
Now we'll rainbow-ize (nope, me neither) it.
As soon as the string contains an 'r', every letter from that point on should be red.
When the computer encounters a 'b', 'g', 'p' or 'y', from there the output should be blue for 'b', green for 'g'...you get the idea.
Loop through the string and output it (so the color continues through the loop).
The output should change color every time it encounters a new r,g,b,p or y.
'''

def colorChange(color):
  if color=="r":
    print("\033[31m", end="")
  elif color==" ":
    print("\033[0m", end="")
  elif color=="b":
    print("\033[34m", end="")
  elif color=="y":
    print("\033[33m", end="")
  elif color == "g":
    print("\033[32m", end="")
  elif color == "p":
    print("\033[35m", end="")

sentence = input("What sentence do you want rainbow-izing?: ")
for letter in sentence:
  colorChange(letter.lower())
  print(letter, end="")
print()

