"""
    background.py
    Dylan Grandjean
    November 16th, 2016

    Moving background which resets when
    reaching the edge of the screen.
"""
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/background.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dy = 5

    def update(self, screen):
        self.rect.bottom += self.dy
        if self.rect.top >= 0:
            self.reset(screen)

    def reset(self, screen):
        self.rect.bottom = screen.get_height()
        
