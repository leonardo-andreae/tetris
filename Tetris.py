import pygame as pyg
import sys, os
sys.path.append(os.path.join(sys.path[0], 'src'))
import GameParameters as par
from Tile import *
from GameState import *
import numpy as np

def event_handler(tile, game_state):
    for event in pyg.event.get():
        # pressing the "X" button terminates the application
        if event.type == pyg.QUIT:
            game_state.game_running = False
        if event.type == game_state.gravity_tick_ev:
            tile.is_falling = True

def draw_grid():
    # draw horizontal lines
    for row_idx in range(0, par.GRID_NR_OF_ROWS + 1):
        start_coords = (par.GRID_TLC_x, par.GRID_TLC_y + row_idx * par.GRID_ELEM_SIZE)
        end_coords = (par.GRID_TLC_x + par.GRID_NR_OF_COLS * par.GRID_ELEM_SIZE, 
                      par.GRID_TLC_y + row_idx * par.GRID_ELEM_SIZE)
        pyg.draw.line(surface=game_window, color=par.BLACK, 
                      start_pos=start_coords, end_pos=end_coords,
                      width=par.GRID_THICKNESS)
    # draw vertical lines    
    for col_idx in range(0, par.GRID_NR_OF_COLS + 1):
        start_coords = (par.GRID_TLC_x + col_idx * par.GRID_ELEM_SIZE, par.GRID_TLC_y)
        end_coords = (par.GRID_TLC_x + col_idx * par.GRID_ELEM_SIZE, 
                      par.GRID_TLC_y + par.GRID_ELEM_SIZE * par.GRID_NR_OF_ROWS)
        pyg.draw.line(surface=game_window, color=par.BLACK, 
                      start_pos=start_coords, end_pos=end_coords,
                      width=par.GRID_THICKNESS)

def draw_block_with_borders(TLC_x, TLC_y, size, color, border_color):
    block = pyg.Rect(TLC_x, TLC_y, size, size)
    pyg.draw.rect(game_window, color, block)
    top_left = (TLC_x, TLC_y) 
    down_left = (top_left[0], top_left[1] + size)
    down_right = (down_left[0] + size, down_left[1])
    top_right = (down_right[0], down_right[1] - size)
    pyg.draw.lines(surface=game_window, color=border_color, closed=True,
                   points=[top_left, down_left, down_right, top_right],
                   width=par.BLOCK_BORDER_THICKNESS)

def draw_board(game_state):
    for row in range (0, par.GRID_NR_OF_ROWS):
        for col in range (0, par.GRID_NR_OF_COLS):
            if game_state.board_occupation_matrix[row][col] != None:
                draw_block_with_borders(par.GRID_TLC_x + col * par.GRID_ELEM_SIZE,
                                        par.GRID_TLC_y + row * par.GRID_ELEM_SIZE,
                                        par.GRID_ELEM_SIZE,
                                        game_state.board_occupation_matrix[row][col],
                                        par.WHITE)

def draw_tile(tile):
    # draw tile with its border
    for col in range (0, par.TILE_CONFIG_IDX_MAX):
        for row in range (0, par.TILE_CONFIG_IDX_MAX):
           if tile.configuration_matrix[row][col] == 1:
               draw_block_with_borders(tile.position.x + par.GRID_ELEM_SIZE * col,
                                       tile.position.y + par.GRID_ELEM_SIZE * row,
                                       par.GRID_ELEM_SIZE,
                                       par.TILE_COLORS[tile.type],
                                       par.WHITE)
 
def draw_scene(tile, game_state):
    # TODO: only draw tile and board each time not the entire thing
    # color background such that older objects do not appear
    game_window.blit(bg, par.BACKGROUND_POS)
    game_window.blit(tetris_logo, par.LOGO_POS)
    
    draw_grid()
    draw_board(game_state)
    draw_tile(tile) 
    # After calling the drawing functions to make the display Surface object look the way you want, you must call this to make the display Surface actually appear on the user’s monitor.
    pyg.display.update()


def main():
    global game_window, bg, tetris_logo
    pyg.init()
    game_window = pyg.display.set_mode((par.GAME_WINDOW_WIDTH, par.GAME_WINDOW_HEIGHT))
    pyg.display.set_caption("Tetris")
    
    # https://www.freepik.com/icons/tetris Icon by Freepik
    tetris_icon = pyg.image.load('assets/tetris_icon.png')
    pyg.display.set_icon(tetris_icon)

    bg = pyg.image.load('assets/bg.jpg')
    tetris_logo = pyg.image.load('assets/tetris_logo.png')
    tetris_logo = pyg.transform.scale2x(tetris_logo)
    
    game_state = GameState()
    tile = Tile(game_state)
  
    while game_state.game_running:
        event_handler(tile, game_state)
        
        game_state.get_current_keys()
        tile.update_position(game_state)
        draw_scene(tile, game_state)

        game_state.game_over_check()

        # limits game's fps (waits) and returns the ms count since the last call
        game_state.clock.tick(par.FPS)          
    pyg.quit() 
    
if __name__ == "__main__":
    main()