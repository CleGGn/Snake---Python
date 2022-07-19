import pygame
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]

    def draw_snake(self, cell_size, cell_size2, screen):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x * cell_size),int(block.y * cell_size2),cell_size,cell_size2)
            pygame.draw.rect(screen,(94, 53, 177),snake_rect)
