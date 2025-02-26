# Tic-tac-toe.py
import random

# Initialize board
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check if someone has won
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full
def is_draw():
    return " " not in board

# Function to make a move
def make_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

# Main game loop
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    display_board()

    current_player = "X"

    while True:
        make_move(current_player)
        display_board()

        if check_winner(current_player):
            print(f"🎉 Player {current_player} wins! 🎉")
            break
        elif is_draw():
            print("It's a draw! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
