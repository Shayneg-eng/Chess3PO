import chess 
from chessboard import display

import chess
import chess.svg
import chess.polyglot
from datetime import datetime
import time
import random
import os

numberOfMovesSearched = 0
board = chess.Board()


def countPieces():
    
    pawnValue = 100
    knightValue = 300
    bishopValue = 320
    rookValue = 500
    queenValue = 900
    
    strBoard = str(board)
    
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
      

def pieceLocationValue():
    
    strBoard = str(board)

    currentSquareBeingChecked = 0
    BOTpieceLocationValue = 0
    PLAYERpieceLocationValue = 0

    for piece in list(strBoard):
        if piece == ' ' or piece == '\n':
            continue
        elif piece == '.':
            currentSquareBeingChecked += 1       
        elif piece == 'r':
            BOTpieceLocationValue += botRookTable[currentSquareBeingChecked]    
            currentSquareBeingChecked += 1                               
        elif piece == 'n':                 
            BOTpieceLocationValue += botKnightTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'b':                                           
            BOTpieceLocationValue += botBishopTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'q':                             
            BOTpieceLocationValue += botQueenTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'p':
            BOTpieceLocationValue += botPawnTable[currentSquareBeingChecked]   
            currentSquareBeingChecked += 1                                
        elif piece == 'k':
            BOTpieceLocationValue += botKingTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'K':
            PLAYERpieceLocationValue += playerKingTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'R':                    
            PLAYERpieceLocationValue += playerRookTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'N':
            PLAYERpieceLocationValue += playerKnightTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'B':                          
            PLAYERpieceLocationValue += playerBishopTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'Q':                    
            PLAYERpieceLocationValue += playerQueenTable[currentSquareBeingChecked]
            currentSquareBeingChecked += 1 
        elif piece == 'P':
            PLAYERpieceLocationValue += playerPawnTable[currentSquareBeingChecked]    
            currentSquareBeingChecked += 1                       
        
    return [PLAYERpieceLocationValue, BOTpieceLocationValue]

def endGame():
    print("----------game end----------")
    os._exit(1)

def findLeagalMoves():
    leagalMoves = board.legal_moves
    leagalMoves = str(leagalMoves)
    parenthesesOneLocation = leagalMoves.find('(')
    parenthesesTwoLocation = leagalMoves.find(')')
    leagalMovesList = leagalMoves[(parenthesesOneLocation+1):parenthesesTwoLocation]
    leagalMovesList = leagalMovesList.split(',')
    return leagalMovesList

def findBestNextMoveForPlayer():
    global numberOfMovesSearched
    
    bestNextMove = 0# going to be set to the evaluation for the best, worst response 
    ABpruningNumber = 10000
    responseMoves = []
    # get legal moves for me
    legalPlayerMoves = findLeagalMoves()
    finalResponseMoveList = []# will compare this with legalPlayerMoves to find best move to make
    
    # for each legal move for me
    
    
    for legalPlayerMove in findLeagalMoves():
        board.push_san(legalPlayerMove.strip())

        for responseMove in findLeagalMoves():
            board.push_san(responseMove.strip())
            
            for responseMove in findLeagalMoves():
                board.push_san(responseMove.strip())   
                responseMove = (pieceLocationValue()[0] - pieceLocationValue()[1]) + (-1 * (countPieces()[0] - countPieces()[1]))# getting the eval for the response move             
                
                if responseMove < ABpruningNumber:
                    ABpruningNumber = responseMove
                    board.pop()
                    break
                
                else:
                    board.pop()# undoing the move so we can play the next response
                    responseMoves.append(responseMove) # adding them to responseMoves list  
                
                numberOfMovesSearched += 1      

            board.pop()# undoing the legal move that we made to start with
        
        bestResponseBoardEval = max(responseMoves)# finding the opponents best response move
        responseMoves = []# clearing the list so it can be used again
        finalResponseMoveList.append(bestResponseBoardEval)
        board.pop()

    bestNextMove = min(finalResponseMoveList)

    indexOfBestMoveToMake = finalResponseMoveList.index(bestNextMove)#finding the index of the best move

    moveToPlay = legalPlayerMoves[indexOfBestMoveToMake]# plugging the index into all of the legal moves

    return moveToPlay


def game():
    print("\n\n\n\n\n\n\n\n\n\n\n")
    print(board)

    legalMoves = ','
    moveNumber = 0
    
    while True:
        
        if moveNumber != 0:
            print("\n\n\n\n\n\n\n\n\n\n\n")
            print(board)
            print("Time for move:", time.time() - startTime)
            print("Number of moves searched:", numberOfMovesSearched)

        playerScore = pieceLocationValue()[1]
        botScore = pieceLocationValue()[0]
        W_Lratio = playerScore - botScore
        
        print("your score:", round((playerScore / (-1.45)),2),"||      BOT score:", round((botScore / (-1.45)),2), "||      W/L:", W_Lratio)
        try:
            print("your legal moves are: ", legalMoves.join(findLeagalMoves()))
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
            print("please play one of the avalable leagal moves listed below")
            continue
        
        startTime = time.time()
        board.push_san(findBestNextMoveForPlayer().strip())

game()