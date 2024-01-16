# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:21:22 2022

@author: oawar
"""

# tic tak toe
import numpy as np 
import math
board = np.full([3,3],"#")
count = 0

def checker(x):
    if len(x) != 3:
        return[100,100]
    elif("," not in x):
        return [6,9]
    if (x[0] not in "123") or (x[2] not in "123"):
        return [4,20]
    else:
        return [int(x[0]),int(x[2])]
    
def error(x):
    match x[0]:
        case 100:
            print("Please enter in the correct format")
            return False
        case 6:
            print("Please enter in the correct format")
            return False
        case 4:
            print("position doesn't exist")
            return False
    return True

def winCheck(board,xox):
    wincon = 0
    for k in range(2):
        for i in range(3):
            wincon = 0
            for j in range(3):
                if (board[i][j] == xox) and (k == 0):
                    wincon = wincon + 1
                elif (board[j][i] == xox) and (k == 1):
                    wincon = wincon + 1
                if wincon == 3:
                    if xox == "x":
                        print("you win")
                    else:
                        print("you lose")
                    return True
    if ((board[0][0] == xox) and (board[1][1]==xox) and (board[2][2]==xox)) or ((board[0][2]==xox)and(board[1][1]==xox)and(board[2][0]==xox)):
        if xox == "x":
            print("you win")
        else:
            print("you lose")
        return True
    
def positionTaken(board,index):
    if (board[index[0]-1,index[1]-1] in "x0"):
        return False
    else:
        return True
    
def AI0(board):
    wincon = 0
    diag = 0
    for k in range(3):
        for i in range(3):
            wincon = 0
            for j in range(3):
                if (board[i][j] == "x") and (k == 0):
                    wincon = wincon + 1
                elif (board[j][i] == "x") and (k == 1):
                    wincon = wincon + 1
                elif (board[j][j] == "x") and (k == 2):
                    wincon = wincon + 1
                if wincon == 2:
                    for j in range(3):
                        if (k == 0) and (board[i][j] == "#"):
                            board[i][j] = "0"
                            return board
                        elif (k==1)and(board[j][i] == "#"):
                            board[j][i] = "0"
                            return board
                        elif (k==2) and (board[j][j] == "#"):
                            board[j][j] = "0"
                            return board
    for i,j in zip(range(3),range(1,4)):
        if board[i][-j] == "x":
            diag = diag + 1
        if diag ==2:
           for i,j in zip(range(3),range(1,4)):
               if board[i][-j] == "#":
                   board[i][-j] = "0"
                   return board

    for i in range(3):
        for j in range(3):
            if (board[i,j] != "x") and (board[i,j] != "0"):
                board[i,j] = "0"
                return board
    return board

while True:
    action = input("Enter the index of your move:\t")
    if (error(checker(action))==False):
        continue
    if (positionTaken(board,checker(action))==False):
        continue
    count = count + 1
    index = checker(action)
    board[index[0]-1,index[1]-1] = "x"
    if winCheck(board,"x") == True:
        print(board)
        break
    board = AI0(board)
    if winCheck(board,"0") == True:
        print(board)
        break
    print(board)
    if winCheck(board,"x") == True:
        break
    if count == 5:
        print("Scratch!")
        break
#complete!
