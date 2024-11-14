import pygame
import numpy as np
from config import *
from map import Map

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.map = Map()

    def new(self):
        pass

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.draw_grid()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    def draw_grid(self):
        for row in range(self.map.grid.shape[0]):
            for col in range(self.map.grid.shape[1]):
                height = self.map.grid[row, col]
                color = self.get_color(height)
                rect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, color, rect)

    @staticmethod
    def get_color(height):
        if height == 0:
            return BLUE
        elif height < 150:
            return SEA_GREEN
        elif height < 350:
            return GREEN
        elif height < 450:
            return DARK_GREEN
        elif height < 550:
            return YELLOW
        elif height < 650:
            return LIGHT_BROWN
        elif height < 750:
            return BROWN
        elif height < 850:
            return DARK_BROWN
        else:
            return WHITE
