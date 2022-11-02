import pygame
from player import *
from pygame.locals import *
def setup(surface):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Choose Your Fighter', True, (255,255,255))
    textRect = text.get_rect()
    textRect.x = 210
    textRect.y = 150
    background = pygame.image.load('tavern.jpg')
    frame = 0
    playerRect = Rect(400 - 200, 300, 64, 64)
    wizardRect = Rect(400 + 100, 300, 64, 64)
    
    # main Loop, Extrapolate to a function
    direction = 'S'
    animation = playerForwardWalk
    animation2 = wizardForwardWalk
    ms = 0
    reverse = False
    option = 0
    oRect = Rect(playerRect)
    oRect.w += 1
    oRect.h += 2
    
    playerImageF = None
    playerImageB = None
    playerImageL = None
    playerImageR = None

    playerAttackF = None
    playerAttackB = None
    playerAttackL = None
    playerAttackR = None
    
    while(playerImageF == None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    #print("a pressed")
                    option = 0
                    oRect.x = playerRect.x
                    oRect.y = playerRect.y
                    break
                elif event.key == K_d:
                    option = 1
                    oRect.x = wizardRect.x
                    oRect.y = wizardRect.y
                    break
                if event.key == K_RETURN:
                    #print("Enter Pressed")
                    if option == 0:
                        playerImageF = playerForwardWalk
                        playerImageB = playerBackWalk
                        playerImageL = playerLeftWalk
                        playerImageR = playerRightWalk
                        playerAttackF = playerForwardAttack
                        playerAttackB = playerBackAttack
                        playerAttackL = playerLeftAttack
                        playerAttackR = playerRightAttack
                        playerDeath = knightDeath
                        playerType = 'Knight'
    
                    else:
                        playerImageF = wizardForwardWalk
                        playerImageB = wizardBackWalk
                        playerImageL = wizardLeftWalk
                        playerImageR = wizardRightWalk
                        playerAttackF = wizardForwardAttack
                        playerAttackB = wizardBackAttack
                        playerAttackL = wizardLeftAttack
                        playerAttackR = wizardRightAttack
                        playerDeath = wizardDeath
                        playerType = 'Wizard'
    
                
                        #Player Movement
                    return (playerImageF,playerImageB, playerImageL, playerImageR, playerAttackF, playerAttackB, playerAttackL, playerAttackR, playerDeath, playerType)
                        #dx, dy = update(dx, dy)
                        #playerX, playerY = move(playerX, playerY, dx, dy)
                        #playerRect.x, playerRect.y = playerX, playerY
                        #print(dx, dy)
        if direction == 'N':
            animation = playerBackWalk
            animation2 = wizardBackWalk
        elif direction == 'S':
            animation = playerForwardWalk
            animation2 = wizardForwardWalk
        elif direction == 'W':
            animation = playerLeftWalk
            animation2 = wizardLeftWalk
        elif direction == 'E':
            animation = playerRightWalk
            animation2 = wizardRightWalk
            
            
        surface.blit(background, (0,0))
        #drawPlayer(surface, playerX, playerY)
        #surface.blit(CRYSTAL_IMG, CRYSTAL_RECT)direction = update
        surface.blit(text, textRect)
        pygame.draw.rect(surface, (255, 255,0), oRect)
        surface.blit(animation[frame], playerRect)
        surface.blit(animation2[frame], wizardRect)
        #drawPlayer(surface, playerRect.x, playerRect.y)
        pygame.display.flip()
        pygame.time.delay(1)
        
        ms += 1
        if ms == 45:
            ms = 0
            if not reverse:
                frame += 1
            else:
                frame -=1
                
            if frame == 8:
                reverse = True
            if frame == 0:
                reverse = False
