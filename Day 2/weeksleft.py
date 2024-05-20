#Ask the desired age
desired_age = int(input("Until what age do you want to live to?\n"))

#Convert desired age to weeks
desired_age_in_weeks = desired_age * 52

#Ask the current age
current_age = int(input("What is your age right now?\n"))

#Convert current age to weeks
current_age_in_weeks = current_age * 52

#Caluclate the weeks left
weeks_left = desired_age_in_weeks - current_age_in_weeks

#Deliver the news
print(f"\nYou have roughly {weeks_left} weeks of life left.")