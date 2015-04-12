gameagain = True
choice = 0
pure = ''
count = 0
gameagain = True
playerx = 0
playero = 0
def printboard(board):
    print '''
     %s | %s | %s 
    -----------
     %s | %s | %s 
    -----------
     %s | %s | %s
    ''' % (board[0],board[1],board[2],\
            board[3],board[4],board[5],\
            board[6],board[7],board[8])
def example():
    print '''
     0 | 1 | 2 
    -----------
     3 | 4 | 5 
    -----------
     6 | 7 | 8
    '''
def playerchoose():
    while True:
        pure = input('Pick a square, any square...')
        if pure > 8:
            example()
            continue
        if board[pure] != ' ':
            print 'That has already been picked'
            printboard(board)
        else:
            board[pure] = 'O'
            break
    return pure
def f(x):
    board[x] = 'X'
    printboard(board)
def result(board):
    #top horiz
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or\
       (board[0] == 'O' and board[1] == 'O' and board[2] == 'O'):
        return True
    #mid horiz
    elif (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or\
         (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'):
        return True
    #low horiz
    elif (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or\
         (board[6] == 'O' and board[7] == 'O' and board[8] == 'O'):
        return True
    
    #left vert
    elif (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or\
         (board[0] == 'O' and board[3] == 'O' and board[6] == 'O'):
        return True
    #mid vert
    elif (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or\
         (board[1] == 'O' and board[4] == 'O' and board[7] == 'O'):
        return True
    #right vert
    elif (board[2] == 'X' and board[5]  == 'X'and board[8] == 'X') or\
         (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        return True
    
    #left-right diag
    elif (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or\
         (board[0] == 'O' and board[4] == 'O' and board[8] == 'O'):
        return True
    #right-left diag
    elif (board[2] == 'X' and board[4] == 'X' and board[6] == 'X') or\
         (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        return True
    
    else:
        return False
def newboard():
	global board
	board = []
	for i in range(0,9):
	    board.append(' ')

example()
while gameagain:
	newboard()
	f(0)
	a = playerchoose()
	if a == 1:
	    f(4)
	    a = playerchoose()
	    if a == 2:
	        f(8)
	    elif a == 3:
	        f(8)
	    elif a == 5:
	        f(8)
	    elif a == 6:
	        f(8)
	    elif a == 7:
	        f(8)
	    elif a == 8:
	        f(6)
	        a = playerchoose()
	        if a == 2:
	            f(3)
	        elif a == 3:
	            f(2)
	        elif a == 5:
	            f(3)
	        elif a == 7:
	            f(3)
	elif a == 2:
	    f(6)
	    a = playerchoose()
	    if a == 1:
	        f(3)
	    elif a == 3:
	        f(8)
	        a = playerchoose()
	        if a == 1:
	            f(7)
	        elif a == 4:
	            f(7)
	        elif a == 5:
	            f(7)
	        elif a == 7:
	            f(4)
	    elif a == 4:
	        f(3)
	    elif a == 5:
	        f(3)
	    elif a == 7:
	        f(3)
	    elif a == 8:
	        f(3)
	elif a == 3:
	    f(4)
	    a = playerchoose()
	    if a == 1:
	        f(8)
	    elif a == 2:
	        f(8)
	    elif a == 5:
	        f(8)
	    elif a == 6:
	        f(8)
	    elif a == 7:
	        f(8)
	    elif a == 8:
	        f(2)
	        a = playerchoose()
	        if a == 2:
	            f(6)
	        elif a == 5:
	            f(2)
	        elif a == 6:
	            f(2)
	        elif a == 7:
	            f(2)
	elif a == 4:
	    f(8)
	    a = playerchoose()
	    if a == 1:
	        f(7)
	        a = playerchoose()
	        if a == 2:
	            f(6)
	        elif a == 3:
	            f(6)
	        elif a == 5:
	            f(6)
	        elif a == 6:
	            f(2)
	            a = playerchoose()
	            if a == 3:
	                f(5)
	            elif a == 5:
	                f(3) #tie
	    elif a == 2:
	        f(6)
	        a = playerchoose()
	        if a == 1:
	            f(3)
	        elif a == 3:
	            f(7)
	        elif a == 5:
	            f(7)
	        elif a == 7:
	            f(3)
	    elif a == 3:
	        f(5)
	        a = playerchoose()
	        if a == 1:
	            f(2)
	        elif a == 2:
	            f(6)
	            a = playerchoose()
	            if a == 1:
	                f(7)
	            elif a == 7:
	                f(1) #tie
	        elif a == 6:
	            f(2)
	        elif a == 7:
	            f(2)
	    elif a == 5:
	        f(3)
	        a = playerchoose()
	        if a == 1:
	            f(6)
	        elif a == 2:
	            f(6)
	        elif a == 6:
	            f(2)
	            a = playerchoose()
	            if a == 1:
	                f(7) #tie
	            elif a == 7:
	                f(1)
	        elif a == 7:
	            f(6)
	    elif a == 6:
	        f(2)
	        a = playerchoose()
	        if a == 1:
	            f(5)
	        elif a == 3:
	            f(1)
	        elif a == 5:
	            f(1)
	        elif a == 7:
	            f(5)
	    elif a == 7:
	        f(1)
	        a = playerchoose()
	        if a == 2:
	            f(6)
	            a = playerchoose()
	            if a == 3:
	                f(5) #tie
	            if a == 5:
	                f(3)
	        elif a == 3:
	            f(2)
	        elif a == 5:
	            f(2)
	        elif a == 6:
	            f(2)
	elif a == 5:
	    f(4)
	    a = playerchoose()
	    if a == 1:
	       	f(8)
	    elif a == 2:
	        f(8)
	    elif a == 3:
	        f(8)
	    elif a == 6:
	        f(8)
	    elif a == 7:
	    	f(8)	
	    elif a == 8:
	    	f(2)
	    	a = playerchoose()
	    	if a == 1:
	        	f(6)
	        elif a == 3:
	            f(1)
	        elif a == 6:
	            f(1)
	        elif a == 7:
	            f(1)
	elif a == 6:
	    f(2)
	    a = playerchoose()
	    if a == 1:
	        f(8)
	        a = playerchoose()
	        if a == 3:
	            f(5)
	        elif a == 4:
	            f(5)
	        elif a == 5:
	            f(4)
	        elif a == 7:
	            f(5)
	    elif a == 3:
	        f(1)
	    elif a == 4:
	        f(1)
	    elif a == 5:
	        f(1)
	    elif a == 7:
	        f(1)
	    elif a == 8:
	        f(1)
	elif a == 7:
	    f(4)
	    a = playerchoose()
	    if a == 1:
	        f(8)
	    elif a == 2:
	        f(8)
	    elif a == 3:
	        f(8)
	    elif a == 5:
	        f(8)
	    elif a == 6:
	        f(8)
	    elif a == 8:
	        f(6)
	        a = playerchoose()
	        if a == 1:
	            f(3)
	        elif a == 2:
	            f(3)
	        elif a == 3:
	            f(2)
	        elif a == 5:
	            f(3)
	elif a == 8:
	    f(2)
	    a = playerchoose()
	    if a == 1:
	        f(6)
	        a = playerchoose()
	        if a == 3:
	            f(4)
	        elif a == 4:
	            f(3)
	        elif a == 5:
	            f(3)
	        elif a == 7:
	            f(3)
	    elif a == 3:
	        f(1)
	    elif a == 4:
	        f(1)
	    elif a == 5:
	        f(1)
	    elif a == 6:
	        f(1)
	    elif a == 7:
	        f(1)

	if result(board) == True:
		print 'Computer Wins!'
		gameagain = input('Play again (0/1)? ')
	else:
		print 'Tie game!'
		gameagain = input('Play again (0/1)? ')

raw_input()
