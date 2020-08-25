"""
Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they 
want to write to the file. After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
A) Read the file
B) Delete the file and start over
C) Append the file
If the user wants to read the file it should simply show the contents of the file on the screen.
If the user wants to start over then the file should be deleted and another empty one made in its place. 
If a user elects to append the file, then they should be able to enter more text, and that text should be added 
to the existing text in the file. 

Extra Credit:
Allow the user to select a 4th option:
D) Replace a single line
If the user wants to replace a single line in the file, 
they will then need to be prompted for 2 bits of information:
1) The line number they want to update.
2) The text that should replace that line.
"""
# need to import a library for checking if a folder/file exists
import os

# Ask the user for a filename if it exists and the complete absolute path to the file
fileName = input("Please enter a filename to use(without the extension)\n")
fileName += ".txt"
# we need to append the absolute path to the file name or it will be stored in the root directory
completeFileName = os.path.join(os.path.dirname(__file__),fileName)

# check to see if the file exists
if os.path.isfile(completeFileName):
    # ask what to do with the existing file and use if elif statements accordingly
    fileMode = input("Would you like to\n1. Read the File(enter r)\n2. Delete the file and start over(enter w)\n3. Append the File(enter a)\n4. Replace a Single line(enter single line)\n")
    
    # used so that we can store the "single line" string (one of the options) for an if statement
    lineAdder = ""
    # set the file mode to read
    if fileMode == "single line":
        lineAdder = fileMode
        fileMode = "r"      
    fileAction = open(completeFileName, fileMode)
    # if/elif logic according to what the user chooses
    if lineAdder == "single line":
        lineNo = int(input("Which line would you like to replace?\n"))
        newText = input("What is the new text?\n")
        # readlines returns an array of lines from the text file
        lineOfText = fileAction.readlines()
        # replace the selected line with the new users text
        lineOfText[lineNo -1] = newText + "\n" 
        print(lineOfText) # For testing !!!
        # we have to open the file in write mode 
        fileAction = open(completeFileName, "w")    
        fileAction.writelines(lineOfText)
    elif fileMode == "r":
        print(fileAction.read())
    elif fileMode == "w":
        reWrite = input("You have choosen to rewrite the file please enter some new text\n")
        fileAction.write(reWrite)
    elif fileMode == "a":
        append = input("you have choosen to append to your previously made file please add some text\n")
        fileAction.write("\n" + append)
    # dont forget to close the file 
    fileAction.close()
# file doesnt exist lets create a new one with the name that was enter for the mystery file
else:
    newFileText = input("Please enter some text for your new file then press enter\n")
    newFile = open(completeFileName, "x")
    newFile.write(newFileText)
    newFile.close()
