import os

import pygame.transform

ROWS = 30
COLS = 30
TILE_SIZE = 26
SCREEN_HEIGHT = ROWS * TILE_SIZE
SCREEN_WIDTH = COLS * TILE_SIZE
TITLE = "Island Height Finder"
FPS = 60

# define colors
BLACK = (0, 0, 0)
RED = (192, 0, 0)

BLUE = (0, 0, 255)
SEA_GREEN = (24, 146, 93)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
LIGHT_BROWN = (204, 153, 0)
BROWN = (153, 102, 51)
DARK_BROWN = (102, 51, 0)
WHITE = (255, 255, 255)

DARK_GREY = (40, 40, 40)
BGCOLOUR = DARK_GREY

# paths
GAME_FOLDER = os.path.dirname(__file__)
MAP_FOLDER = os.path.join(GAME_FOLDER, 'assets')

tile_green = pygame.transform.scale(pygame.image.load(os.path.join("assets", "trees-and-bushes.png")),
                                    (TILE_SIZE, TILE_SIZE))
