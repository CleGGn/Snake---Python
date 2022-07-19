import pygame, sys
from modele.Fruit import FRUIT
from modele.Snake import SNAKE

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT(cell_number)
snake = SNAKE()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,215,70)) 
    fruit.draw_fruit(cell_size, cell_size, screen) 
    snake.draw_snake(cell_size, cell_size, screen) 
    pygame.display.update()
    clock.tick(60)