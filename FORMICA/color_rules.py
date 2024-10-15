from constants import *
import random

# Formica
# rules for tile colors


# tiles fall when tile below is WHITE
def handle_fall(y, x, grid, next_grid, COLORS, color):
    if grid[y + 1, x]['rectangle'].color == COLORS['WHITE']:
        next_grid[y + 1, x]['rectangle'].color = color
        next_grid[y, x]['rectangle'].color = COLORS['WHITE']


def spread_color(y, x, grid, next_grid, COLORS, new_color, adj_type = 'adjacent'):
    # patterns
    if adj_type == 'adjacent':
        adjacent_tiles = [(y + dy, x + dx) for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                          if 0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1]]
    elif adj_type == 'all_adjacent':
        adjacent_tiles = [(y + dy, x + dx) for dy, dx in
                          [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                          if 0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1]]
    if adjacent_tiles:
        # selects a random tile within the adj type
        rand_tile = random.choice(adjacent_tiles)
        if next_grid[rand_tile[0], rand_tile[1]]['rectangle'].color == COLORS['RED']:
            next_grid[rand_tile[0], rand_tile[1]]['rectangle'].color = COLORS['RED']
            pass
        next_grid[rand_tile[0], rand_tile[1]]['rectangle'].color = new_color


##### BLUE (water)
# checks if rows are blue
def is_row_blue(y, grid, COLORS):
    return all(grid[y, x]['rectangle'].color == COLORS['BLUE'] for x in range(grid.shape[1]))


def handle_blue(y, x, grid, next_grid, COLORS):
    if y < grid.shape[0] - 1 and grid[y + 1, x]['rectangle'].color == COLORS['WHITE']:
        next_grid[y + 1, x]['rectangle'].color = COLORS['BLUE']
        next_grid[y, x]['rectangle'].color = COLORS['WHITE']
        # fills the row
    elif y == grid.shape[0] - 1 or is_row_blue(y + 1, grid, COLORS):
        if x > 0 and grid[y, x - 1]['rectangle'].color == COLORS['WHITE']:
            next_grid[y, x - 1]['rectangle'].color = COLORS['BLUE']
        elif x < grid.shape[1] - 1 and grid[y, x + 1]['rectangle'].color == COLORS['WHITE']:
            next_grid[y, x + 1]['rectangle'].color = COLORS['BLUE']


##### RED/ORANGE (lava, fire)
def handle_orange(y, x, grid, next_grid, COLORS):
    spread_color(y, x, grid, next_grid, COLORS, COLORS['RED'], adj_type = 'all_adjacent')


def handle_red(y, x, grid, next_grid, colors):
    handle_fall(y, x, grid, next_grid, COLORS, COLORS['RED'])
    if next_grid[y + 1, x]['rectangle'].color == COLORS['BLUE']:
        grid[y, x]['rectangle'].color = COLORS['TEAL']


##### DARK BROWN (rock)
def handle_dbrown(y, x, grid, next_grid, COLORS):
    if grid[y + 1, x]['rectangle'].color == COLORS['BLUE']:
        next_grid[y + 1, x]['rectangle'].color = COLORS['DARK_BROWN']
        next_grid[y, x]['rectangle'].color = COLORS['WHITE']


#### GREEN (life)
# duplicates itself
def handle_green_1(y, x, grid, next_grid, COLORS):
    handle_fall(y, x, grid, next_grid, COLORS, COLORS['GREEN_1'])
    spread_color(y, x, grid, next_grid, COLORS, COLORS['GREEN_2'], adj_type = 'adjacent')


def handle_green_2(y, x, grid, next_grid, COLORS):
    handle_fall(y, x, grid, next_grid, COLORS, COLORS['GREEN_2'])
    spread_color(y, x, grid, next_grid, COLORS, COLORS['GREEN_3'], adj_type = 'all_adjacent')


def handle_green_3(y, x, grid, next_grid, COLORS):
    handle_fall(y, x, grid, next_grid, COLORS, COLORS['GREEN_3'])
    # growth factor
    if random.random() < 0.05:
        spread_color(y, x, grid, next_grid, COLORS, COLORS['GREEN_1'], adj_type = 'all_adjacent')
    else:
        spread_color(y, x, grid, next_grid, COLORS, COLORS['GREEN_4'], adj_type = 'all_adjacent')


def handle_green_4(y, x, grid, next_grid, COLORS):
    handle_fall(y, x, grid, next_grid, COLORS, COLORS['GREEN_4'])
