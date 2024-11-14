import pygame
import numpy as np
from config import *
from map import Map


class Game:
    def __init__(self):
        self.game_state = "playing"
        self.guess_cnt = 3
        self.correct_island_id = None
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.map = Map()
        pygame.font.init()

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
        self.display_game_state()
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
        row = mouse_pos[1] // TILE_SIZE
        col = mouse_pos[0] // TILE_SIZE

        if self.map.grid[row, col] > 0:
            island_id = self.map.field_to_island[(row, col)]
            return self.map.island_to_avg_height[island_id]
        else:
            return None

    def get_correct_island(self):
        max_avg_height = max(self.map.island_to_avg_height.values())
        for island_id, avg_height in self.map.island_to_avg_height.items():
            if avg_height == max_avg_height:
                correct_island_id = island_id
                break
        return max_avg_height

    def handle_guess(self, selected_island_avg_height):
        correct_avg_height = self.get_correct_island()

        if selected_island_avg_height == correct_avg_height:
            self.game_state = "won"
        else:
            self.guess_cnt -= 1
            if self.guess_cnt == 0:
                self.game_state = "lost"

    def display_game_state(self):
        if self.game_state == "playing":
            font = pygame.font.Font(None, 36)
            text = font.render(f"Guesses left: {self.guess_cnt}", True, RED)
            text_rect = text.get_rect()
            text_rect.topleft = (10, 10)
            self.screen.blit(text, text_rect)

        elif self.game_state == "won":
            font = pygame.font.Font(None, 72)
            text = font.render("You Won!", True, GREEN)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.screen.blit(text, text_rect)

        elif self.game_state == "lost":
            font = pygame.font.Font(None, 72)
            text = font.render("You Lost!", True, RED)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.screen.blit(text, text_rect)


    def draw_grid(self):
        for row in range(self.map.grid.shape[0]):
            for col in range(self.map.grid.shape[1]):
                height = self.map.grid[row, col]
                self.display_tile(row, col, height)

    def display_tile(self, row, col, height):
        if height == 0:
            self.screen.blit(tile_sea, (col * TILE_SIZE, row * TILE_SIZE))
        elif height <= 100:
            self.screen.blit(tile_sand, (col * TILE_SIZE, row * TILE_SIZE))
        elif height <= 250:
            self.screen.blit(tile_yellow_grass, (col * TILE_SIZE, row * TILE_SIZE))
        elif height <= 400:
            self.screen.blit(tile_trees, (col * TILE_SIZE, row * TILE_SIZE))
        elif height <= 550:
            self.screen.blit(tile_grass, (col * TILE_SIZE, row * TILE_SIZE))
        elif height <= 700:
            self.screen.blit(tile_rock, (col * TILE_SIZE, row * TILE_SIZE))
        elif height <= 850:
            self.screen.blit(tile_dirt, (col * TILE_SIZE, row * TILE_SIZE))
        else:
            self.screen.blit(tile_marble, (col * TILE_SIZE, row * TILE_SIZE))

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
