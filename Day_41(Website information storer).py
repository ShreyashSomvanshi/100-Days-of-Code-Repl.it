'''
Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
Finally, output the whole dictionary (keys and values).
'''

website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
