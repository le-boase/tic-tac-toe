# main.py

import tkinter as tk
from user_interface import create_buttons
from tic_tac_toe import initialize_board, reset_game

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    board, current_player = reset_game()
    buttons = [[None for _ in range(3)] for _ in range(3)]
    create_buttons(root, board, current_player, buttons)
    root.mainloop()