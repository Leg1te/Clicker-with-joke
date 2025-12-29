import pygame

class Game:
    def __init__(self, assets):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.assets = assets
