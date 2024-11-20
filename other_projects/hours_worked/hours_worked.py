##################################################################################################
##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
##################################################################################################
# Description:
# This calculates the hours worked in a day

##################################################################################################
##################################################################################################


#clear screen function
from os import system, name
def clear(): 
    """Clears the screen on the console"""
    #for windows
    if name == "nt":
        system("cls")
    #for mac and linux(here, os.name is 'posix')
    else:
        system("clear")

#try/ except for clean keyboard interrupt
try:
    #Wrap the main code in here

    clear()

    print("\nCreated by Sam Insanali || GitHub: https://github.com/SInsanali ")

    #user prompts
    print ("\n[-] This program will calculate the amount of hours you worked in a day")
    print ("\n[-] It works in 24 hr format, accepable times range from 0000-2400")

    start_time = int(input("\n[?] What time did you come into work today?: "))
    end_time = int(input("\n[?] What time did you finish working?: "))

    # Function to calculate hours worked
    def calculate_hours_worked(start, end):
        # Assuming the times are in the format HHMM
        start_hours = start // 100
        start_minutes = start % 100
        end_hours = end // 100
        end_minutes = end % 100

        # Convert everything to minutes
        start_total_minutes = start_hours * 60 + start_minutes
        end_total_minutes = end_hours * 60 + end_minutes

        # Calculate the difference
        if end_total_minutes < start_total_minutes:
            # This accounts for working past midnight
            minutes_worked = (1440 - start_total_minutes) + end_total_minutes
        else:
            minutes_worked = end_total_minutes - start_total_minutes

        # Convert back to hours and minutes
        hours_worked = minutes_worked // 60
        remaining_minutes = minutes_worked % 60

        return hours_worked, remaining_minutes

    # Get the time worked
    hours, minutes = calculate_hours_worked(start_time, end_time)

    # Output the result
    print(f"\n[!] You worked for {hours} hours and {minutes} minutes today.\n")

except KeyboardInterrupt:
    #Print an error message and exit cleanly
    print("\nExecution interrupted by user. Exiting program.")