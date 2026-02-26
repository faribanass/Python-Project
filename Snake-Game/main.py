import pygame
from settings import WIDTH, HEIGHT
from game import Game

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Snake")

game = Game(screen)
game.run()