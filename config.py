"""
Configuration module for Island Height Finder game.

Contains all constant values, settings, and asset loading for the game.
Includes screen dimensions, colors, tile sizes, and loaded image assets.
"""
import os
import pygame.transform

ROWS = 30
COLS = 30
TILE_SIZE = 24
HEADER_HEIGHT = 50
SCREEN_HEIGHT = ROWS * TILE_SIZE + HEADER_HEIGHT
SCREEN_WIDTH = COLS * TILE_SIZE
TITLE = "Island Height Finder"
FPS = 60

GAME_OVER_HEIGHT = 300
GAME_OVER_WIDTH = 400
GAME_OVER_X = (SCREEN_WIDTH - GAME_OVER_WIDTH) // 2
GAME_OVER_Y = HEADER_HEIGHT + (SCREEN_HEIGHT - HEADER_HEIGHT - GAME_OVER_HEIGHT) // 2

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
BUTTON_SPACING = 20

TOTAL_BUTTONS_WIDTH = (BUTTON_WIDTH * 2) + BUTTON_SPACING
START_X = GAME_OVER_X + (GAME_OVER_WIDTH - TOTAL_BUTTONS_WIDTH) // 2
BUTTON_Y = GAME_OVER_Y + GAME_OVER_HEIGHT - BUTTON_HEIGHT - 20

GAME_AREA_START_Y = HEADER_HEIGHT

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

GAME_FOLDER = os.path.dirname(__file__)
MAP_FOLDER = os.path.join(GAME_FOLDER, 'assets')

tile_trees = pygame.transform.scale(pygame.image.load(os.path.join("assets", "trees-and-bushes.png")),
                                    (TILE_SIZE, TILE_SIZE))
tile_rock = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_sea = pygame.transform.scale(pygame.image.load(os.path.join("assets", "sea.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_grass = pygame.transform.scale(pygame.image.load(os.path.join("assets", "grass.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_dark_grass = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dark_grass.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_sand = pygame.transform.scale(pygame.image.load(os.path.join("assets", "sand.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_marble = pygame.transform.scale(pygame.image.load(os.path.join("assets", "marble.png")),
                                   (TILE_SIZE, TILE_SIZE))
legend_image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "legend.png")),
                                   (400, 50))