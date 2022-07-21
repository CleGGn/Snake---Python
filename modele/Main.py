from turtle import position
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

    def draw_elements(self, cell_size,cell_number, screen, game_font):
        self.draw_grass(cell_size, cell_number, screen)
        self.fruit.draw_fruit(cell_size, screen) 
        self.snake.draw_snake(cell_size, screen)
        self.draw_score(game_font, cell_size, cell_number, screen)

    def check_collision(self,cell_number):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize(cell_number)
            self.snake.add_block()
            self.snake.play_crunch_cound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize(cell_number)

    def check_fail(self, cell_number):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self, cell_size,cell_number, screen):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size ,row * cell_size,cell_size, cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size ,row * cell_size,cell_size, cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self, game_font, cell_size, cell_number, screen):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))

        rat = self.fruit.rat
        rat_rect = rat.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(rat_rect.left,rat_rect.top,rat_rect.width + score_rect.width + 6 ,rat_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(rat, rat_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)