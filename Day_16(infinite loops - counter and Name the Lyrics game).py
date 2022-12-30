############ Counter ##############
counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    print("Exitting, your current total is", counter)
    break
print("Bye!")


############ Name the Lyrics Game ##############

print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
    break
  else:
    print("Nope! Try again!")
    counter +=1
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")

