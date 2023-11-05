# In snake.py

import pygame
import sys
import random

class Snake:
    def __init__(self):
        self.cell_size = 40
        self.head_size = 40
        self.color = (0, 255, 0)
        self.body = [(5, 5)]
        self.direction = "DOWN"
        self.points = 0

    def draw_snake(self, screen):
        for segment in self.body:
            self.draw_segment(segment[0], segment[1], screen, self.color)

    def draw_segment(self, grid_x, grid_y, screen, color):
        screen_x = grid_x * self.cell_size
        screen_y = grid_y * self.cell_size
        pygame.draw.rect(screen, color, (screen_x, screen_y, self.cell_size, self.cell_size))

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)

        if 0 <= new_head[0] < 16 and 0 <= new_head[1] < 12:
            self.body.insert(0, new_head)

            if len(self.body) > 2:
                self.body.pop()
        else:
            pygame.quit()
            sys.exit()

    def change_direction(self, new_direction):
        if not ((self.direction == "UP" and new_direction == "DOWN") or
                (self.direction == "DOWN" and new_direction == "UP") or
                (self.direction == "LEFT" and new_direction == "RIGHT") or
                (self.direction == "RIGHT" and new_direction == "LEFT")):
            self.direction = new_direction

    def check_collision(self, apple):
        return self.body[0] == apple.position

    def eat_apple(self, apple):
        if self.check_collision(apple):
            apple.generate_new_position()

            # Randomize the number of blocks to add (between 1 and 3)
            blocks_to_add = random.randint(1, 3)

            for _ in range(blocks_to_add):
                self.body.append(self.body[-1])

            self.points += apple.point_value  # Update points based on apple type
            print(f"Points: {self.points}")

    def check_collision_boundary(self):
        head_x, head_y = self.body[0]
        return not (0 <= head_x < 16 and 0 <= head_y < 12)

    def check_collision_self(self):
        head = self.body[0]
        return head in self.body[1:]
