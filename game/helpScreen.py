import pygame
from player import *
from pygame.locals import *
def displayHelp():
    font = pygame.font.Font('freesansbold.ttf', 50)
    textUpper = font.render('Controls', True, (255,255,255))
    textUpperRect = textUpper.get_rect()
    textUpperRect.x = MAX_WIDTH / 2  - textUpperRect.w/2
    textUpperRect.y = 150

    textLower = font.render('of Ulumok', True, (255,255,255))
    textLowerRect = textLower.get_rect()
    textLowerRect.x = MAX_WIDTH / 2 - textLowerRect.w/2
    textLowerRect.y = 200
    background = pygame.image.load('map.jpg')

    font = pygame.font.Font('freesansbold.ttf', 15)
    textW = font.render("[W]/[Up Arrow]- Move Forward", True, (255,255,255))
    textWRect = textW.get_rect()
    textWRect.x = MAX_WIDTH / 2 - textWRect.w/2
    textWRect.y = 225

    font = pygame.font.Font('freesansbold.ttf', 15)
    textA = font.render('[A]/[Left Arrow]: Move Left/Make Selection', True, (255,255,255))
    textARect = textA.get_rect()
    textARect.x = MAX_WIDTH / 2 - textARect.w/2
    textARect.y = 250

    textS = font.render("[S]/[Down Arrow]- Move Backwards", True, (255,255,255))
    textSRect = textS.get_rect()
    textSRect.x = MAX_WIDTH / 2 - textSRect.w/2
    textSRect.y = 275

    font = pygame.font.Font('freesansbold.ttf', 15)
    textD = font.render('[D]/[Right Arrow]: Move Right/Make Selection', True, (255,255,255))
    textDRect = textD.get_rect()
    textDRect.x = MAX_WIDTH / 2 - textDRect.w/2
    textDRect.y = 300

    textSpace = font.render('[Space]/[Mouse]: Attack', True, (255,255,255))
    textSpaceRect = textD.get_rect()
    textSpaceRect.x = MAX_WIDTH / 2 - textDRect.w/4
    textSpaceRect.y = 325
    
    textE = font.render('[Enter]: Confirm', True, (255,255,255))
    textERect = textD.get_rect()
    textERect.x = MAX_WIDTH / 2 - textDRect.w/4
    textERect.y = 350

    textEs = font.render('[ESC]: Exit Shop/Exit Game', True, (255,255,255))
    textEsRect = textD.get_rect()
    textEsRect.x = MAX_WIDTH / 2 - textDRect.w/4
    textEsRect.y = 375
    
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
        surface.blit(textE, textERect)
        surface.blit(textEs, textEsRect)
        
        
        #surface.blit(textHelp, textHelpRect)
        #pygame.draw.rect(surface, (255, 255,0), oRect)
        #drawPlayer(surface, playerRect.x, playerRect.y)
        pygame.display.flip()
        pygame.time.delay(1)
