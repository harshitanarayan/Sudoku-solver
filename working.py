# Game Board 
board = [
    [0, 0, 1, 0, 3, 0, 0, 2, 6],
    [0, 0, 0, 8, 1, 0, 7, 9, 0],
    [0, 4, 0, 7, 0, 0, 0, 0, 0],
    [1, 2, 4, 5, 0, 6, 3, 7, 0],
    [0, 8, 0, 2, 0, 9, 0, 0, 0],
    [7, 0, 9, 1, 0, 3, 8, 5, 2],
    [0, 0, 0, 0, 2, 0, 6, 0, 0],
    [6, 0, 7, 3, 0, 0, 0, 0, 0],
    [4, 3, 0, 0, 0, 0, 0, 8, 7]
]

def solve(board):
    # BASE CASE 
    empty_pos = findEmpty(board)
    #if empty, execute if 
    #if not empty_pos, we have found the sol, so return true 
    if not empty_pos:
        return True
    else:
        row, col =  empty_pos
    
    for i in range(1, 10):
        if isValidInput(board, i, (row,col)):
            board[row][col] = i

            #Recusrively solve the board with i as the input 
            if solve(board):
                return True
            
            board[row][col] = 0
    return False

#Check if the input in row, column and 3x3 box is valid or not         
def isValidInput(board, inputNum, pos):

    #Check row for duplicate number
    for i in range(len(board[0])):
        #if inputNum is already present in the row, its an invalid input
        # board[pos[0]][i] == inputNum => Iterates through the row and checks if the inputNum is already present 
        # pos[1] != i => checks if the position is where we just inserted the inputNum and if so then ignore that position 
        if board[pos[0]][i] == inputNum and pos[1] != i:
            return False 
    
    #Check column for duplicate number 
    for i in range(len(board)):
        if board[i][pos[1]] == inputNum and pos[0] != i:
            return False

    #Check 3x3 box for duplicate number 
    #Checks which 3x3 box we are in 
    pos_x = pos[1] // 3
    pos_y = pos[0] // 3

    #pos_y*3 => (0, 1, 2) * 3 to get to the actual index number of the position
    #pos_y*3 + 3 => To iterate to next 3 index to check validity within the box
    for i in range(pos_y*3, pos_y*3 + 3):
        for j in range(pos_x*3, pos_x*3 + 3):
            if board[i][j] == inputNum and (i,j) != pos:
                return False
    
    return True
     

#Print board
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            # if at the end, go to the next line 
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="") #end="" => stay on the same line 

# Find and return an empty space 
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # returning row, col i.e. y,x

    return None

printBoard(board)
solve(board)
print('----------------------Solution-------------------------')
printBoard(board)

