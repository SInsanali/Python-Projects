line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your stash! X marks the spot.")
position = input("Where do you want to put the secret stuff?\n")

#make the letter varible that isolates the first letter in the input and make sure theyre uppercase
letter = position[0].upper()

#make a list that contains all of the acceptable inputs for postition variable
abc = ["A","B","C"]
#correlate an index number to the letter that is inputted
letter_index = abc.index(letter)
#correlate an index number for the number that is inputted
#subtract 1 to meet zero indexing standards
number_index = int(position[1]) -1

#make the x appear on the 'map' 
#number index comes first because the line number (y axis on the map) needs to be specified first
#list[which item in the list][which character in the item]
map[number_index][letter_index] = 'X'

