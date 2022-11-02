import pygame
from player import *
from pygame.locals import *
def displayScore():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('SCORES', True, (255,255,255))
    textRect = text.get_rect()
    textRect.x = 340
    textRect.y = 50
    background = pygame.image.load('map.jpg')
    file = open('scores.txt', 'r')
    scores = []
    for i in range(10):
        score = file.readline()
        s, n = score.split(' ')
        n = n[:-1]
        scores.append((int(s),n))
    file.close()

    scoreText = []
    scoreRect = []
    exitBool = False
    font = pygame.font.Font('freesansbold.ttf', 32)
    for i in range(10):
        score = scores[i]
        s, n = score
        scoreText.append(font.render('%s. %s %s'%((i+1), s, n), True, (255,255,255)))
        sR = scoreText[i].get_rect()
        sR.x = 340
        sR.y = 50 * (i + 2)
        scoreRect.append(sR)      
    while(not exitBool):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                exitBool = True
                break
                
                        #Player Movement
        surface.blit(background, (0,0))
        #drawPlayer(surface, playerX, playerY)
        #surface.blit(CRYSTAL_IMG, CRYSTAL_RECT)direction = update
        surface.blit(text, textRect)
        for i in range(10):
            surface.blit(scoreText[i], scoreRect[i])
        #pygame.draw.rect(surface, (255, 255,0), oRect)
        #drawPlayer(surface, playerRect.x, playerRect.y)
        pygame.display.flip()
        pygame.time.delay(1)
        
