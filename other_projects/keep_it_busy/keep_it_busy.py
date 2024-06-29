##################################################################################################
# Created by Sam Insanali
# GitHub: https://github.com/SInsanali
##################################################################################################
#The purpose of this program is to create a file called things.txt in C:\"user"\Documents
#and delete it after a wait time. It will run indefinitely until stopped by the user.

#I made this to keep the computer busy so it wont lock while doing other tasks
##################################################################################################

import os
import time
import random


# Define the path to the Documents folder
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

while True: #runs the loop forever
    # Define the full path to the file
    file_path = os.path.join(documents_folder, "things.txt")

    # Create and open the file
    with open(file_path, 'w') as file:
        pass  # Just open and close the file

    # Wait for 10 seconds
    time.sleep(10)
    
    random_number = random.randint(10,100)
    # Uncomment below for a random interval: 10-120 seconds
    #time.sleep(random_number)
    

    # Delete the file
    if os.path.exists(file_path):
        os.remove(file_path)

    # Wait for another 10 seconds before repeating
    time.sleep(10)
