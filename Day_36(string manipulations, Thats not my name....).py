'''
Create a list of people's names. Ask for first and last name (surname) separately.
~Strip any extra spaces.
~Store names in a capitalized version.
~Create a new string using an fString that combines the tidied up version of the first name and tidied up version of the last name.
~Add those new versions to a list.
~Do not allow duplicates.
~Each time you add a new name, you should print out the full list.
'''

rolodex = []

def printList():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()
