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

# Write a player_move function that accepts a string with the game board, 
# asks the player which position he wants to play and returns the updated game board with the player's move. 
# The function should reject negative or too large numbers or 
# moves to an occupied position. 
# If the user has entered a wrong argument, the function should ask again (to get correct answer).

def player_move (string):
    while (True):
        position_number = int(input("Make your move!\n Tell me where to put your x (number beweteen 1 and 20): "))
        if (position_number >= 1) & (position_number <= 20):
            player_position = string[(position_number - 1): position_number]
            if player_position == '-':
                return move(string, position_number, 'x')
            else:
                print("Someone has been here before!")
        else: 
            print("I can't work with that! * dramatic gesture *") 
