'''
THIS CODE USES A LIBRARY:
THIS PROGRAM USES THE PYTHON CHESS LIBRARY
LINK TO LIBRARY: https://python-chess.readthedocs.io/en/latest/
THIS LIBRARY IS USED TO FACILITATE MOVES ON THE BOARD AND THE CHESS GAME ENGINE INCLUDING LEGAL MOVES, THE BOARD, AND GAME CASES
SO THAT THE GAME MAY RUN
THE AI ALGORITHM WAS CREATED BY OURSELVES, AND WAS NOT TAKEN FROM THIS LIBRARY
 
THIS CODE ALSO USES TWO OTHER LIBRARIES THAT ARE BUILT INTO PYTHON: OS, AND TIME
OS AND TIME ARE PURELY FOR MAKING THE BOT LOOK GOOD AND PROVIDING STATS LIKE THE AMOUNT OF TIME TAKEN TO MAKE A MOVE
'''
 
 
from itertools import count
import chess, time, os

from pyparsing import White
 
'''
Sequencing:
     - The board is initialized along with the counter for the moves searched
'''
board = chess.Board()
 
#Counter Variable
movesSearched = 0
 
 
#Function that counts the pieces on the board along with their value
def countPieces():
    '''
    Sequencing:
        - Piece Values are initialized 1 by 1
        - Once the pieces values are initialized, the board
        searches for all instances of the board and assigns
        them to a variable.
    '''
   
    #Piece Values
    pawnValue = 100
    knightValue = 300
    bishopValue = 320
    rookValue = 500
    queenValue = 900
   
    #Board is being visualized as a string
    strBoard = str(board)
   
    #Counter variable of each piece
    rCount = 0
    nCount = 0
    bCount = 0
    qCount = 0
    pCount = 0
    RCount = 0
    NCount = 0
    BCount = 0
    QCount = 0
    PCount = 0
   
    #.count() method used to search for all instances
    rCount = strBoard.count('r')
    nCount = strBoard.count('n')
    bCount = strBoard.count('b')
    qCount = strBoard.count('q')
    pCount = strBoard.count('p')
    RCount = strBoard.count('R')
    NCount = strBoard.count('N')
    BCount = strBoard.count('B')
    QCount = strBoard.count('Q')
    PCount = strBoard.count('P')
 
    whiteValue = (rCount * rookValue) + (nCount * knightValue) + (bCount * bishopValue) + (qCount * queenValue) + (pCount * pawnValue)
    blackValue = (RCount * rookValue) + (NCount * knightValue) + (BCount * bishopValue) + (QCount * queenValue) + (PCount * pawnValue)
   
    return [whiteValue, blackValue]
   
 
 
'''
Sequencing:
    - Each table is initialized to represent the best move for
    the computer and the player depending on the piece that they were to play.
'''
botPawnTable = [
0, 0, 0, 0, 0, 0, 0, 0,
5, 10, 10, -20, -20, 10, 10, 5,
5, -5, -10, 0, 0, -10, -5, 5,
0, 0, 0, 20, 20, 0, 0, 0,
5, 5, 10, 25, 25, 10, 5, 5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
0, 0, 0, 0, 0, 0, 0, 0]
 
playerPawnTable = [
0, 0, 0, 0, 0, 0, 0, 0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
5, 5, 10, 25, 25, 10, 5, 5,
0, 0, 0, 20, 20, 0, 0, 0,
5, -5, -10, 0, 0, -10, -5, 5,
5, 10, 10, -20, -20, 10, 10, 5,
0, 0, 0, 0, 0, 0, 0, 0]
 
botKnightTable = [
-50, -40, -30, -30, -30, -30, -40, -50,
-40, -20, 0, 5, 5, 0, -20, -40,
-30, 5, 10, 15, 15, 10, 5, -30,
-30, 0, 15, 20, 20, 15, 0, -30,
-30, 5, 15, 20, 20, 15, 5, -30,
-30, 0, 10, 15, 15, 10, 0, -30,
-40, -20, 0, 0, 0, 0, -20, -40,
-50, -40, -30, -30, -30, -30, -40, -50]
 
playerKnightTable = [
-50, -40, -30, -30, -30, -30, -40, -50,
-40, -20, 0, 0, 0, 0, -20, -40,
-30, 0, 10, 15, 15, 10, 0, -30,
-30, 5, 15, 20, 20, 15, 5, -30,
-30, 0, 15, 20, 20, 15, 0, -30,
-30, 5, 10, 15, 15, 10, 5, -30,
-40, -20, 0, 5, 5, 0, -20, -40,
-50, -40, -30, -30, -30, -30, -40, -50]
 
botBishopTable = [
-20, -10, -10, -10, -10, -10, -10, -20,
-10, 5, 0, 0, 0, 0, 5, -10,
-10, 10, 10, 10, 10, 10, 10, -10,
-10, 0, 10, 10, 10, 10, 0, -10,
-10, 5, 5, 10, 10, 5, 5, -10,
-10, 0, 5, 10, 10, 5, 0, -10,
-10, 0, 0, 0, 0, 0, 0, -10,
-20, -10, -10, -10, -10, -10, -10, -20]
 
playerBishopTable = [
-20, -10, -10, -10, -10, -10, -10, -20,
-10, 0, 0, 0, 0, 0, 0, -10,
-10, 0, 5, 10, 10, 5, 0, -10,
-10, 5, 5, 10, 10, 5, 5, -10,
-10, 0, 10, 10, 10, 10, 0, -10,
-10, 10, 10, 10, 10, 10, 10, -10,
-10, 5, 0, 0, 0, 0, 5, -10,
-20, -10, -10, -10, -10, -10, -10, -20]
 
botRookTable = [
0, 0, 0, 5, 5, 0, 0, 0,
-5, 0, 0, 0, 0, 0, 0, -5,
-5, 0, 0, 0, 0, 0, 0, -5,
-5, 0, 0, 0, 0, 0, 0, -5,
-5, 0, 0, 0, 0, 0, 0, -5,
-5, 0, 0, 0, 0, 0, 0, -5,
5, 10, 10, 10, 10, 10, 10, 5,
0, 0, 0, 0, 0, 0, 0, 0]
 
playerRookTable = [
0, 0, 0, 0, 0, 0, 0, 0,
5, 10, 10, 10, 10, 10, 10, 5,
-5, 0, 0, 0, 0, 0, 0, -5,
-5, 0, 0, 0, 0, 0, 0, -5,
-5, 0, 0, 0, 0, 0, 0, -5,
-5, 0, 0, 0, 0, 0, 0, -5,
-5, 0, 0, 0, 0, 0, 0, -5,
0, 0, 0, 5, 5, 0, 0, 0]
 
playerKingTable = [
20, 30, 10, 0, 0, 10, 30, 20,
20, 20, 0, 0, 0, 0, 20, 20,
-10, -20, -20, -20, -20, -20, -20, -10,
-20, -30, -30, -40, -40, -30, -30, -20,
-30, -40, -40, -50, -50, -40, -40, -30,
-30, -40, -40, -50, -50, -40, -40, -30,
-30, -40, -40, -50, -50, -40, -40, -30,
-30, -40, -40, -50, -50, -40, -40, -30]
 
botKingTable = [
-30, -40, -40, -50, -50, -40, -40, -30,
-30, -40, -40, -50, -50, -40, -40, -30,
-30, -40, -40, -50, -50, -40, -40, -30,
-30, -40, -40, -50, -50, -40, -40, -30,
-20, -30, -30, -40, -40, -30, -30, -20,
-10, -20, -20, -20, -20, -20, -20, -10,
20, 20, 0, 0, 0, 0, 20, 20,
20, 30, 10,0, 0, 10, 30, 20]
 
playerQueenTable = [
-20, -10, -10, -5, -5, -10, -10, -20,
-10, 0, 0, 0, 0, 0, 0, -10,
-10, 5, 5, 5, 5, 5, 0, -10,
0, 0, 5, 5, 5, 5, 0, -5,
-5, 0, 5, 5, 5, 5, 0, -5,
-10, 0, 5, 5, 5, 5, 0, -10,
-10, 0, 0, 0, 0, 0, 0, -10,
-20, -10, -10, -5, -5, -10, -10, -20]
 
botQueenTable = [
-20, -10, -10, -5, -5, -10, -10, -20,
-10, 0, 0, 0, 0, 0, 0, -10,
-10, 0, 5, 5, 5, 5, 0, -10,
-5, 0, 5, 5, 5, 5, 0, -5,
-5, 0, 5, 5, 5, 5, 0, 0,
-10, 0, 5, 5, 5, 5, 5, -10,
-10, 0, 0, 0, 0, 0, 0, -10,
-20, -10, -10, -5, -5, -10, -10, -20]
     
 
#Function that finds where the pieces are on the board
def pieceLocationValue():
   
    '''
    Sequencing:
        - Initializing stringed board as well as counter variables before
        continuing the function.
    '''
 
    strBoard = str(board)
 
    currentSquareBeingChecked = 0
    BOTpieceLocationValue = 0
    PLAYERpieceLocationValue = 0
 
    '''
    Iteration:
        - For loop that iterates through the str board.
        - Assign each iteration value to 'piece'.
   
    Selection:
        - if, elif branches that check the current square
        that is being checked.
        - Assigns each black piece that is found to the computer's
        piece location values.
        - Assigns each white piece that is found to the player's
        piece location values.
    '''
    pieceTables = {
        'r': botRookTable, 'n': botKnightTable, 'b': botBishopTable,
        'q': botQueenTable, 'p': botPawnTable, 'k': botKingTable,
        'K': playerKingTable, 'R': playerRookTable, 'N': playerKnightTable,
        'B': playerBishopTable, 'Q': playerQueenTable, 'P': playerPawnTable
    }

    BOTpieceLocationValue = PLAYERpieceLocationValue = currentSquareBeingChecked = 0

    for piece in strBoard:
        if piece in pieceTables:
            if piece.islower():
                BOTpieceLocationValue += pieceTables[piece][currentSquareBeingChecked]
            else:
                PLAYERpieceLocationValue += pieceTables[piece][currentSquareBeingChecked]
            currentSquareBeingChecked += 1
        elif piece == '.':
            currentSquareBeingChecked += 1

    return [PLAYERpieceLocationValue, BOTpieceLocationValue]
 
#Function that ends the game if needed
def endGame():
    '''
    Sequencing:
         - prints the game ending message and uses the os
    module to exit the code.
    '''
    print(""" ________                        ___________            ___
 /  _____|_____    _____   ____   \_   _____/ ____    __| _/
/   \  ___\__  \  /     \_/ __ \   |    __)_ /    \  / __ |
\    \_\  \/ __ \|  Y Y  \  ___/   |        \   |  \/ /_/ |
 \______  (____  /__|_|  /\___  > /_______  /___|  /\____ |
        \/     \/      \/     \/          \/     \/      \/ )
        """)
    os._exit(1)
 
#Function that finds the legal moves for each side
def findLegalMoves(visualOrCompute):
 
    '''
    Sequencing:
        - Initializes the Legal Moves
        - Initializes the Legal Moves as a list in regard
        to the instances.
    '''
    numOfLegalMoves = 0
    LegalMoves = board.legal_moves
    LegalMoves = str(LegalMoves)
    parenthesesOneLocation = LegalMoves.find('(')
    parenthesesTwoLocation = LegalMoves.find(')')
    LegalMovesList = LegalMoves[(parenthesesOneLocation+1):parenthesesTwoLocation]
    LegalMovesList = LegalMovesList.split(',')
    if visualOrCompute == 'visual':
        for move in LegalMovesList:
            numOfLegalMoves += 1  
        print("you have",numOfLegalMoves, "legal moves")
        LegalMovesList = ' '.join(LegalMovesList)
        return LegalMovesList
    elif visualOrCompute == 'compute':
        return LegalMovesList
    return
 
#Function that calculates the best next move for the player
def findBestNextMoveForPlayer():
 
    '''
    Sequencing:
        - Assigns the necessary variables before continuing with the code
    Iteration:
        - Nested For loops that searches within the legalMoves and calculates the best
        move for the player using a linear search
    '''
   
    #bestNextMove is set to the evaluation for the best, worst response
    bestNextMove = 0
    movesSearched = 0
    responseMoves = []
 
    #Gets the LegalMoves for the player
    legalPlayerMoves = findLegalMoves('compute')
 
    #Compares the  finalResponseMoveList with legalPlayerMoves to find the best move to make
    finalResponseMoveList = []
   
   
   
    #For loop that searches through the findLegalMoves() function
    for legalPlayerMove in findLegalMoves('compute'):
        board.push_san(legalPlayerMove.strip())
 
        for responseMove in findLegalMoves('compute'):
            board.push_san(responseMove.strip())
           
            for responseMove in findLegalMoves('compute'):
                board.push_san(responseMove.strip())
               
                #Gets the eval for the response move
                responseMove = (pieceLocationValue()[0] - pieceLocationValue()[1]) + (-1 * (countPieces()[0] - countPieces()[1]))
 
                #Undoing the move so we can play the next response
                board.pop()
 
                #Adding the moves to the response list
                responseMoves.append(responseMove)
           
                movesSearched += 1      
            #Undoing the move that we made to start with
            board.pop()
       
        #Finding the opponent's best response move
        bestResponseBoardEval = max(responseMoves)
 
        #Clearing the list so it can be used again
        responseMoves = []
        finalResponseMoveList.append(bestResponseBoardEval)
        board.pop()
 
    bestNextMove = min(finalResponseMoveList)
 
    #Finding the index of the best move
    indexOfBestMoveToMake = finalResponseMoveList.index(bestNextMove)
 
    #Pluggin the index into all of the legal moves
    moveToPlay = legalPlayerMoves[indexOfBestMoveToMake]
 
    return moveToPlay, movesSearched
 
 
'''
Sequencing:
    - Prints the board, and initializes the necessary variables
Selection:
    - try and except block that checks for errors
        - If there is an error, it will print a message to the player
    - if, else that checks the user's input and determines whether the game should continue
Iteration:
    - while Loop that continues until the game is complete
'''
#Function that facilitates the game
def game(check):
 
 
    if check.lower() == "yes":
        print("\n\n\n")
        print(board)
 
        legalMoves = ','
        moveNumber = 0
           
   
        while True:
            
            if moveNumber != 0:
                print("\n\n\n\n\n\n\n\n\n\n\n")
                print(board)
                print("Time for move:", time.time() - startTime)
                print("Number of moves searched:", movesSearched)
 
            playerScore = pieceLocationValue()[1] + countPieces()[1]
            botScore = pieceLocationValue()[0] + countPieces()[0]
            W_Lratio = playerScore - botScore
           
            print("your score:", playerScore,"||      BOT score:", botScore, "||      W/L:", W_Lratio)
            try:
                print("your legal moves are: ", findLegalMoves('visual'))
                playersMove = input('enter your move or type "stop" to terminate: ')
                if playersMove == 'stop':
                    endGame()
                elif playersMove == 'undo':
                    board.pop(); board.pop()
                else:
                    board.push_san(playersMove)
                    print(board)
                    moveNumber += 1
            except:
                print("please play one of the available Legal moves listed below")
                continue
       
            startTime = time.time()
            BOTmove, movesSearched = findBestNextMoveForPlayer()
            board.push_san(BOTmove.strip())
            print("My move is:", BOTmove)
    else:
        print("Thank you for playing....Not...")
'''
Game function is called to start the program,
and the chess game
'''
 
check = input("""\n\n\n\n\n\n
________                                                         __      __                     __                 __                               _________
\______ \   ____    ___.__. ____  __ __  __  _  _______    _____/  |_  _/  |_  ____     _______/  |______ ________/  |_     _________    _____   ___\_____   |
 |    |  \ /  _ \  <   |  |/  _ \|  |  \ \ \/ \/ /\__  \  /    \   __\ \   __\/  _ \   /  ___/\   __\__  ||_  __ \   __\   / ___\__  \  /     \_/ __ \ /   __/
 |    `   (  <_> )  \___  (  <_> )  |  /  \     /  / __ \|   |  \  |    |  | (  <_> )  \___ \  |  |  / __ \|  | \/|  |    / /_/  > __ \|  Y Y  \  ___/|   |  
/_______  /\____/   / ____|\____/|____/    \/\_/  (____  /___|  /__|    |__|  \____/  /____  > |__| (____  /__|   |__|    \___  (____  /__|_|  /\___  >___|  
        \/          \/                                 \/     \/                           \/            \/              /_____/     \/      \/     \/<___> \n
 
Answer: """)
game(check)

