from modele.Fruit import FRUIT
from modele.Snake import SNAKE
import pygame, sys

class MAIN:
    def __init__(self, cell_number):
        self.fruit = FRUIT(cell_number)
        self.snake = SNAKE()

    def update(self, cell_number):
        self.snake.move_snake()
        self.check_collision(cell_number)
        self.check_fail(cell_number)

    def draw_elements(self, cell_size, screen):
        self.fruit.draw_fruit(cell_size, screen) 
        self.snake.draw_snake(cell_size, screen)

    def check_collision(self,cell_number):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize(cell_number)
            self.snake.add_block()

    def check_fail(self, cell_number):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()