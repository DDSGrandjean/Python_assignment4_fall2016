"""
    playerClass.py
    November 16, 2016
    Dylan Grandjean

    Class which creates a player controlled
    circle which is controlled by the mouse
    and destroys monsters in the game.
"""
import pygame, math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.image.set_colorkey((255, 255, 255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        self.dx = 2
        self.dy = 2

    def update(self, mouseX, mouseY):
        #Player boundaries
        if not (mouseX - self.rect.centerx) == 0 and not (mouseY - self.rect.centery) == 0:
            self.rect.centerx += (mouseX - self.rect.centerx) / 40.0
            self.rect.centery += (mouseY - self.rect.centery) / 40.0
