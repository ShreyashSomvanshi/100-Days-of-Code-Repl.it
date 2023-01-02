'''
Create a list that stores greetings in different languages. Start with the language you speak.
Then, go on the internet to find other greetings in other languages.
Import random library. Generate a random number between 0 and maximum number of items in your list.
At random, when the user clicks run, print one of the greetings.
Use an f-string.
'''

import random
greetings = ["Hello there!", "Konnichiwa", "Guten Tag!", "Bore Da!"]
index = random.randint(0,3)
print(greetings[index])


