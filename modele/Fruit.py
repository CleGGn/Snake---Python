import pygame, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self, cell_number):
        self.randomize(cell_number)
        self.rat = pygame.image.load('Graphics/rat.png').convert_alpha()

    def draw_fruit(self, cell_size, screen):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(self.rat,fruit_rect)
        # pygame.draw.rect(screen,(120,166,114),fruit_rect)

    def randomize(self, cell_number):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)