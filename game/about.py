import pygame
from player import *
from pygame.locals import *
def displayAbout():
    font = pygame.font.Font('freesansbold.ttf', 50)
    textUpper = font.render('Objective', True, (255,255,255))
    textUpperRect = textUpper.get_rect()
    textUpperRect.x = MAX_WIDTH / 2  - textUpperRect.w/2
    textUpperRect.y = 150

    textLower = font.render('of Ulumok', True, (255,255,255))
    textLowerRect = textLower.get_rect()
    textLowerRect.x = MAX_WIDTH / 2 - textLowerRect.w/2
    textLowerRect.y = 200
    background = pygame.image.load('map.jpg')

    font = pygame.font.Font('freesansbold.ttf', 15)
    textW = font.render("The objective of the game is to protect the sacred Crystal of Ulumok for as long as you can", True, (255,255,255))
    textWRect = textW.get_rect()
    textWRect.x = MAX_WIDTH / 2 - textWRect.w/2
    textWRect.y = 225

    font = pygame.font.Font('freesansbold.ttf', 15)
    textA = font.render('The game ends when you either run out of lives or the Crystal runs out of health.', True, (255,255,255))
    textARect = textA.get_rect()
    textARect.x = MAX_WIDTH / 2 - textARect.w/2
    textARect.y = 250

    textS = font.render("You get 50 points for each enemy killed and 250 for each wave completed.", True, (255,255,255))
    textSRect = textS.get_rect()
    textSRect.x = MAX_WIDTH / 2 - textSRect.w/2
    textSRect.y = 275

    font = pygame.font.Font('freesansbold.ttf', 15)
    textD = font.render('Will you go down as Ulumok\'s greatest warrior,', True, (255,255,255))
    textDRect = textD.get_rect()
    textDRect.x = MAX_WIDTH / 2 - textDRect.w/2
    textDRect.y = 300

    textSpace = font.render(' or just another peasant vanquished by the Undead Hoarde?', True, (255,255,255))
    textSpaceRect = textD.get_rect()
    textSpaceRect.x = MAX_WIDTH / 2 - (textDRect.w/2 + 50)
    textSpaceRect.y = 325
    
    textE = font.render('[Enter]: Confirm', True, (255,255,255))
    textERect = textD.get_rect()
    textERect.x = MAX_WIDTH / 2 - (textERect.w/2 + 25)
    textERect.y = 350
    
    background = pygame.image.load('map.jpg')


    exitBool = False
    while(not exitBool):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    exitBool = True
                break
                
                        #Player Movement
        surface.blit(background, (0,0))
        surface.blit(textUpper, textUpperRect)
        #surface.blit(textLower, textLowerRect)
        #surface.blit(textStart, textStartRect)
        surface.blit(textW, textWRect)
        surface.blit(textA, textARect)
        surface.blit(textS, textSRect)
        surface.blit(textD, textDRect)
        surface.blit(textSpace, textSpaceRect)
        #surface.blit(textE, textERect)
        
        
        #surface.blit(textHelp, textHelpRect)
        #pygame.draw.rect(surface, (255, 255,0), oRect)
        #drawPlayer(surface, playerRect.x, playerRect.y)
        pygame.display.flip()
        pygame.time.delay(1)
