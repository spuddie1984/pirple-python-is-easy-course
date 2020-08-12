"""
Create a function that takes in two parameters: rows, and columns, both of which are integers. 
(as in the examples from the lectures)The function should then proceed to draw a playing board, the same number of rows and columns as specified. 
After drawing the board, your function should return True.
"""
# use these libraries to check the terminal's dimensions
import sys
import os

# 1st way
# just a simple for loop with some simple maths
def drawBoard(rows,columns):
    # loop through each row adding the gameboard's borders and spaces
    for row in range(1,(rows * 2)):
        # remember the seperator (-----) is considered a row as well
        # we are basically checking for the seperator row
        if row % 2 != 0: 
            print(" |" * (columns - 1))        
        else:
            print("-" * ((columns * 2) -1))
    return True

# uncomment function call below, to test the drawBoard function
# drawBoard(int(input("How many rows for your board game?\n")),int(input("how many columns as well?\n")))

# 2nd Way
# nested for loops example
def drawBoard2(rows,columns):
    for row in range(1,(rows * 2)):
        # print non-seperator rows
        if row % 2 != 0:
            # loop through each column
            for column in range(1,(columns * 2)):
                # print column borders,(end stops print moving to the next line)
                if column % 2 == 0:
                    print("|",end="")
                # print column tiles, (end stops print moving to the next line)
                elif column != ((columns * 2) -1):
                    print(" ",end="")    
                # dont forget to print the last column
                else:
                    print(" ")
        else:
            # print seperators
            print("-" * ((columns * 2) -1))
    return True

# uncomment function call below, to test the drawBoard2 function
# drawBoard2(int(input("How many rows for your board game?\n")),int(input("how many columns as well?\n")))

"""
Extra Credit:
Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. If someone passes a value greater than either maximum, your function should return Talse.
"""
# write the terminal's dimensions into corresponding variables for later use
terminalColumns, terminalRows = os.get_terminal_size()

# extra credits way ;P
# nested for loop example with terminal size checker
def drawBoard3(rows,columns):
    # check users inputted rows | columns isnt greater then terminal dimensions, if it is return false and tell the user
    if rows > terminalRows:
        print("Sorry too many rows, doesnt fit the terminal's screen height")
        return False
    elif  columns > terminalColumns:
        print("Sorry too many Columns, doesnt fit the terminal's screen width")
        return False
    else:
        for row in range(1,(rows * 2)):
            # print non-seperator rows
            if row % 2 != 0:
                # loop through each column
                for column in range(1,(columns * 2)):
                    # print column borders,(end stops print moving to the next line)
                    if column % 2 == 0:
                        print("|",end="")
                    # print column tiles, (end stops print moving to the next line)
                    elif column != ((columns * 2) -1):
                        print(" ",end="")
                    # dont forget to print the last column    
                    else:
                        print(" ")
            else:
                # print seperators
                print("-" * ((columns * 2) -1))
        return True

# drawBoard3(int(input("How many rows for your board game?\n")),int(input("how many columns as well?\n")))
