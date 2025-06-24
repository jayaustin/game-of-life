import pygame
import numpy as np
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 1000
CELL_SIZE = 5
GRID_SIZE = WINDOW_SIZE // CELL_SIZE
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 140
BUTTON_MARGIN = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)

# Create window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + BUTTON_HEIGHT + 2 * BUTTON_MARGIN))
pygame.display.set_caption("Conway's Game of Life")

# Initialize grid
grid = np.zeros((GRID_SIZE, GRID_SIZE))

def draw_grid():
    screen.fill(BLACK)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] == 1:
                pygame.draw.rect(screen, WHITE, 
                               (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_button(text, x, y, width, height, hover=False):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surface, text_rect)

def get_neighbors(grid, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            row = (y + i) % GRID_SIZE
            col = (x + j) % GRID_SIZE
            total += grid[row][col]
    return total

def update_grid():
    new_grid = grid.copy()
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            neighbors = get_neighbors(grid, x, y)
            if grid[y][x] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[y][x] = 0
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1
    return new_grid

def randomize_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            grid[y][x] = random.choice([0, 1])

# Button positions
button_y = WINDOW_SIZE + BUTTON_MARGIN
play_button = pygame.Rect(BUTTON_MARGIN, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
reset_button = pygame.Rect(2 * BUTTON_MARGIN + BUTTON_WIDTH, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
random_button = pygame.Rect(3 * BUTTON_MARGIN + 2 * BUTTON_WIDTH, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)

running = True
playing = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                playing = not playing
            elif reset_button.collidepoint(mouse_pos):
                grid = np.zeros((GRID_SIZE, GRID_SIZE))
                playing = False
            elif random_button.collidepoint(mouse_pos):
                randomize_grid()
            elif mouse_pos[1] < WINDOW_SIZE:  # Click on grid
                x = mouse_pos[0] // CELL_SIZE
                y = mouse_pos[1] // CELL_SIZE
                if x < GRID_SIZE and y < GRID_SIZE:
                    grid[y][x] = 1 if grid[y][x] == 0 else 0

    if playing:
        grid = update_grid()

    # Draw everything
    draw_grid()
    
    # Draw buttons
    mouse_pos = pygame.mouse.get_pos()
    draw_button("Play/Pause" if not playing else "Playing", 
                play_button.x, play_button.y, BUTTON_WIDTH, BUTTON_HEIGHT,
                play_button.collidepoint(mouse_pos))
    draw_button("Reset", reset_button.x, reset_button.y, BUTTON_WIDTH, BUTTON_HEIGHT,
                reset_button.collidepoint(mouse_pos))
    draw_button("Randomize", random_button.x, random_button.y, BUTTON_WIDTH, BUTTON_HEIGHT,
                random_button.collidepoint(mouse_pos))

    pygame.display.flip()
    clock.tick(10)  # Limit to 10 FPS

pygame.quit()