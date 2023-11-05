# In main.py

import pygame
import sys
from grid import Grid
from snake import Snake
from apple import Apple

background_colour = (0, 0, 0)
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake Game')
screen.fill(background_colour)
pygame.display.flip()

running = True
clock = pygame.time.Clock()

grid = Grid()
snake = Snake()
apple = Apple()
score = 0

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == GAME_UPDATE:
            snake.move()

            # Check for collisions with the apple
            if snake.check_collision(apple):
                snake.eat_apple(apple)
                score += apple.point_value  # Update score based on apple type

            # Check for collisions with boundaries or itself
            if snake.check_collision_boundary() or snake.check_collision_self():
                # Game over screen
                print(f"Game Over! Your Score: {score}")
                running = False

            # Check for collisions or other game logic here
            screen.fill(background_colour)
            grid.draw_grid(width, height, screen)
            snake.draw_snake(screen)
            apple.draw_apple(screen)

            pygame.display.flip()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    clock.tick(10)  # Adjust the frame rate as needed

pygame.quit()
