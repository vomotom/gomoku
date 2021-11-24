import os, string

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def board_init():
    board = [" " for i in range(15**2)]
    return board

def draw_board(board):
    clearConsole()
    board_string = "  "
    horizontal_line = "   " + 15 * " ---"
    for letter in string.ascii_uppercase[:15]:
        board_string += "   " + letter
    board_string += "\n" + horizontal_line + "\n"
    square_counter = 0
    for row in range(15):
        if row < 9:
            board_string += " "
        board_string += str(row + 1) + " |"
        for column in range(15):
            board_string += " " + board[square_counter] + " |"
            square_counter += 1
        board_string += "\n" + horizontal_line + "\n"

    print(board_string)

def coords_to_index(coords):
    pass

def player_turn(board):
    pass


board = board_init()
draw_board(board)