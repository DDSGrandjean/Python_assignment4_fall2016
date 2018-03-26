"""
    monsterClass.py
    November 14th, 2016
    Dylan Grandjean

    Class which creates a monster at random position
    and speed which moves around, randomly switching
    position and speed.
"""
import pygame, random

class Monster(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/monster.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.image.set_colorkey((255, 255, 255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

        self.ouch = pygame.mixer.Sound("assets/laser.wav")
        
        self.rect.centerx = random.randint(0, 640)
        self.rect.centery = random.randint(0, 480)
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        self.sec = random.randint(0, 100)

    def update(self, screen):
        #move monsters and check for boundaries
        self.sec += 1

        if self.sec == 120:
            self.sec = 0
            self.dx = random.randint(-5, 5)
            self.dy = random.randint(-5, 5)

        if self.rect.left > screen.get_width():
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = screen.get_width()
        if self.rect.top > screen.get_height():
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = screen.get_height()

        self.rect.centerx += self.dx
        self.rect.centery += self.dy

    def ouchPlay(self):
        #makes a sounf
        self.ouch.play()
