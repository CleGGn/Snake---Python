import pygame, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self, cell_number):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)


    def draw_fruit(self, cell_size, cell_size2, screen):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size2),cell_size,cell_size2)
        pygame.draw.rect(screen,(120,166,114),fruit_rect)
