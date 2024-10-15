import pyglet
from pyglet import shapes
from pyglet.text import Label
import numpy as np
from pyglet.window import key
import ctypes
from pyglet.window.key import MOD_SHIFT
import config_window
from color_rules import *

# config window loop
if __name__ == "__main__":
    slider_values = config_window.main()
    print(f"Slider values: {slider_values}")
# passes on slider values 1-4
rows_value = slider_values[0]
cols_value = slider_values[1]
scale_factor = slider_values[2]
update_speed = slider_values[3]
# derived values
window_width = cols_value * scale_factor
window_height = rows_value * scale_factor
# generation & tile batch creation
generation_counter = 0
batch = pyglet.graphics.Batch()


# grid constructor
def create_empty_grid(rows, columns):
    return np.empty((rows, columns), dtype = object)


# scroll lock check
def scroll_lock_is_active():
    return ctypes.windll.user32.GetKeyState(0x91) & 0x0001 != 0


# construct grid based on previous sliders
grid = create_empty_grid(rows_value, cols_value)

# construct a window based on sliders and scaling
window = pyglet.window.Window(
    window_width, window_height, caption = f'{generation_counter}')
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Populate the grid with rectangles and labels, put in batch
for i in range(rows_value):
    for j in range(cols_value):
        x = j * scale_factor
        y = window_height - (i + 1) * scale_factor  # Adjust y to start from the top
        grid[i, j] = {
            'rectangle': shapes.Rectangle(x, y, scale_factor, scale_factor, color = COLORS['BLUE'], batch = batch),
            'label': Label(f'({i},{j})', x = x + scale_factor // 2, y = y + scale_factor // 2,
                           anchor_x = 'center', anchor_y = 'center', batch = batch)
        }


# draw the batch
@window.event
def on_draw():
    window.clear()
    batch.draw()


# change a tile next frame depending on which color it is
def automate():
    global grid
    # copy current grid
    next_grid = grid.copy()
    color_rules = {
        COLORS['BLUE']: lambda y, x: handle_blue(y, x, grid, next_grid, COLORS),
        COLORS['RED']: lambda y, x: handle_red(y, x, grid, next_grid, COLORS),
        COLORS['ORANGE']: lambda y, x: handle_orange(y, x, grid, next_grid, COLORS),
        COLORS['GREEN_1']: lambda y, x: handle_green_1(y, x, grid, next_grid, COLORS),
        COLORS['GREEN_2']: lambda y, x: handle_green_2(y, x, grid, next_grid, COLORS),
        COLORS['GREEN_3']: lambda y, x: handle_green_3(y, x, grid, next_grid, COLORS),
        COLORS['DARK_BROWN']: lambda y, x: handle_dbrown(y, x, grid, next_grid, COLORS)
    }
    for x in range(cols_value):
        for y in range(rows_value - 1, -1, -1):
            # access tile at (y, x)
            t_focus = grid[y, x]
            current_color = t_focus['rectangle'].color
            # what each color does
            if current_color == COLORS['WHITE']:
                pass
            if current_color in color_rules:
                try:
                    color_rules[current_color](y, x)
                except IndexError:
                    pass

    grid = next_grid  # Update the original grid only after processing all tiles
    return grid


# randomize random tile color
def randomize_tile():
    row = random.randint(0, rows_value - 1)
    col = random.randint(0, cols_value - 1)
    new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    grid[row, col]['rectangle'].color = new_color


def randomize_all():
    for i in range(rows_value):
        for j in range(cols_value):
            new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            x = j * scale_factor
            y = window_height - (i + 1) * scale_factor  # Adjust y to start from the top
            grid[i, j] = {
                'rectangle': shapes.Rectangle(x, y, scale_factor, scale_factor, color = new_color, batch = batch),
                'label': Label(f'({i},{j})', x = x + scale_factor // 2, y = y + scale_factor // 2,
                               anchor_x = 'center', anchor_y = 'center', batch = batch)
            }


def change_all(color):
    for i in range(rows_value):
        for j in range(cols_value):
            x = j * scale_factor
            y = window_height - (i + 1) * scale_factor  # Adjust y to start from the top
            grid[i, j] = {
                'rectangle': shapes.Rectangle(x, y, scale_factor, scale_factor, color = color, batch = batch),
                'label': Label(f'({i},{j})', x = x + scale_factor // 2, y = y + scale_factor // 2,
                               anchor_x = 'center', anchor_y = 'center', batch = batch)
            }


# events each frame
def update(dt):
    global generation_counter
    if scroll_lock_is_active():
        # automates tiles only when scroll lock is active
        automate()
        generation_counter += 1
        window.set_caption(f'{generation_counter}')


# mouse behavior
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        col = int(x // scale_factor)
        row = int((window_height - y) // scale_factor)  # Adjust y to start from the top
        if 0 <= row < rows_value and 0 <= col < cols_value:
            grid[row, col]['rectangle'].color = COLORS['BLUE']

    if button == pyglet.window.mouse.LEFT and modifiers & MOD_SHIFT:
        col = int(x // scale_factor)
        row = int((window_height - y) // scale_factor)
        if 0 <= row < rows_value and 0 <= col < cols_value:
            grid[row, col]['rectangle'].color = COLORS['GREEN_1']

    if button == pyglet.window.mouse.RIGHT:
        col = int(x // scale_factor)
        row = int((window_height - y) // scale_factor)
        if 0 <= row < rows_value and 0 <= col < cols_value:
            grid[row, col]['rectangle'].color = COLORS['RED']

    if button == pyglet.window.mouse.RIGHT and modifiers & MOD_SHIFT:
        col = int(x // scale_factor)
        row = int((window_height - y) // scale_factor)
        if 0 <= row < rows_value and 0 <= col < cols_value:
            grid[row, col]['rectangle'].color = COLORS['ORANGE']


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons == pyglet.window.mouse.LEFT:
        col = int(x // scale_factor)
        row = int((window_height - y) // scale_factor)  # Adjust y to start from the top
        if 0 <= row < rows_value and 0 <= col < cols_value:
            grid[row, col]['rectangle'].color = COLORS['BLUE']


# hotkeys
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.R:
        row, col = random.randint(0, rows_value), random.randint(0, cols_value)
        if 0 <= row < rows_value and 0 <= col < cols_value:
            randomize_all()

    if symbol == key.C:
        row, col = random.randint(0, rows_value), random.randint(0, cols_value)
        if 0 <= row < rows_value and 0 <= col < cols_value:
            change_all(COLORS['WHITE'])


# main loop
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 15)
    pyglet.app.run()
