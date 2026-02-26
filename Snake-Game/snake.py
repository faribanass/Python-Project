import pygame
from settings import *

class Snake:
    def __init__(self):
        self.body = [(5,5), (4,5), (3,5)]
        self.direction = (1,0)
        self.grow = False

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0],
                    head[1] + self.direction[1])

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, surface):
        for segment in self.body:
            rect = pygame.Rect(segment[0]*CELL_SIZE,
                               segment[1]*CELL_SIZE,
                               CELL_SIZE,
                               CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= COLS:
            return True
        if head[1] < 0 or head[1] >= ROWS:
            return True
        if head in self.body[1:]:
            return True
        return False