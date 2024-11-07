# Write a function evaluate that accepts the string with the board of 1D tic-tac-toe 
# as argument and returns one character based on the state of the game:

# "x" – The player who uses crosses (Xs) has won (the board contains xxx)
# "o" – The player who uses noughts (Os) has won (the board contains ooo)
#"!" – Draw (the board is full but nobody has won)
# "-" – Rest (i.e. the game is not finished)
from random import randrange

def evaluate (string):
    crosses = "xxx"
    noughts = "ooo"
    full = "-"
    if crosses in string: 
        return "x"
    elif noughts in string:
        return "o"
    elif full not in string:        # draw
        return "!"
    else:
        return "-"

# Write a move function that accepts the string with the game board, a position number (0-19) and a (x or o) mark 
# and returns a game board  (i.e., a string with the given mark placed in the given position). 

def move (string, position_number, character):
    part_a = string[:position_number]
    part_b = string[position_number + 1:]
    board_update = part_a + character + part_b
    return board_update

# Write a player_move function that accepts a string with the game board, 
# asks the player which position he wants to play and returns the updated game board with the player's move. 
# The function should reject negative or too large numbers or 
# moves to an occupied position. 
# If the user has entered a wrong argument, the function should ask again (to get correct answer).

def player_move (string):
    while (True):
        position_number = int(input("Make your move!\n Tell me where to put your x (number beweteen 1 and 20): ")) - 1
        if 0 <= position_number < 20:
            if string [position_number] == '-':
                return move(string, position_number, 'x')
            else:
                print("Someone has been here before!")
        else: 
            print("I can't work with that! * dramatic gesture *") 

# Write a pc_move function that accepts the string with the game board. It will select a position to play, and returns the game board with the computer's move.
# Use a simple random "strategy":

# Select a random number from 0 to 19.
# If the position is empty, place the computer's mark there.
# If not, repeat from the first step (select another random number). The function header should look something like this:


def pc_move (string):
    while (True):
        pc_choice = randrange (0,20)
        if string[pc_choice] == '-':
            return move(string, pc_choice, 'o')

# Write a tictactoe_1d function that creates a string with a game board and alternately calls the player_move and pc_move functions
# until someone wins or draws. Do not forget to check the status of the game after every turn.

def tictactoe ():
    board = "--------------------"
    turn = "player"

    while (True):
        print("\nCurrent board", board)
        if turn == "player":
            board = player_move(board)
            turn = "pc"
        else:
            board = pc_move(board)
            turn = "player"
        
        result = evaluate(board)
        if result != "-": 
            print("\nFinal board:", board)
            if result == "x":
                print("Player wins!")
            elif result == "o":
                print("PC wins!")
            elif result == "!":
                print("Draw!")
            break
    return board


tictactoe()