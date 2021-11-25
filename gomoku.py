import os, string
columns = string.ascii_uppercase[:15]

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
    for letter in columns:
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
    column = coords[0].upper()
    row = int(coords[1:]) - 1
    for count, letter in enumerate(columns):
        if column == letter:
            column = count
            break
    index = row * 15 + column
    print("index: ", index)
    return index

def get_winning_positions():
    winning_positions = []

    # rows    
    for row in range(15):
        for square in range(11):
            position = []
            for i in range(5):
                position.append(row*15+square+i)
            winning_positions.append(position)


    # columns
    for column in range(15):
        for square in range(11):
            position = []
            for i in range(5):
                position.append(column+square*15+i*15)
            winning_positions.append(position)

    # top left diagonal
    for row in range(11):
        for square in range(11):
            position = []
            for i in range(5):
                position.append(row*15+square+i*16)
            winning_positions.append(position)

    # bottom right diagonal
    for row in range(4,15):
        for square in range(11):
            position = []
            for i in range(5):
                position.append(row*15+square-i*14)
            winning_positions.append(position)
    
    
    return winning_positions

def check_state(board):
    winning_positions = get_winning_positions()
    for player in ["X", "Y"]:
        for position in winning_positions:
            if player == board[position[0]] == board[position[1]] == \
                board[position[2]] == board[position[3]] == \
                    board[position[4]]:

                    return player
    return False




def player_turn(board):
    pass



board = board_init()
while True:
    draw_board(board)
    if check_state(board) == "X":
        print("Hrac X vyhral!")
        input()
        break

    player_move = input("Kam chces hrat? ")
    board[coords_to_index(player_move)] = "X"


