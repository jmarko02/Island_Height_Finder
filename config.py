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

tile_trees = pygame.transform.scale(pygame.image.load(os.path.join("assets", "trees-and-bushes.png")),
                                    (TILE_SIZE, TILE_SIZE))
tile_clay = pygame.transform.scale(pygame.image.load(os.path.join("assets", "clay.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_desert = pygame.transform.scale(pygame.image.load(os.path.join("assets", "desert.png")),
                                     (TILE_SIZE, TILE_SIZE))
tile_grains = pygame.transform.scale(pygame.image.load(os.path.join("assets", "grains.png")),
                                     (TILE_SIZE, TILE_SIZE))
tile_landscape = pygame.transform.scale(pygame.image.load(os.path.join("assets", "landscape.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_rock = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_sea = pygame.transform.scale(pygame.image.load(os.path.join("assets", "sea.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_woods = pygame.transform.scale(pygame.image.load(os.path.join("assets", "woods.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_clouds = pygame.transform.scale(pygame.image.load(os.path.join("assets", "clouds.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_grass = pygame.transform.scale(pygame.image.load(os.path.join("assets", "grass.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_hill = pygame.transform.scale(pygame.image.load(os.path.join("assets", "hill.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_desert1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "desert1.jpg")),
                                   (TILE_SIZE, TILE_SIZE))
tile_snow = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images.jpeg")),
                                   (TILE_SIZE, TILE_SIZE))
tile_dirt = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dirt.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_water = pygame.transform.scale(pygame.image.load(os.path.join("assets", "water.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_yellow_grass = pygame.transform.scale(pygame.image.load(os.path.join("assets", "yellow_grass.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_snow1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "snow.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_dark_grass = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dark_grass.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_sand = pygame.transform.scale(pygame.image.load(os.path.join("assets", "sand.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_sand = pygame.transform.scale(pygame.image.load(os.path.join("assets", "image.png")),
                                   (TILE_SIZE, TILE_SIZE))
tile_marble = pygame.transform.scale(pygame.image.load(os.path.join("assets", "marble.png")),
                                   (TILE_SIZE, TILE_SIZE))