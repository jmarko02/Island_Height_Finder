import pygame
from config import *
from map import Map

"""
Main game class controlling game logic and display.

Manages the game state, user interactions, and visual representation of the island
height finding game. Handles player guesses, updates game state, and renders the
game interface including the map, header with guess counter, and game over screen.

Attributes:
    game_state (str): Current state of game ("playing", "won", "lost", "quit")
    guess_cnt (int): Number of remaining guesses
    screen: Pygame display surface for rendering
    map (Map): Map instance containing island data
    clock: Pygame clock for controlling frame rate
"""


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

        self.restart_button = pygame.Rect(
            START_X,
            BUTTON_Y,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )

        self.exit_button = pygame.Rect(
            START_X + BUTTON_WIDTH + BUTTON_SPACING,
            BUTTON_Y,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )

    def new(self):
        self.game_state = "playing"
        self.guess_cnt = 3
        self.map = Map()

    def run(self):
        while self.game_state != "quit":
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.draw_grid()
        self.display_game_state()

        if self.game_state in ["won", "lost"]:
            self.draw_game_over_window()

        pygame.display.flip()

    def draw_game_over_window(self):
        window_rect = pygame.Rect(GAME_OVER_X, GAME_OVER_Y, GAME_OVER_WIDTH, GAME_OVER_HEIGHT)
        pygame.draw.rect(self.screen, DARK_GREY, window_rect)
        pygame.draw.rect(self.screen, WHITE, window_rect, 2)

        font = pygame.font.Font(None, 48)
        title_text = "You Won!" if self.game_state == "won" else "You Lost!"
        title_color = GREEN if self.game_state == "won" else RED
        title = font.render(title_text, True, title_color)
        title_rect = title.get_rect(centerx=window_rect.centerx, top=window_rect.top + 20)
        self.screen.blit(title, title_rect)

        pygame.draw.rect(self.screen, GREEN, self.restart_button)
        pygame.draw.rect(self.screen, RED, self.exit_button)

        button_font = pygame.font.Font(None, 32)
        restart_text = button_font.render("Restart", True, WHITE)
        exit_text = button_font.render("Exit", True, WHITE)

        restart_text_rect = restart_text.get_rect(center=self.restart_button.center)
        exit_text_rect = exit_text.get_rect(center=self.exit_button.center)

        self.screen.blit(restart_text, restart_text_rect)
        self.screen.blit(exit_text, exit_text_rect)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = "quit"
                pygame.quit()
                quit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = "quit"
                    pygame.quit()
                    quit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if self.game_state in ["won", "lost"]:
                    if self.restart_button.collidepoint(mouse_position):
                        self.new()
                    elif self.exit_button.collidepoint(mouse_position):
                        self.game_state = "quit"
                        pygame.quit()
                        quit(0)
                else:
                    selected_island_avg_height = self.get_selected_island(mouse_position)
                    if selected_island_avg_height is not None:
                        self.handle_guess(selected_island_avg_height)

    def get_selected_island(self, mouse_pos):
        row = (mouse_pos[1] - HEADER_HEIGHT) // TILE_SIZE
        col = mouse_pos[0] // TILE_SIZE
        if (0 <= row < self.map.grid.shape[0] and
                0 <= col < self.map.grid.shape[1] and
                mouse_pos[1] >= HEADER_HEIGHT):

            if self.map.grid[row, col] > 0:
                island_id = self.map.field_to_island[(row, col)]
                return self.map.island_to_avg_height[island_id]
            else:
                return None

    def get_correct_island(self):
        max_avg_height = max(self.map.island_to_avg_height.values())
        for island_id, avg_height in self.map.island_to_avg_height.items():
            if avg_height == max_avg_height:
                self.correct_island_id = island_id
                break
        return max_avg_height

    def handle_guess(self, selected_island_avg_height):
        correct_avg_height = self.get_correct_island()

        if selected_island_avg_height == correct_avg_height:
            self.game_state = "won"
        else:
            selected_island_id = None
            for island_id, avg_height in self.map.island_to_avg_height.items():
                if avg_height == selected_island_avg_height:
                    selected_island_id = island_id
                    break

            self.flood_island(selected_island_id)
            self.map.island_to_avg_height.pop(selected_island_id)

            self.guess_cnt -= 1
            if self.guess_cnt == 0:
                self.game_state = "lost"

    def flood_island(self, island_id):
        island_fields = self.map.island_to_fields[island_id]

        for row, col in island_fields:
            self.map.grid[(row, col)] = 0

        self.map.island_to_fields.pop(island_id)

        for row, col in island_fields:
            self.map.field_to_island.pop((row, col))

    def display_game_state(self):
        if self.game_state == "playing":

            header_rect = pygame.Rect(0, 0, SCREEN_WIDTH, HEADER_HEIGHT)
            pygame.draw.rect(self.screen, WHITE, header_rect)
            pygame.draw.line(self.screen, WHITE, (0, HEADER_HEIGHT), (SCREEN_WIDTH, HEADER_HEIGHT))

            font = pygame.font.Font(None, 36)
            text = font.render(f"Guesses left: {self.guess_cnt}", True, RED)
            text_rect = text.get_rect()
            text_rect.left = 20
            text_rect.centery = HEADER_HEIGHT // 2
            self.screen.blit(text, text_rect)

            legend_rect = legend_image.get_rect()
            legend_rect.right = SCREEN_WIDTH
            legend_rect.centery = HEADER_HEIGHT // 2
            self.screen.blit(legend_image, legend_rect)

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
            self.screen.blit(tile_sea, (col * TILE_SIZE, GAME_AREA_START_Y + row * TILE_SIZE))
        elif height <= 150:
            self.screen.blit(tile_sand, (col * TILE_SIZE, GAME_AREA_START_Y + row * TILE_SIZE))
        elif height <= 300:
            self.screen.blit(tile_grass, (col * TILE_SIZE, GAME_AREA_START_Y + row * TILE_SIZE))
        elif height <= 450:
            self.screen.blit(tile_dark_grass, (col * TILE_SIZE, GAME_AREA_START_Y + row * TILE_SIZE))
        elif height <= 600:
            self.screen.blit(tile_trees, (col * TILE_SIZE, GAME_AREA_START_Y + row * TILE_SIZE))
        elif height <= 800:
            self.screen.blit(tile_rock, (col * TILE_SIZE, GAME_AREA_START_Y + row * TILE_SIZE))
        else:
            self.screen.blit(tile_marble, (col * TILE_SIZE, GAME_AREA_START_Y + row * TILE_SIZE))

