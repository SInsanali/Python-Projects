#NOTE
#define clear screen function
from os import system, name

def clear(): 
    #for windows
    if name == "nt":
        action = system("cls")
    #for mac and linux(here, os.name is 'posix')
    else:
        action = system("clear")





#NOTE
#try/ except for clean keyboard interrupt

try:
    #Wrap the main code in here
    

except KeyboardInterrupt:
    #Print an error message and exit cleanly
    print("\nExecution interrupted by user. Exiting program cleanly.")


#NOTE
#While loop input validation
while True:
    shift_input = input("How many places will this be shifted?:\n")   

    if shift_input.isdigit():
        shift = int(shift_input)
        break
    else:
        print("\nPlease enter a valid number.")
