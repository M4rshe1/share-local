import tkinter as tk
from tkinter import filedialog
import os


def select_folder():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory(title="Select a folder", initialdir=f"/users/{os.getlogin()}/Downloads")
    if path == "":
        print("No file selected")
        exit()
    else:
        return path



