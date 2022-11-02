import pygame, sys
from pygame.locals import *
from config import *

from startUp import *
from displayScore import *
from enemy import *
from crystal import *
#playerForwardWalk, playerBackWalk, playerLeftWalk, playerRightWalk, playerForwardAttack, playerBackAttack, playerLeftAttack, playerRightAttack, playerDeath = setup(surface) 
#player = player(playerRect, surface, playerForwardWalk, playerBackWalk, playerLeftWalk, playerRightWalk, playerForwardAttack, playerBackAttack, playerLeftAttack, playerRightAttack, playerDeath)
 

#enemies = get_wave()
#print(len(enemies))
#Setting up, Move to config
pygame.display.set_caption("CISS145: GAME TITLE TBD")
def cleanUp(enemies):
    ret = []
    for e in enemies:
        if e.alive:
            ret.append(e)
    return ret

def updateWaveText():
    wave_text = font.render('WAVE: %s' % WAVE, True, (255,255,255))
    waveTextRect = wave_text.get_rect()
    waveTextRect.x = MAX_WIDTH - 100
    waveTextRect.y = 25
    return wave_text, waveTextRect

def handleDeath(player, enemies):
    if player.deathAnimation:
        for enemy in enemies:
            if not enemy.attacking:
                enemy.frame = 0
        if player.frame == 5:
            enemies = get_wave(ENEMY_COUNT)
        return enemies
    return enemies
def handleInitial():
    surface = pygame.display.set_mode([MAX_WIDTH, MAX_HEIGHT])
    background = pygame.image.load('map.jpg')
    font = pygame.font.Font('freesansbold.ttf', 20)
    name = "---"
    
    i = 0
    end = False
    while(i < 3):
        text = font.render('Enter Your Initials: %s' % name, True, (255,255,255))
        TextRect = text.get_rect()
        TextRect.x = MAX_WIDTH/2 - TextRect.w // 2
        TextRect.y = MAX_HEIGHT/2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN or i >= 3:
                    end = True
                if pygame.key.name(event.key) in 'abcdefghijklmnopqrstuvwxyz':
                    #print(event.key.name())
                    name = name[:i] + pygame.key.name(event.key) + name[i + 1:]
                    name.upper()
                    i += 1
                    #print(i)
                    
        if end:
            break
        surface.blit(background, (0,0))
        surface.blit(text, TextRect)
        pygame.display.flip()
        pygame.time.delay(1)
        
    return name.upper()
# main Loop, Extrapolate to a function
def play(player, crystal, enemies, WAVE = 1):
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not player.attacking and not player.deathAnimation:
                player.checkAttack(event)
            if not player.attacking and not player.deathAnimation:
                player.updatePlayer(event)
        if not player.deathAnimation:
            player.move(crystal.rect)
        player.setAnimation()
        for enemy in enemies:
            enemy.run(player, crystal)

        enemies = handleDeath(player, enemies)    
        
        
        surface.blit(background, (0,0))
        player.draw()
        for enemy in enemies:
            enemy.draw()
        crystal.draw()
        Wave_string = ("Wave: %s" % WAVE)
        wave_text = font.render(Wave_string, True, (255,255,255))
        waveTextRect = wave_text.get_rect()
        waveTextRect.x = MAX_WIDTH - 100
        waveTextRect.y = 25

        ENEMY_COUNT = len(enemies)
    
        drawWave(wave_text, waveTextRect)
        pygame.display.flip()
        pygame.time.delay(1)
        player.updateFrame()
        for enemy in enemies:
            enemy.updateFrame()
        enemies = cleanUp(enemies)
        if ENEMY_COUNT == 0:
            WAVE += 1
            enemies = get_wave(ENEMY_COUNT, WAVE)
            player.score += 250
            #End The Game
        if player.lives < 0 or crystal.health < 0:
            file = open('scores.txt', 'r')
            scores = []
            for i in range(10):
                score = file.readline()
                s, n = score.split(' ')
                n = n[:-1]
                scores.append((int(s),n))
            file.close()
            #TO-ADD: If the score is in higher than lowest score, prompt player to edit initials
            lowestS, nL = scores[-1]
            name = "---"
            if player.score > lowestS:
                name = handleInitial()
            myData = (player.score, name)
            scores.append(myData)
            scores.sort(key=lambda a: a[0], reverse = True)
            file = open('scores.txt', 'w')
            for i in range(10):
                s,n = scores[i]
                data = "%s %s\n" % (str(s),n)
                file.write(data)
            file.close()
            enemies.clear()
            
            break
while(True):
    #from startUp import *
    playerForwardWalk, playerBackWalk, playerLeftWalk, playerRightWalk, playerForwardAttack, playerBackAttack, playerLeftAttack, playerRightAttack, playerDeath, playerType = setup(surface)
    player = Player(playerRect, surface, playerForwardWalk, playerBackWalk, playerLeftWalk, playerRightWalk, playerForwardAttack, playerBackAttack, playerLeftAttack, playerRightAttack, playerDeath, playerType)
    crystal = Crystal(surface, CRYSTAL_IMG, CRYSTAL_RECT)
    enemies = get_wave()
    font = pygame.font.Font('freesansbold.ttf', 20)
    play(player, crystal, enemies)
    displayScore()
    
