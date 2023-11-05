import pygame


class Grid:
    def __init__(self):
        self.cell_size = 40

    def draw_grid(self, screen_width, screen_height, screen):
        for x in range(0, screen_width, self.cell_size):
            pygame.draw.line(screen, (0, 0, 255), (x, 0), (x, screen_height))
        for y in range(0, screen_height, self.cell_size):
            pygame.draw.line(screen, (0, 0, 255), (0, y), (screen_width, y))

    def drawing(self, grid_x, grid_y, screen, color):
        screen_x = grid_x * self.cell_size
        screen_y = grid_y * self.cell_size
        pygame.draw.rect(screen, color, (screen_x, screen_y, self.cell_size, self.cell_size))



