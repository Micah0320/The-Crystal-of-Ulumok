import pygame
from player import *
from pygame.locals import *
from helpScreen import *
from displayScore import *
from about import *
def displayTitle():
    font = pygame.font.Font('freesansbold.ttf', 50)
    textUpper = font.render('The Crystal', True, (255,255,255))
    textUpperRect = textUpper.get_rect()
    textUpperRect.x = MAX_WIDTH / 2  - textUpperRect.w/2
    textUpperRect.y = 150

    textLower = font.render('of Ulumok', True, (255,255,255))
    textLowerRect = textLower.get_rect()
    textLowerRect.x = MAX_WIDTH / 2 - textLowerRect.w/2
    textLowerRect.y = 200
    background = pygame.image.load('map.jpg')

    font = pygame.font.Font('freesansbold.ttf', 25)
    textStart = font.render('[Enter]: Start Game', True, (255,255,255))
    textStartRect = textStart.get_rect()
    textStartRect.x = MAX_WIDTH / 2 - textLowerRect.w/2
    textStartRect.y = 350

    font = pygame.font.Font('freesansbold.ttf', 25)
    textHelp = font.render('[h]: Help Menu', True, (255,255,255))
    textHelpRect = textStart.get_rect()
    textHelpRect.x = MAX_WIDTH / 2 - textLowerRect.w/2
    textHelpRect.y = 375

    font = pygame.font.Font('freesansbold.ttf', 25)
    textScore = font.render('[s]: Show Scores', True, (255,255,255))
    textScoreRect = textStart.get_rect()
    textScoreRect.x = MAX_WIDTH / 2 - textLowerRect.w/2
    textScoreRect.y = 400
    
    font = pygame.font.Font('freesansbold.ttf', 25)
    textAb = font.render('[a]: About', True, (255,255,255))
    textAbRect = textStart.get_rect()
    textAbRect.x = MAX_WIDTH / 2 - (textLowerRect.w/2)
    textAbRect.y = 425
    
    background = pygame.image.load('map.jpg')


    exitBool = False
    while(not exitBool):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_h:
                    displayHelp()
                elif event.key == K_s:
                    displayScore(surface)
                elif event.key == K_a:
                    displayAbout()
                elif event.key == K_RETURN:
                    exitBool = True
                elif event.key == K_ESCAPE:
                    sys.exit()
                break
                
                        #Player Movement
        surface.blit(background, (0,0))
        surface.blit(textUpper, textUpperRect)
        surface.blit(textLower, textLowerRect)
        surface.blit(textStart, textStartRect)
        surface.blit(textHelp, textHelpRect)
        surface.blit(textScore, textScoreRect)
        surface.blit(textAb, textAbRect)
        #pygame.draw.rect(surface, (255, 255,0), oRect)
        #drawPlayer(surface, playerRect.x, playerRect.y)
        pygame.display.flip()
        pygame.time.delay(1)
        
