'''
Solo Checkpoint 02
Author: Bro. Hayes
'''

def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    # assign/get the first player
    player = "x"
    # create a board
    board = create_board()
    # loop if there isn't a winner or if the game isn't a draw
    end = False
    while end == False:

        # display the board
        display_board(board)

        # allow the player to make a move
        move = make_move(player, board)

        end = is_winner(board)
        
        if end == False:
            end = is_draw(board)

        # pick the next player
        player = next_player(player)

    # display the final board
    display_board(board)
    # show message for winner and thanks for playing
    print("Good game! Thanks for playing!")

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = []
    for tile in range(9):
        board.append(tile + 1)
    return board
    

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}\n")
        
    
def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''

    

    return False


def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''

    verify = board.copy()
    for i in board:
        if (i == "x") or (i == "o"):
            verify.remove(i)
    
    if len(verify) == 0:
        print(verify)
        return True
    else:
        return False
    

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    try:
        move = int(input(f"Player {player}, select your space: "))
        if move not in board:
            raise ValueError
        else:
            board[move - 1] = player
    except ValueError:
        print("Invalid move. Try again.")
        make_move(player, board)
    

def next_player(current):
    ''' return: x if current is o, otherwise x '''
    if current == "o":
        return "x"
    else:
        return "o"

# run main if this has been called from the command line
if __name__ == "__main__":
    main()