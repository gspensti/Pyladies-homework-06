# Write a function evaluate that accepts the string with the board of 1D tic-tac-toe 
# as argument and returns one character based on the state of the game:

# "x" – The player who uses crosses (Xs) has won (the board contains xxx)
# "o" – The player who uses noughts (Os) has won (the board contains ooo)
#"!" – Draw (the board is full but nobody has won)
# "-" – Rest (i.e. the game is not finished)


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
    part_a = string[:(position_number - 1)]
    part_b = string[position_number:]
    board_update = part_a + character + part_b
    return (board_update)

#def player_move (string, [], x,o)