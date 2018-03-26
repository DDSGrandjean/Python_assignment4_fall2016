"""
    squeaker.py
    Dylan Grandjean
    November 14th, 2016

    Game which has the player run over
    foes in order to destroy them.
"""
#import and initialize pygame
import pygame
from monsterClass import *
from playerClass import *
from background import *
pygame.init()
if not pygame.mixer:
    print "-- Sound Error --"
else:
    pygame.mixer.init()

#display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Monstruction!")

def main():
    #Create background
    back = pygame.Surface(screen.get_size())
    back = back.convert()
    back.fill((255, 255, 255))
    
    #variables
    clock = pygame.time.Clock()
    keepGoing = True;
    mouseX = 320
    mouseY = 240
    background = Background()
    player = Player()
    monsters = []
    i = 0
    while i < 50:
        monsters.append(Monster())
        i += 1
    monsterGroup = pygame.sprite.Group(monsters)
    playerGroup = pygame.sprite.Group(player)
    backgroundGroup = pygame.sprite.Group(background)
    
    #loop
    while keepGoing:
        #fps
        clock.tick(30)

        #events handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                mouseX, mouseY = pygame.mouse.get_pos()

        hitMonsters = pygame.sprite.spritecollide(player, monsterGroup, True)
        if not hitMonsters == []:
            hitMonsters[0].ouchPlay()

        #refresh display
        backgroundGroup.clear(screen, back)
        monsterGroup.clear(screen, back)
        playerGroup.clear(screen, back)
        backgroundGroup.update(screen)
        monsterGroup.update(screen)
        playerGroup.update(mouseX, mouseY)
        backgroundGroup.draw(screen)
        monsterGroup.draw(screen)
        playerGroup.draw(screen)

        pygame.display.flip()
                
    pygame.quit()

if __name__ == "__main__":
    main()
            




    
