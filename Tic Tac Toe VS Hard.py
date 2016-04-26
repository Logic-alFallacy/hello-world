import random

board = []

for x in range(0,3):
    board.append (["-"] * 3)




def print_board (board):
    for row in board:
        print (" ".join(row))



boardNum ="""1 2 3
4 5 6
7 8 9
"""

mode = ""
val = 0

while mode != "1" and mode != "2":
    mode = input("\nType 1 to play against another human or type 2 to play against a computer.\n> ")
    
mode=int(mode)

if mode == 1:
           
    while val < 9:
    
        pickaTruth = True

        while pickaTruth == True:
            print("\n\n")

            print (boardNum)
            
            pickaPlace = int(input("\n\nX, choose the number of the position in which your piece will go: "))
            if pickaPlace < 1 and pickaPlace > 9:
                pickaTruth = True
            elif pickaPlace == 1:
                pickarow = 0
                pickacol = 0
            elif pickaPlace == 2:
                pickarow = 0
                pickacol = 1
            elif pickaPlace == 3:
                pickarow = 0
                pickacol = 2
            elif pickaPlace == 4:
                pickarow = 1
                pickacol = 0
            elif pickaPlace == 5:
                pickarow = 1
                pickacol = 1
            elif pickaPlace == 6:
                pickarow = 1
                pickacol = 2
            elif pickaPlace == 7:
                pickarow = 2
                pickacol = 0
            elif pickaPlace == 8:
                pickarow = 2
                pickacol = 1
            elif pickaPlace == 9:
                pickarow = 2
                pickacol = 2
        
        

            if (board[pickarow][pickacol] == "X") or (board[pickarow][pickacol] == "O"):
                print ("\nThis is already taken.\n")
            else:
                print ("\nSuccess!\n")
                board[pickarow][pickacol] = "X"
    
                print_board (board)
                print ("\n\n")
                
                
                pickaTruth = False
            break
        val += 1
        if (board[0][0] == "X") and (board[1][0] == "X") and (board[2][0] == "X") or (board[0][1] == "X") and (board[1][1] == "X") and (board[2][1] == "X") or (board[0][2] == "X") and (board[1][2] == "X") and (board[2][2] == "X") or (board[0][0] == "X") and (board[0][1] == "X") and (board[0][2] == "X") or (board[1][0] == "X") and (board[1][1] == "X") and (board[1][2] == "X") or (board[2][0] == "X") and (board[2][1] == "X") and (board[2][2] == "X") or (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] == "X") or (board[0][2] == "X") and (board[1][1] == "X") and (board[2][0] == "X"):
            print ("X has won! Congratulations, player X.\n\n")
            val = 9
            input ("Press enter to exit.")
        

        if val == 9:
            break

        print ("\n\n")
    
        print (boardNum)
    
        pickbTruth = True
    

        while pickbTruth == True:
            pickbPlace = int(input("\n\nO, choose the number of the position in which your piece will go: "))
            if pickbPlace < 1 and pickbPlace > 9:
                pickbTruth = True
            elif pickbPlace == 1:
                pickbrow = 0
                pickbcol = 0
            elif pickbPlace == 2:
                pickbrow = 0
                pickbcol = 1
            elif pickbPlace == 3:
                pickbrow = 0
                pickbcol = 2
            elif pickbPlace == 4:
                pickbrow = 1
                pickbcol = 0
            elif pickbPlace == 5:
                pickbrow = 1
                pickbcol = 1
            elif pickbPlace == 6:
                pickbrow = 1
                pickbcol = 2
            elif pickbPlace == 7:
                pickbrow = 2
                pickbcol = 0
            elif pickbPlace == 8:
                pickbrow = 2
                pickbcol = 1
            elif pickbPlace == 9:
                pickbrow = 2
                pickbcol = 2
    
        

            if (board[pickbrow][pickbcol] == "X") or (board[pickbrow][pickbcol] == "O"):
                print ("\nThis is already taken.\n")
            else:
                print ("\nSuccess!\n")
                board[pickbrow][pickbcol] = "O"
    
                print_board (board)

                print ("\n\n")
            
        
        
                break
        val += 1
        if (board[0][0] == "O") and (board[1][0] == "O") and (board[2][0] == "O") or (board[0][1] == "O") and (board[1][1] == "O") and (board[2][1] == "O") or (board[0][2] == "O") and (board[1][2] == "O") and (board[2][2] == "O") or (board[0][0] == "O") and (board[0][1] == "O") and (board[0][2] == "O") or (board[1][0] == "O") and (board[1][1] == "O") and (board[1][2] == "O") or (board[2][0] == "O") and (board[2][1] == "O") and (board[2][2] == "O") or (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] == "O") or (board[0][2] == "O") and (board[1][1] == "O") and (board[2][0] == "O"):
            print ("O has won! Congratulations, player O.\n\n")
            val = 9
            input ("Press enter to exit.")
    
    
elif mode == 2:
    while val < 9:
        pickaTruth = True

        while pickaTruth == True:
            print("\n\n")

            print (boardNum)
            
            pickaPlace = int(input("\n\nX, choose the number of the position in which your piece will go: "))
            if pickaPlace < 1 and pickaPlace > 9:
                pickaTruth = True
            elif pickaPlace == 1:
                pickarow = 0
                pickacol = 0
            elif pickaPlace == 2:
                pickarow = 0
                pickacol = 1
            elif pickaPlace == 3:
                pickarow = 0
                pickacol = 2
            elif pickaPlace == 4:
                pickarow = 1
                pickacol = 0
            elif pickaPlace == 5:
                pickarow = 1
                pickacol = 1
            elif pickaPlace == 6:
                pickarow = 1
                pickacol = 2
            elif pickaPlace == 7:
                pickarow = 2
                pickacol = 0
            elif pickaPlace == 8:
                pickarow = 2
                pickacol = 1
            elif pickaPlace == 9:
                pickarow = 2
                pickacol = 2
        
        

            if (board[pickarow][pickacol] == "X") or (board[pickarow][pickacol] == "O"):
                print ("\nThis is already taken.\n")
            else:
                print ("\nSuccess!\n")
                board[pickarow][pickacol] = "X"
    
                print_board (board)
                print ("\n\n")
                
                
                pickaTruth = False
            break
        val += 1
        if (board[0][0] == "X") and (board[1][0] == "X") and (board[2][0] == "X") or (board[0][1] == "X") and (board[1][1] == "X") and (board[2][1] == "X") or (board[0][2] == "X") and (board[1][2] == "X") and (board[2][2] == "X") or (board[0][0] == "X") and (board[0][1] == "X") and (board[0][2] == "X") or (board[1][0] == "X") and (board[1][1] == "X") and (board[1][2] == "X") or (board[2][0] == "X") and (board[2][1] == "X") and (board[2][2] == "X") or (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] == "X") or (board[0][2] == "X") and (board[1][1] == "X") and (board[2][0] == "X"):
            print ("X has won! Congratulations, player X.\n\n")
            val = 9
            input ("Press enter to exit.")
        

        if val == 9:
            
            break

        pickbTruth = True
        print ("It is the computer's turn!\n")

        while pickbTruth == True:
            pickbPlace = 0
            #Starting corners
            if (board[0][0] == "X"): #and (board[0][1] != "X") and (board[0][2] != "X") and (board[1][0] != "X") and (board[1][1] != "X") and (board[2][0] != "X") and (board[2][1] !="X") and (board[2][2] !="X"):
                pickbPlace = 9
            elif (board[0][2] == "X"): #and (board[0][0] != "X") and (board[0][1] != "X") and (board[1][0] != "X") and (board[1][1] != "X") and (board[0][0] != "X") and (board[2][1] !="X") and (board[2][2] !="X"):
                pickbPlace = 7
            elif (board[2][0] == "X"): #and (board[0][0] != "X") and (board[0][1] != "X") and (board[1][0] != "X") and (board[1][1] != "X") and (board[0][0] != "X") and (board[2][1] !="X") and (board[2][2] !="X"):
                pickbPlace = 3
            elif (board[2][2] == "X"): #and (board[0][0] != "X") and (board[0][1] != "X") and (board[1][0] != "X") and (board[1][1] != "X") and (board[2][0] != "X") and (board[2][1] !="X") and (board[0][0] !="X"):
                pickbPlace = 1
                                                                                                                                                                        
            #Columns
            if (board[0][0] == "O") and (board[1][0] == "O") and (board[2][0] != "X"):
                pickbPlace = 7
            elif (board[0][0] == "O") and (board[2][0] == "O") and (board[1][0] != "X"):
                pickbPlace = 4
            elif (board[1][0] == "O") and (board[2][0] == "O") and (board[0][0] != "X"):
                pickbPlace = 1
                
            elif (board[0][1] == "O") and (board[1][1] == "O") and (board[2][1] != "X"):
                pickbPlace = 8
            elif (board[0][1] == "O") and (board[2][1] == "O") and (board[1][1] != "X"):
                pickbPlace = 5
            elif (board[1][1] == "O") and (board[2][1] == "O") and (board[0][1] != "X"):
                pickbPlace = 2

            elif (board[0][2] == "O") and (board[1][2] == "O") and (board[2][2] != "X"):
                pickbPlace = 9
            elif (board[0][2] == "O") and (board[2][2] == "O") and (board[1][2] != "X"):
                pickbPlace = 6
            elif (board[1][2] == "O") and (board[2][2] == "O") and (board[0][2] != "X"):
                pickbPlace = 3

            #Rows

            elif (board[0][0] == "O") and (board[0][1] == "O") and (board[0][2] != "X"):
                pickbPlace = 3
            elif (board[0][0] == "O") and (board[0][2] == "O") and (board[0][1] != "X"):
                pickbPlace = 2
            elif (board[0][1] == "O") and (board[0][2] == "O") and (board[0][0] != "X"):
                pickbPlace = 1

            elif (board[1][0] == "O") and (board[1][1] == "O") and (board[1][2] != "X"):
                pickbPlace = 6
            elif (board[1][0] == "O") and (board[1][2] == "O") and (board[1][1] != "X"):
                pickbPlace = 5
            elif (board[1][1] == "O") and (board[1][2] == "O") and (board[1][0] != "X"):
                pickbPlace = 4

            elif (board[2][0] == "O") and (board[2][1] == "O") and (board[2][2] != "X"):
                pickbPlace = 9
            elif (board[2][0] == "O") and (board[2][2] == "O") and (board[2][1] != "X"):
                pickbPlace = 8
            elif (board[2][1] == "O") and (board[2][2] == "O") and (board[2][0] != "X"):
                pickbPlace = 7

            #Diagonals

            elif (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] != "X"):
                pickbPlace = 9
            elif (board[0][0] == "O") and (board[2][2] == "O") and (board[1][1] != "X"):
                pickbPlace = 5
            elif (board[1][1] == "O") and (board[2][2] == "O") and (board[0][0] != "X"):
                pickbPlace = 1

            elif (board[0][2] == "O") and (board[1][1] == "O") and (board[2][0] != "X"):
                pickbPlace = 7
            elif (board[0][2] == "O") and (board[2][0] == "O") and (board[1][1] != "X"):
                pickbPlace = 5
            elif (board[1][1] == "O") and (board[2][0] == "O") and (board[0][2] != "X"):
                pickbPlace = 3

            #End of choosing
            
            elif (board[0][0] == "X") and (board[1][0] == "X") and (board[2][0] != "O"):
                pickbPlace = 7
            elif (board[0][0] == "X") and (board[2][0] == "X") and (board[1][0] != "O"):
                pickbPlace = 4
            elif (board[1][0] == "X") and (board[2][0] == "X") and (board[0][0] != "O"):
                pickbPlace = 1
                
            elif (board[0][1] == "X") and (board[1][1] == "X") and (board[2][1] != "O"):
                pickbPlace = 8
            elif (board[0][1] == "X") and (board[2][1] == "X") and (board[1][1] != "O"):
                pickbPlace = 5
            elif (board[1][1] == "X") and (board[2][1] == "X") and (board[0][1] != "O"):
                pickbPlace = 2

            elif (board[0][2] == "X") and (board[1][2] == "X") and (board[2][2] != "O"):
                pickbPlace = 9
            elif (board[0][2] == "X") and (board[2][2] == "X") and (board[1][2] != "O"):
                pickbPlace = 6
            elif (board[1][2] == "X") and (board[2][2] == "X") and (board[0][2] != "O"):
                pickbPlace = 3

            #Rows

            elif (board[0][0] == "X") and (board[0][1] == "X") and (board[0][2] != "O"):
                pickbPlace = 3
            elif (board[0][0] == "X") and (board[0][2] == "X") and (board[0][1] != "O"):
                pickbPlace = 2
            elif (board[0][1] == "X") and (board[0][2] == "X") and (board[0][0] != "O"):
                pickbPlace = 1

            elif (board[1][0] == "X") and (board[1][1] == "X") and (board[1][2] != "O"):
                pickbPlace = 6
            elif (board[1][0] == "X") and (board[1][2] == "X") and (board[1][1] != "O"):
                pickbPlace = 5
            elif (board[1][1] == "X") and (board[1][2] == "X") and (board[1][0] != "O"):
                pickbPlace = 4

            elif (board[2][0] == "X") and (board[2][1] == "X") and (board[2][2] != "O"):
                pickbPlace = 9
            elif (board[2][0] == "X") and (board[2][2] == "X") and (board[2][1] != "O"):
                pickbPlace = 8
            elif (board[2][1] == "X") and (board[2][2] == "X") and (board[2][0] != "O"):
                pickbPlace = 7

            #Diagonals

            elif (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] != "O"):
                pickbPlace = 9
            elif (board[0][0] == "X") and (board[2][2] == "X") and (board[1][1] != "O"):
                pickbPlace = 5
            elif (board[1][1] == "X") and (board[2][2] == "X") and (board[0][0] != "O"):
                pickbPlace = 1

            elif (board[0][2] == "X") and (board[1][1] == "X") and (board[2][0] != "O"):
                pickbPlace = 7
            elif (board[0][2] == "X") and (board[2][0] == "X") and (board[1][1] != "O"):
                pickbPlace = 5
            elif (board[1][1] == "X") and (board[2][0] == "X") and (board[0][2] != "O"):
                pickbPlace = 3
            
            if pickbPlace == 0:
                pickbPlace = random.randint(1,9)
                
            if pickbPlace < 1 and pickbPlace > 9:
                pickbTruth = True
                
            elif pickbPlace == 1:
                pickbrow = 0
                pickbcol = 0
            elif pickbPlace == 2:
                pickbrow = 0
                pickbcol = 1
            elif pickbPlace == 3:
                pickbrow = 0
                pickbcol = 2
            elif pickbPlace == 4:
                pickbrow = 1
                pickbcol = 0
            elif pickbPlace == 5:
                pickbrow = 1
                pickbcol = 1
            elif pickbPlace == 6:
                pickbrow = 1
                pickbcol = 2
            elif pickbPlace == 7:
                pickbrow = 2
                pickbcol = 0
            elif pickbPlace == 8:
                pickbrow = 2
                pickbcol = 1
            elif pickbPlace == 9:
                pickbrow = 2
                pickbcol = 2
    
        
            fixed = False
            while fixed == False:
                if (board[pickbrow][pickbcol] == "X") or (board[pickbrow][pickbcol] == "O"):
                    print ("\nThe computer is thinking too much.\n")
                    pickbrow = random.randint(0,2)
                    pickbcol = random.randint(0,2)
                else:
                    fixed = True
                
            #else:
            print ("\nSuccess!\n")
            board[pickbrow][pickbcol] = "O"
    
            print_board (board)

            print ("\n\n")

            pickbTruth = False

            break
        val += 1
        if (board[0][0] == "O") and (board[1][0] == "O") and (board[2][0] == "O") or (board[0][1] == "O") and (board[1][1] == "O") and (board[2][1] == "O") or (board[0][2] == "O") and (board[1][2] == "O") and (board[2][2] == "O") or (board[0][0] == "O") and (board[0][1] == "O") and (board[0][2] == "O") or (board[1][0] == "O") and (board[1][1] == "O") and (board[1][2] == "O") or (board[2][0] == "O") and (board[2][1] == "O") and (board[2][2] == "O") or (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] == "O") or (board[0][2] == "O") and (board[1][1] == "O") and (board[2][0] == "O"):
            print ("The computer has won! Unlucky, player X.\n\n")
            val = 9
            input ("Press enter to exit.")
else:
    print ("\n\nYou've done something very stupid. I think it is time to leave.\n")
    input ("Press enter to exit.")
