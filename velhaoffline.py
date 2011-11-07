# PyTicTacToe
# 2007 by Patrick O'Brien
# [url="http://www.obtown.com"]http://www.obtown.com[/url]


# Load the board
board = " 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9"

# Set the winning combinations. Paired off in threes
# For example: 123 is a winning combo. So is 147. 
checkboard=[1,2,3,4,5,6,7,8,9,1,4,7,2,5,8,3,6,9,1,5,9,3,5,7]


# Set Space Holder
spaces=range(1,10)

# movehandler function

# This function takes the players choice and makes sure it 
# has not been used. If not, set the move. 

def moveHandler(board,spaces,checkboard,player,n):
        # set X for player one, or O for player 2
        if player==1:
                check="X"
        else:   
                check="O"
        # Check if block is used.
        while spaces.count(n)==0:
                print "\nInvalid Space"
                n=playerinput(player)
                
        # Remove block from spaces array
        spaces=spaces.remove(n)

        # Replace block with check mark in board
        board=board.replace(str(n),check)

        # Replace space with check mark in checkboard array
        for c in range(len(checkboard)):
                if checkboard[c]==n:
                        checkboard[c]=check

        # Run the checkwinner function
        status = checkwinner(checkboard,check)
        return board,status


# Checkwinner function

# This function checks whether or not a player has a winning
# combination based on the checkboard array.

def checkwinner(checkboard,check):
        # Set the array element variables
        a,b,c=0,1,2

        #Loop through checkboard to check winner
        while a<=21:
                combo = [checkboard[a],checkboard[b],checkboard[c]]

                # If we have three 'X' or 'O' we have a winner
                if combo.count(check) == 3:
                        status =1
                        break
                else:
                        status =0

                # Iterate to the next combo
                a+=3
                b+=3
                c+=3

        # Return status of the game
        return status

# 
def  playerinput(player):
        try:
                key = int(raw_input('\n\nPlayer ' + str(player) + ': Please select a space '))
        except ValueError:
                print "Invalid Space"
                key = playerinput(player)
        
        return key
                
        
                
        
        

#Start Game
while True:
        player = len(spaces)%2 +1
        if player == 1:
                player = 2
        else:
                player =1
        
        print "\n\n" + board
        key = playerinput(player)
        board,status =moveHandler(board,spaces,checkboard,player,key)
        
        if status == 1:
                print '\n\nPlayer ' + str(player) + ' is the winner!!!'
                print board
                break
        elif len(spaces)==0:
                print "No more spaces left. Game ends in a TIE!!!"
                print board
                break
        else:
                continue
