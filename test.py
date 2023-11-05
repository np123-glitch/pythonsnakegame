import pygame

# Define grid and block size
GRID_WIDTH = 12
GRID_HEIGHT = 16
BLOCK_SIZE = 20

class GridBlock:
    def __init__(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.screen_x = grid_x * BLOCK_SIZE
        self.screen_y = grid_y * BLOCK_SIZE
        self.color = (255, 0, 0)  # Example color (red)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.screen_x, self.screen_y, BLOCK_SIZE, BLOCK_SIZE))

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = GRID_WIDTH * BLOCK_SIZE
screen_height = GRID_HEIGHT * BLOCK_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid Example")

# Create a grid of blocks
grid = [[GridBlock(x, y) for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw everything
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw the grid
    for row in grid:
        for block in row:
            block.draw(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
