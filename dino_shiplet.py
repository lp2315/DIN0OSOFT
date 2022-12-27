import turtle
import tkinter as tk
import random as rand
import time


# Basic turtle on drawing board,
# with controls


scaling = 5

# drawing board
App = tk.Tk()
canv = tk.Canvas(App,
                 width = 100 * scaling, height = 100 * scaling,
                 cursor = "cross")
canv.pack()

# turtle
screen = turtle.TurtleScreen(canv)

t = turtle.RawTurtle(screen)
t.pensize(1.5)
t.showturtle()


def hover():
    t.up()


tk.Button(App, text = "↑", command = hover).pack(side = tk.LEFT)
App.bind("e", lambda event: hover())


def land():
    t.down()


tk.Button(App, text = "↓", command = land).pack(side = tk.LEFT)
App.bind("<Shift-e>", lambda event: land())

# screen

screen.bgcolor("black")
screen.onclick(t.goto)


def erase():
    t.clear()


App.bind("<Control-n>", lambda event: erase())


def spawn_object():
    x = input("How many objects?")  # amount
    x = int(x)

    for i in range(x):
        teleport()
        t.shape("circle")  # object
        t.color("red")
        stamp()

    t.shape("classic")

    print(str(x) + " enemies spawned")


App.bind("p", lambda event: spawn_enemy())


# color randomizer

def penerate():
    x = rand.randrange(0, 16777215, 1)
    x = str((hex(x))[2:])
    x = "#" + ('{:<06}'.format(x))
    t.color(x)


penerate()

tk.Button(App, text = "Pen", command = penerate, bg = "red").pack(side = tk.LEFT)
App.bind("<Shift-C>", lambda event: penerate())


# movement

def forward():
    t.fd(1 * scaling)


tk.Button(App, text = "+", command = forward).pack(side = tk.LEFT)
App.bind("w", lambda event: forward())


def back():
    t.bk(1 * scaling)


tk.Button(App, text = "-", command = back).pack(side = tk.LEFT)
App.bind("s", lambda event: back())


def jump():
    t.penup()
    t.forward(5 * scaling)
    t.pendown()


tk.Button(App, text = "J", command = jump).pack(side = tk.LEFT)
App.bind("<space>", lambda event: jump())


def left():
    t.left(90)


tk.Button(App, text = "L", command = left).pack(side = tk.LEFT)
App.bind("a", lambda event: left())


def right():
    t.right(90)


tk.Button(App, text = "R", command = right).pack(side = tk.LEFT)
App.bind("d", lambda event: right())


def flip():
    t.right(180)


tk.Button(App, text = "180", command = flip).pack(side = tk.LEFT)
App.bind("q", lambda event: flip())


# operations

def stamp():
    t.stamp()


tk.Button(App, text = "X", command = stamp).pack(side = tk.LEFT)
App.bind("x", lambda event: stamp())


def undo():
    t.undo()


tk.Button(App, text = "Undo", command = undo).pack(side = tk.LEFT)
App.bind("<Control-z>", lambda event: undo())


def teleport():
    t.up()
    x = rand.randrange(0, 200, 1)
    y = rand.randrange(0, 200, 1)
    t.goto(x, y)
    t.down()


tk.Button(App, text = "TP", command = teleport).pack(side = tk.LEFT)
App.bind("t", lambda event: teleport())


# loop

App.mainloop()
