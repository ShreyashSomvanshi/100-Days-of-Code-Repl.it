print("Exam Grade Calculator")
print()
name_of_exam = input("Name of exam: ")
print()
total_score = int(input("Max. Possible Score:"))
your_score = int(input("Your score: "))
print()



number_score = float(your_score / total_score)
final_number = round(number_score, 2)
final_perc = round(float(your_score / total_score)*100, 2)

print("You got",final_perc,"%")

if final_number >= .90:
  print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your letter grade is an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your letter score is a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your letter grade is a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your letter grade is a D.")
elif final_number <= .49:
  print("Your letter grade is a U.")
else: 
  print("Try again!")
