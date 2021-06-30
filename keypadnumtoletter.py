# Given a numerical PIN, finds all possible combinations of telephone keypad letter equivalents.
# Please see the image in this repository for an example of such a keypad.
# This program assumes that any given digit can correspond to any of its assigned letters.
# This program does not account for multiple presses of a keypad number cycling through its assigned letters.

from itertools import product

# retrieves the appropriate letter corresponding to the entered number based on an index
def letterFetch(num, counter):
    if num == 0:
        return "_"
    elif num == 1:
        return "_"
    elif num == 2:
        if counter == 0:
            return "A"
        elif counter == 1:
            return "B"
        elif counter == 2:
            return "C"
        elif counter == 3:
            return
    elif num == 3:
        if counter == 0:
            return "D"
        elif counter == 1:
            return "E"
        elif counter == 2:
            return "F"
        elif counter == 3:
            return
    elif num == 4:
        if counter == 0:
            return "G"
        elif counter == 1:
            return "H"
        elif counter == 2:
            return "I"
        elif counter == 3:
            return
    elif num == 5:
        if counter == 0:
            return "J"
        elif counter == 1:
            return "K"
        elif counter == 2:
            return "L"
        elif counter == 3:
            return
    elif num == 6:
        if counter == 0:
            return "M"
        elif counter == 1:
            return "N"
        elif counter == 2:
            return "O"
        elif counter == 3:
            return
    elif num == 7:
        if counter == 0:
            return "P"
        elif counter == 1:
            return "Q"
        elif counter == 2:
            return "R"
        elif counter == 3:
            return "S"
    elif num == 8:
        if counter == 0:
            return "T"
        elif counter == 1:
            return "U"
        elif counter == 2:
            return "V"
        elif counter == 3:
            return
    elif num == 9:
        if counter == 0:
            return "W"
        elif counter == 1:
            return "X"
        elif counter == 2:
            return "Y"
        elif counter == 3:
            return "Z" 

def main():
    # variable for selecting calculation option
    pin = input("Enter the 4-number PIN with the digits separated by spaces: ")
    # list to hold the indicies for number selection
    letterPicker =  []
    # list of tuples containing every combination of indicies
    counters = product([0, 1, 2, 3], repeat = 4)
    
    # splits the entered digits to be handled one at a time
    digits = pin.split()

    # for every combination of indicies
    for i in list(counters):
        # covert tuples to lists
        letterPicker = list(i)
        # completed, valid alphabetical equivalent PIN
        finalAlpha = ""

        # for every digit in the PIN
        for k in range(4):
            # convert the number from letterPicker and the correct index from the current list combination of indicies
            finalAlpha += str(letterFetch(int(digits[k]), letterPicker[k]))
            # for non-7 or non-9 digits that do not have a fourth letter, clear finalAlpha to prevent invalid output
            if (digits[k] != 7 or digits[k] != 9) and letterPicker[k] == 3:
                finalAlpha = ""
                break
        # avoid printing blank finalAlpha's
        if finalAlpha == "" or finalAlpha == "_":
            continue
        # display a completed, valid alphabetical equivalent PIN
        print(finalAlpha)

main()
