# main.py

import tkinter as tk
from user_interface import TicTacToeGUI

if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()