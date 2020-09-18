"""
Possible Improvements:
- More checks for correct input from user.


Once you've got the rules down, your assignment should be fairly straightforward. 
You'll want to draw the board, and allow two players to take turns placing their pieces on the board 
(but as you learned above, they can only do so by choosing a column, not a row). 
The first player to get 4 diagonally, vertically or horizontally wins !
The first player to get 4 across or diagonal should win!

Extra Credit:

Want to try colorful pieces instead of X and O? 
First you'll need to figure out how to import a package like termcolor into your project. 
We're going to cover importing later in the course, 
but try and see if you can figure it out on your own. 
Or you might be able to find unicode characters to use instead, 
depending on what your system supports. Here's a hint: print(u'\u2B24')
"""
# playing area 7w 6h
# 123456789112345
# | | | | | | | | row1
# |-------------|  row2 
# | | | | | | | | row3
# |-------------| row4
# and so on ........

# lets add a splash of color to our game
from termcolor import colored

# Could ask the user which player should start the game if you used an input instead of statically setting the variable
playerChecker = 1
# when this is false the game will finish
gameOver = False
winner = f''
# create a gameBoard array to keep track of players turns
# columns     1  2  3  4  5  6  7     
gameBoard = [["","","","","","",""], # row 1
             ["","","","","","",""], # row 2
             ["","","","","","",""], # row 3
             ["","","","","","",""], # row 4
             ["","","","","","",""], # row 5
             ["","","","","","",""]] # row 6
             
# this is based off of the gameboard array above any changes to the gameBoard array will be drawn to the console with this function
def drawBoard():
    for column in gameBoard:
        tile_data = f''
        for tile_no, tile in enumerate(column):
            if tile_no < 6:
                if len(tile) < 1:
                    tile_data += f'| '
                else:
                    tile_data += f'|{tile}'
            else:
                if len(tile) < 1:
                    tile_data += f'| |'
                else:
                    tile_data += f'|{tile}|'
        
        print(tile_data)
        print(f'---------------')

# psuedo code
# update the game board upon each players turn
# perform checks to place pieces in the correct areas/tiles

# Add player tile to the board
def makePlayerMove(column,playerPiece):
    # Assign each player peice a different color
    pieceCoordinates = []
    # Have to check for existing tiles in the respective column
    # start counting  from the end of the list looking for the next empty spot
    for tile in range(len(gameBoard)-1, -1, -1):
        if len(gameBoard[tile][column]) < 1:
            gameBoard[tile][column] = playerPiece
            pieceCoordinates = [tile,column,playerPiece]
            # We have found an empty spot lets make a break for it
            break
    # after all of that lets redraw the updated board
    drawBoard()
    # return the index of the players piece so that we can check for a win
    return pieceCoordinates


# check for player won condition vertically
def verticalChecker(player,pieceCoordinates):
    # set opponents piece for current players turn
    if player == 1:
        opponent = colored('O', 'green')
    elif player == 2:
        opponent = colored('X', 'red')
    # check vertically for 4 in a row
    # pieceCoordinates[row,column]
    # start from coord and move down, only proceed checking from rows 1-3(in other words there is already 3 pieces in the column).
    if pieceCoordinates[0] < 3:
        for checkWin in range(pieceCoordinates[0], pieceCoordinates[0] + 4):
            # if oponents piece is present then move on to next check and break from this one
            if gameBoard[checkWin][pieceCoordinates[1]] == opponent:
                horizontalChecker(player,pieceCoordinates,opponent)
                break
            elif checkWin >= pieceCoordinates[0] + 3:
                global gameOver
                global winner
                gameOver = True
                winner = f'Player {player}'

    else:
        horizontalChecker(player,pieceCoordinates,opponent)          
    
# check for player won condition horizontally
def horizontalChecker(player,pieceCoordinates,opponent):
    # pieceCoordinates[row,column]
    rightBoardEdge = 7
    leftBoardEdge = 0
    global gameOver
    global winner
    inARowCount = 0
    # psuedocode
    # 2 checks when a player moves left and right
    # left: if not left edge check, add checked pieces (if any exist) to checked piece counter,if opponents or empty tiles stop adding and move on
    # right: if not right edge check, add checked pieces (if any exist) to checked piece counter,if opponents or empty tiles stop adding and move on
    for countLeft in range(pieceCoordinates[1]-1,leftBoardEdge-1,-1):
        if gameBoard[pieceCoordinates[0]][countLeft] ==  opponent or len(gameBoard[pieceCoordinates[0]][countLeft]) < 1:
            break
        else:
            inARowCount += 1
    for countRight in range(pieceCoordinates[1]+1,rightBoardEdge,1):
        if gameBoard[pieceCoordinates[0]][countRight] ==  opponent or len(gameBoard[pieceCoordinates[0]][countRight]) < 1:
            break
        else:
            inARowCount += 1
    # check for win
    if inARowCount == 3:
        gameOver = True
        winner = f'Player {player}'
    else:
        diagonalChecker(player,pieceCoordinates,opponent)

# check for player won condition diagonally
def diagonalChecker(player,pieceCoordinates,opponent):
     
    rightBoardEdge = 5
    leftBoardEdge = 0
    topBoardEdge = 0
    bottomBoardEdge = 6
    goingLeftCounter = 0
    goingRightCounter = 0
    diagonalRowLeftCounter = 0
    diagonalRowRightCounter = 0
    global gameOver
    global winner

    # pieceCoordinates[row,column]
    goingLeftCounter = goingRightCounter = pieceCoordinates[1]
    for countToTopLeft in range(pieceCoordinates[0],topBoardEdge,-1):
        if pieceCoordinates[1] > leftBoardEdge +1 and countToTopLeft -1 != topBoardEdge:
            goingLeftCounter -= 1
            if gameBoard[countToTopLeft -1][goingLeftCounter] == opponent or len(gameBoard[countToTopLeft -1][goingLeftCounter]) < 1:
                break
            else:
                diagonalRowLeftCounter += 1 
        
    for countToTopRight in range(pieceCoordinates[0],topBoardEdge,+1):
        if pieceCoordinates[1] < rightBoardEdge -1 and countToTopRight -1 != topBoardEdge:
            goingRightCounter += 1
            if gameBoard[countToTopRight -1][goingRightCounter] == opponent or len(gameBoard[countToTopRight -1][goingRightCounter]) < 1:
                break
            else:
                diagonalRowRightCounter += 1 
    
    # reset left, right counters for next set of loop checks
    goingLeftCounter = goingRightCounter = pieceCoordinates[1]
    for countToBottomLeft in range(pieceCoordinates[0],bottomBoardEdge,1):
        if pieceCoordinates[1] > leftBoardEdge + 1 and countToBottomLeft +1 != bottomBoardEdge:
            goingLeftCounter -= 1
            if gameBoard[countToBottomLeft +1][goingLeftCounter] == opponent or len(gameBoard[countToBottomLeft +1][goingLeftCounter]) < 1:
                break
            else:
                diagonalRowLeftCounter += 1 
        
    for countToBottomRight in range(pieceCoordinates[0],bottomBoardEdge,1):
        if pieceCoordinates[1] < rightBoardEdge -1 and countToBottomRight +1 != bottomBoardEdge:
            goingRightCounter +=  1
            if gameBoard[countToBottomRight +1][goingRightCounter] == opponent or len(gameBoard[countToBottomRight +1][goingRightCounter]) < 1:
                break
            else:
                diagonalRowRightCounter += 1 

    # check for win
    if diagonalRowLeftCounter == 3 or diagonalRowRightCounter == 3:
        gameOver = True
        winner = f'Player {player}'

# this is the function that asks the player to make a move ;P
def playerTurn(player):
    coloredPlayer1 = colored('Player1','red')
    coloredPlayer2 = colored('Player2','green')
    askAgain = False
    if player == 1:
        while(True): 
            if not askAgain: 
                player1 = int(input(f'What column would {coloredPlayer1} like place their piece(note columns start from 0 and go to 6:'))
            if len(gameBoard[0][player1]) < 1:
                # start the check for win process
                verticalChecker(1,makePlayerMove(player1,colored('X', 'red')))
                askAgain = False
                break
            else:
                askAgain = True
                player1 = int(input(f'Sorry {coloredPlayer1} that column is full try another(note columns start from 0 and go to 6:'))
    elif player == 2:
        while(True):
            if not askAgain:
                player2 = int(input(f'What column would {coloredPlayer2} like place their piece(note columns start from 0 and go to 6:'))
            if len(gameBoard[0][player2]) < 1:
                # start the check for win process
                verticalChecker(2,makePlayerMove(player2,colored('O', 'green')))
                askAgain = False
                break
            else: 
                askAgain = True
                player2 = int(input(f'Sorry {coloredPlayer2} that column is full try another(note columns start from 0 and go to 6:'))


# keep prompting players to make a move until there is a win condition
while(gameOver == False):
    if playerChecker == 1:
        playerTurn(playerChecker)
        playerChecker += 1
    elif playerChecker == 2:
        playerTurn(playerChecker)
        playerChecker = 1
else:
    print(f'Game Over {winner} wins!!')
