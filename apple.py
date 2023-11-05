import pygame
from grid import Grid
import random


class Apple:
    def __init__(self):
        self.cell_size = 40
        self.position = (0, 0)  # Initialize the position, it will be updated later
        self.generate_new_position()
        self.point_value = random.randint(1, 3)

    def generate_new_position(self):
        # Generate a new random position for the apple

        x = random.randint(0, 14)
        y = random.randint(0, 10)
        self.position = (x, y)

    def draw_apple(self, screen):
        grid = Grid()
        grid.drawing(self.position[0], self.position[1], screen, (255, 0, 0))
