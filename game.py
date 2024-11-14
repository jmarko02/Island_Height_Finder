import pygame
import numpy as np
from config import *
from map import Map


class Game:
    def __init__(self):
        self.game_state = "playing"
        self.guess_cnt = 3
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.map = Map()

    def new(self):
        pass

    def run(self):
        # self.playing = True
        # while self.playing:
        while self.game_state == "playing":
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                selected_island_avg_height = self.get_selected_island(mouse_position)
                if selected_island_avg_height is not None:
                    self.handle_guess(selected_island_avg_height)

    def get_selected_island(self, mouse_pos):
        # Implement the logic to detect the selected island and calculate its average height
        # Return the average height or None if no island is selected
        pass

    def get_correct_island(self):
        # Implement the logic to find the island with the greatest average height
        # Return the average height of the correct island
        pass

    def handle_guess(self, selected_island_avg_height):
        # Implement the logic to handle the user's guess
        # Update the game state and number of guesses accordingly
        pass

    def display_game_state(self):
        # Display the current game state (number of guesses, won/lost, etc.) on the screen
        pass

    def draw_grid(self):
        for row in range(self.map.grid.shape[0]):
            for col in range(self.map.grid.shape[1]):
                height = self.map.grid[row, col]
                if height == 0:
                    color = (0, 0, 255)
                    rect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    pygame.draw.rect(self.screen, color, rect)
                elif height <= 400:
                    # Render terrain with the loaded image
                    self.screen.blit(tile_green, (col * TILE_SIZE, row * TILE_SIZE))
                else:
                    # Render other terrain heights with the previous color-based method
                    color = self.get_color(height)
                    rect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    pygame.draw.rect(self.screen, color, rect)
                # color = self.get_color(height)
                # ect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                # pygame.draw.rect(self.screen, color, rect)

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
            return DARK_BROWN
        elif height < 750:
            return BROWN
        elif height < 850:
            return LIGHT_BROWN
        else:
            return WHITE
