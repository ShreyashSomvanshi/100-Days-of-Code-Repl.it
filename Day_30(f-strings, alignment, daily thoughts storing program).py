#############################################################
''''
Print text alignment
left = <, right = >, center = ^
'''
for i in range(1, 5):
  print(f"Day {i} of 30")
  
for i in range(1, 5):
  print(f"Day {i: <10} of 30")

for i in range(1, 5):
  print(f"Day {i: >10} of 30")

for i in range(1, 5):
  print(f"Day {i: ^10} of 30")

#############################################################

'''
Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.
For each day, prompt the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.
'''
print("30 Days Down - What did you think?")
print()
for i in range(1, 10):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()
