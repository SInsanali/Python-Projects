#Welcome message
print("Welcome to the Love Score Calculator!")

#Get user inputs
name1 = input("What is your first and last name?\n")
name2 = input("\nWhat is their first and last name?\n")

print("The Love Calculator is calculating your score...")

#combine names together and make lowercase
combined_names = (name1 + name2).lower()

#count letters in the combined names
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

#sum the amount in "true" and "love"
true_total = int(t + r + u + e)
love_total = int(l + o + v +e)

#create love score
love_score = int(f"{true_total}{love_total}")

#create messages for score ranges
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
