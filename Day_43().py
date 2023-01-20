'''
Anyway, your challenge is to enable "gambling for the elderly" (aka Bingo), and you'll achieve it like this:

Randomly generate a series of number between 0 and 90.
Allocate each number to a place in a 2D list.
The numbers should be in numerical order, left to right.
Numbers should not be repeated.
The center square should not contain a number. It should contain the word 'BINGO!'.
When the program is run, the bingo card should be displayed on screen.
'''


import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()
