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



