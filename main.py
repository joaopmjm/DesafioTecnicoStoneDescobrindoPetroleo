from utils.classes import ship, grid
from utils.funcoes import readCommands
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
g =grid()
commands = readCommands(file_path)
g.mount(commands, g)
with open("output.txt","w") as f:
    f.write(g.getShips())