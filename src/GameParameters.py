import pygame as pyg

# Miscellaneous
FPS = 60
FALL_TIME_INTERVAL_ms = 500
BLOCK_BORDER_THICKNESS = 2

# Grid
GRID_ELEM_SIZE = 30
GRID_NR_OF_COLS = 10
GRID_NR_OF_ROWS = 20
GRID_TLC_x = 50 # TLC = top left corner
GRID_TLC_y = 50
GRID_THICKNESS = 1

# Game window and positioning
GAME_WINDOW_WIDTH = 900
GAME_WINDOW_HEIGHT = 680
BACKGROUND_POS = (-830, -320)
LOGO_POS = (-100, -130)
SCORE_TEXT_POS = (400, 400)

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128,128,128)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 127, 0)

# Tile related
TILE_COLORS = {"I": CYAN,
               "J": BLUE,
               "L": ORANGE,
               "O": YELLOW,
               "S": GREEN,
               "T": PURPLE,
               "Z": RED}
NR_OF_TILES = len(TILE_COLORS)
TILE_CONFIG_IDX_MAX = 4
TILE_SHAPES = {"I": [[[0, 0, 0, 0],
                     [1, 1, 1, 1],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 1, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1, 0]],
                     
                     [[0, 0, 0, 0],
                     [1, 1, 1, 1],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 1, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1, 0]]
                     ],
               
               "J": [[[0, 0, 0, 0],
                     [1, 1, 1, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 1, 1, 0],
                     [0, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 0, 0],
                     [1, 0, 0, 0],
                     [1, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 1, 0, 0],
                     [0, 1, 0, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0]]
                     ],
               
                "L": [[[0, 0, 0, 0],
                     [1, 1, 1, 0],
                     [1, 0, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 0, 0],
                     [0, 0, 1, 0],
                     [1, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]]
                     ],
                
                "O": [[[0, 0, 0, 0],
                     [0, 1, 1, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 0, 0],
                     [0, 1, 1, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 0, 0],
                     [0, 1, 1, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 0, 0],
                     [0, 1, 1, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0]]
                     ],
                
                "S": [[[0, 0, 0, 0],
                     [0, 1, 1, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[1, 0, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 0, 0],
                     [0, 1, 1, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[1, 0, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]]
                     ],
                
                "T": [[[0, 0, 0, 0],
                     [1, 1, 1, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 0, 0],
                     [0, 1, 0, 0],
                     [1, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 1, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]]
                     ],
                
                "Z": [[[0, 0, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 1, 0],
                     [0, 1, 1, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0]],
                     
                     [[0, 0, 1, 0],
                     [0, 1, 1, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]]
                     ],                                                      
               }

# Hotkeys
LEFT = pyg.K_LEFT
RIGHT = pyg.K_RIGHT
DOWN = pyg.K_DOWN
ROTATE = pyg.K_SPACE