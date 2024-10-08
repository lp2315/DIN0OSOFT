import tkinter as tk
from tkinter import *
import keyboard
import datetime as dt


# ask strings

help_message = "HELP TEXT"
info_message = "WELCOME TO FOSSIL CONSOLE"
error_message = "NO SUCH COMMAND..."


# root

root = tk.Tk()
root.title("FOSSIL Terminal")
root.geometry("700x250+15+15")
root.resizable(False, False)
root.iconbitmap("foss_1.ico")


# top label

logo = tk.PhotoImage(file = "foss_small.png")
tk.Label(root, image = logo, text = 'FOSSIL', font = ("Terminal", 14), compound = 'top').pack()


# text widget plus colors of input text

console = (tk.Text(root, height = 10, bg = "black", fg = "white"))
console.pack(padx = 1, pady = 1)

console.tag_config("ask", foreground = "green")
console.tag_config("system", foreground = "yellow")


# entry widget

lastcommand = StringVar()
input_bar = tk.Entry(root, font = ("Courier New Italic", 12), textvariable = lastcommand, width = 55)

input_bar.pack(padx = 1, pady = 1, side = "left")
input_bar.focus()


# functions

def send():
    timestamp = dt.datetime.now()
    msg = str(input_bar.get())
    console.insert("-1.0", str(timestamp.strftime('%H:%M - ') + msg + "\n"))
    input_bar.delete(0, END)


def ask():
    timestamp = dt.datetime.now()
    msg = str(input_bar.get())
    console.insert("-1.0", str(timestamp.strftime('%H:%M - ') + msg + "\n"), "ask")
    if msg == "help":
        console.insert("-1.0", "> " + help_message + "\n", "system")
    elif msg == "info":
        console.insert("-1.0", "> " + info_message + "\n", "system")
    else:
        console.insert("-1.0", "> " + error_message + "\n", "system")
    input_bar.delete(0, END)


# buttons

tk.Button(root, bg = "blue", fg = "white", text = "!", font = ("Courier New", 12), command = send).pack(
    padx = 1, pady = 1, side = "right")
tk.Button(root, bg = "green", fg = "white", text = "?", font = ("Courier New", 12), command = ask).pack(
    padx = 1, pady = 1, side = "right")


# hotkeys

keyboard.add_hotkey('shift+enter', ask)
keyboard.add_hotkey('enter', send)

console.insert("-1.0", "> " + info_message + "\n", "system")

#

if __name__ == "__main__":
    root.mainloop()
