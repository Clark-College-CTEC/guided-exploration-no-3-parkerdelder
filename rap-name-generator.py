# Guided Exploration No. 3
# Parker Elder

# Import the random library
import random

# Assigns an empty list to the variable
possible_names = []

# Creates a .txt file for our rap name to be recorded, it will open the file and write the name when we run the program
outputFile = open('rap-names-output.txt', 'w')

# Opens the rap-names file to be read as the variable 'dataFile'
with open('rap-names.txt', 'r') as dataFile:
    # This loop will iterate through each name in the rap-names file line-by-line
    for name in dataFile:
        # This will strip the invisible line feed off the end of each line and then add the name to the possible_names list we created on line 8
        possible_names.append(name.rstrip())

# Asks the user how many rap names they want to create(must be a whole number)
count = int(input('How many rap names would you like to create? '))
# Asks the user how many parts the name should contain(must be a whole number)
parts = int(input('How many parts should the name contain? '))

# Runs a counted loop for the above input "count" variable
for i in range(count):
    # This will add the name parts to into the list as they are generated
    name_parts = []
    # Runs a counted loop for the amount of name parts defined in the input above
    for j in range(parts):
        # This will generate a random number to select a random name from the possible_names.txt file, it will then add it to the name_parts.txt file
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
        # This will write the newly generated name into the name_parts.txt file and glue the names together separated by a ' ' and then adds a new line at the end of the name.
        outputFile.write(f"{' '.join(name_parts)}\n")
        # This will print out the same thing that is being written to the name_parts.txt file, but in the terminal below in VS Code.
        print(f"{' '.join(name_parts)}")
# This will close the file after it has completed running the program
outputFile.close()
