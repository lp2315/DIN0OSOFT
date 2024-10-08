import pyglet as pyg
import pyglet.shapes
from pyglet.gl import *
from pyglet.window import key
import random
import numpy as np
import ctypes
from pyglet.window.key import MOD_SHIFT
# config
from constants import *


# pyglet
GAME = pyg.window.Window(
    W, H,
    caption = "game"
)

# scroll lock toggling
user32 = ctypes.WinDLL('user32')

# cursor
GAME_CURSOR = GAME.get_system_mouse_cursor(GAME.CURSOR_CROSSHAIR)
GAME.set_mouse_cursor(GAME_CURSOR)
# graphics and openGL ?
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
TILE_BATCH = pyg.graphics.Batch()


# general functions
def shuffle_color():
    return list(COLORS.values())[random.randrange(0, len(COLORS), 1)]


# tilemap class and methods
class TileMap:

    ### for each column, on each row, create a rectangle, assign to np array
    def __init__(self, columns = COLS, rows = ROWS):
        self.generation = int()
        self.total_tiles = int(COLS * ROWS)
        self.total_area = self.total_tiles * TILE_SIZE

        self.current = np.zeros((COLS, ROWS), dtype = pyglet.shapes.Rectangle)
        self.next = np.zeros((COLS, ROWS), dtype = pyglet.shapes.Rectangle)

        for r in range(0, ROWS, 1):

            for c in range(0, COLS, 1):
                t = pyglet.shapes.Rectangle(
                    r * TILE_SIZE, c * TILE_SIZE,
                    TILE_SIZE, TILE_SIZE,
                    batch = TILE_BATCH
                )
                t.color = shuffle_color()

                self.current[r, c] = t

    ### changing all tiles
    def change_all(self, color):
        for r in range(0, COLS, 1):

            for c in range(0, ROWS, 1):
                self.current[r, c].color = color

            if (c * ROWS) == W:
                c = 0
                r += 1

    def shuffle_all(self):
        for r in range(0, COLS, 1):
            for c in range(0, ROWS, 1):
                self.current[r, c].color = shuffle_color()

    ### change tile at y,x into color
    def set_tile(self, y, x, color):
        try:
            t = self.current[y // TILE_SIZE, x // TILE_SIZE]
            if t.color != color:
                t.color = color
                return t.draw()
        ### does nothing if mouse out of range
        except IndexError:
            pass

    ### the automation
    def automate(self):

        # next array becomes a copy of current
        self.next = self.current.copy()

        for y in range(COLS):

            for x in range(ROWS):

                t_focus = self.current[y, x]

                t_cross = get_cross(self.current, y, x)

                t_criss = get_criss(self.current, y, x)

                ### what each color does

                # white and black blinking
                if t_focus.color == COLORS['WHITE']:
                    self.next[y, x].color = COLORS['BLACK']

                elif t_focus.color == COLORS['BLACK']:
                    self.next[y, x].color = COLORS['WHITE']

        # buffer swap
        self.current, self.next = self.next, self.current

    ### performs automation if scroll lock is toggled on
    def scroll_lock_toggler(self):
        if user32.GetKeyState(0x91):
            self.automate()
            self.generation += 1  # increments generation
            GAME.set_caption(str(self.generation))


# constructor
Board = TileMap()

# clock
c = pyg.clock.get_default()  # grabs pyglets clock


def update(dt):  # every FPS second, perform these things, dt is time since last frame
    c.tick()  # every FPS, tick the clock

    Board.scroll_lock_toggler()


# events
@GAME.event
def on_draw():
    GAME.clear()
    TILE_BATCH.draw()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


# mouse input
@GAME.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyg.window.mouse.LEFT:
        Board.set_tile(x, y, COLORS['AQUA'])

    if button == pyg.window.mouse.LEFT and modifiers & MOD_SHIFT:
        Board.set_tile(x, y, COLORS['BLUE'])

    if button == pyg.window.mouse.RIGHT:
        Board.set_tile(x, y, COLORS['PERU'])

    if button == pyg.window.mouse.RIGHT and modifiers & MOD_SHIFT:
        Board.set_tile(x, y, COLORS['WHITE'])


@GAME.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons == pyg.window.mouse.LEFT:
        Board.set_tile(x, y, COLORS['AQUA'])

    if buttons == pyg.window.mouse.LEFT and modifiers & MOD_SHIFT:
        Board.set_tile(x, y, COLORS['BLUE'])

    if buttons == pyg.window.mouse.RIGHT:
        Board.set_tile(x, y, COLORS['PERU'])

    if buttons == pyg.window.mouse.RIGHT and modifiers & MOD_SHIFT:
        Board.set_tile(x, y, COLORS['WHITE'])


# key input
@GAME.event
def on_key_press(symbol, modifiers):
    if symbol == key.T:
        ### Test ###
        print("123")
        pass

    if symbol == key.H:
        print(HELP_TEXT)

    if symbol == key.R:
        Board.shuffle_all()

    if symbol == key.C:
        Board.change_all(COLORS['WHITE'])

    # shift plus X to exit
    if symbol == key.X and modifiers & MOD_SHIFT:
        pyg.app.exit()


# print help
print(HELP_TEXT)

# loop and refresh rate
if __name__ == "__main__":
    c.schedule_interval(update, FPS)
    pyg.app.run()
