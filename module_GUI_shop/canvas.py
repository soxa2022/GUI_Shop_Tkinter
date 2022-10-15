from os.path import sep
from tkinter import *

path = "." + sep + 'db' + sep + 'images' + sep


def create_app():
    roots = Tk()
    roots.geometry("800x800")
    roots.resizable(False, False)
    roots.title('GUI Product shop')
    roots.iconbitmap(default=path + 'logo_.ico')
    return roots


def create_frame():
    frames = Canvas(root, width=800, height=800)
    frames.grid(row=0, column=0)
    return frames


root = create_app()
frame = create_frame()
