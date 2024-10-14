import pyglet
from pyglet import shapes
from pyglet.text import Label
import numpy as np
from pyglet.window import key
import random
import ctypes
import config_window
from constants import *

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

    for x in range(cols_value):
        for y in range(rows_value):
            # access tile at (y, x)
            t_focus = grid[y, x]
            current_color = t_focus['rectangle'].color

            # what each color does
            if current_color == COLORS['WHITE']:
                t_focus['rectangle'].color = COLORS['BLACK']

            elif current_color == COLORS['BLACK']:
                t_focus['rectangle'].color = COLORS['WHITE']

    # update the grid with the next state
    grid = next_grid


# randomize random tile color
def randomize_tile():
    row = random.randint(0, rows_value - 1)
    col = random.randint(0, cols_value - 1)
    new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    grid[row, col]['rectangle'].color = new_color


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
            grid[row, col]['rectangle'].color = COLORS['WHITE']


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons == pyglet.window.mouse.LEFT:
        col = int(x // scale_factor)
        row = int((window_height - y) // scale_factor)  # Adjust y to start from the top
        if 0 <= row < rows_value and 0 <= col < cols_value:
            grid[row, col]['rectangle'].color = COLORS['WHITE']


# hotkeys
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.H:
        row, col = random.randint(0, rows_value), random.randint(0, cols_value)
        if 0 <= row < rows_value and 0 <= col < cols_value:
            randomize_tile()


# main loop
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, update_speed)
    pyglet.app.run()
