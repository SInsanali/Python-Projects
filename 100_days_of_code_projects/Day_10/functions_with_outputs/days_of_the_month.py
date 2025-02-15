def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year"
      else:
        return "Not leap year"
    else:
      return "Leap year"
  else:
    return "Not leap year"
  

def days_in_month(the_year, the_month):
  #ordered Jan - Dec
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

  leap = is_leap(year)

  if leap == "Not leap year":
    return (month_days[the_month - 1])
  
  elif leap == "Leap year" and the_month != 2:
    return (month_days [the_month - 1])
  
  else:
    return (month_days [the_month - 1] + 1)

  
#user input
year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): ")) 
days = days_in_month(year, month)
print(f"\nThere are {days} days in {month}/{year}")

