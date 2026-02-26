import random
import pygame
from settings import *

class Food:
    def __init__(self):
        self.position = (random.randint(0, COLS-1),
                         random.randint(0, ROWS-1))

    def draw(self, surface):
        rect = pygame.Rect(self.position[0]*CELL_SIZE,
                           self.position[1]*CELL_SIZE,
                           CELL_SIZE,
                           CELL_SIZE)
        pygame.draw.rect(surface, RED, rect)