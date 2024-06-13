import os
import time

# Define the path to the Documents folder
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

while True:
    # Define the full path to the file
    file_path = os.path.join(documents_folder, "things.txt")

    # Create and open the file
    with open(file_path, 'w') as file:
        pass  # Just open and close the file

    # Wait for 10 seconds
    time.sleep(10)

    # Delete the file
    if os.path.exists(file_path):
        os.remove(file_path)

    # Wait for another 10 seconds before repeating
    time.sleep(10)
