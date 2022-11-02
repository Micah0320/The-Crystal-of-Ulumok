import pygame, sys
from pygame.locals import *
from spritesheet import SpriteSheet
from config import *
backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('KnightWalk.png')
player_image = spriteSheet.image_at(backWalkRect, -1)
playerBackWalk = [player_image]
for i in range(1, 9):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    playerBackWalk.append(player_image)

backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
playerLeftWalk = [player_image]
for i in range(1,9):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    playerLeftWalk.append(player_image)


backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
playerForwardWalk = [player_image]
for i in range(1,9):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    playerForwardWalk.append(player_image)

backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
playerRightWalk = [player_image]
for i in range(1,9):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect,-1)
    playerRightWalk.append(player_image)

backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('KnightAttck.png')
player_image = spriteSheet.image_at(backWalkRect, -1)
playerBackAttack = [player_image]
for i in range(1, 5):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    playerBackAttack.append(player_image)

backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
playerLeftAttack = [player_image]
for i in range(1,5):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    playerLeftAttack.append(player_image)


backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
playerForwardAttack = [player_image]
for i in range(1,5):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    playerForwardAttack.append(player_image)

backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
playerRightAttack = [player_image]
for i in range(1,5):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect,-1)
    playerRightAttack.append(player_image)

backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('WizardWalk.png')
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardBackWalk = [player_image]
for i in range(1, 9):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    wizardBackWalk.append(player_image)

backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardLeftWalk = [player_image]
for i in range(1,9):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    wizardLeftWalk.append(player_image)


backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardForwardWalk = [player_image]
for i in range(1,9):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    wizardForwardWalk.append(player_image)

backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardRightWalk = [player_image]
for i in range(1,9):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    wizardRightWalk.append(player_image)

backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('WizardAttack.png')
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardBackAttack = [player_image]
for i in range(1, 5):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    wizardBackAttack.append(player_image)

backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardLeftAttack = [player_image]
for i in range(1,5):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    wizardLeftAttack.append(player_image)


backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardForwardAttack = [player_image]
for i in range(1,5):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    wizardForwardAttack.append(player_image)

backWalkRect.x = 0
backWalkRect.y += 65
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardRightAttack = [player_image]
for i in range(1,5):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect,-1)
    wizardRightAttack.append(player_image)

backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('KnightDeath.png')
player_image = spriteSheet.image_at(backWalkRect, -1)
knightDeath = [player_image]
for i in range(1, 6):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    knightDeath.append(player_image)

backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('WizardDeath.png')
player_image = spriteSheet.image_at(backWalkRect, -1)
wizardDeath = [player_image]
for i in range(1, 6):
    backWalkRect.x += 65
    player_image = spriteSheet.image_at(backWalkRect, -1)
    wizardDeath.append(player_image)



class Player:
    
    #Initialize the player
    def __init__(self, pRect, surface, walkF, walkB, walkL, walkR, attackF, attackB, attackL, attackR, death, classType):
        self.dx = 0
        self.dy = 0
        self.x = pRect.x
        self.y = pRect.y
        self.frame = 0
        self.classType = classType
        self.attacking = False
        self.moving = False
        self.reverse = False
        self.direction = 'N'
        self.ms = 0
        self.walk_animation = None
        self.master_walk = []
        self.attack_animation = None
        self.master_attack = []
        self.animation = walkF
        self.rect = Rect(pRect)
        self.__surface = surface
        self.master_walk.append(walkF)
        self.master_walk.append(walkB)
        self.master_walk.append(walkL)
        self.master_walk.append(walkR)
        self.master_attack.append(attackF)
        self.master_attack.append(attackB)
        self.master_attack.append(attackL)
        self.master_attack.append(attackR)
        self.spell = pygame.image.load('spell.png').convert()
        self.spell.set_alpha(100)
        self.deathAnimation = False
        self.death = death
        self.alive = True
        self.lives = 3
        self.score = 0
        self.gold = 0

    def draw(self):
        #print(self.frame)
        #Gets Lives for player and displays it on the screen
        live_string = ("Lives: %s" %self.lives)
        live_text = font.render(live_string, True, (255,255,255))
        liveTextRect = live_text.get_rect()
        liveTextRect.x = MAX_WIDTH - 100
        liveTextRect.y = 45

        score_string = ("Score: %s" %self.score)
        score_text = font.render(score_string, True, (255,255,255))
        scoreTextRect = score_text.get_rect()
        scoreTextRect.x = 0
        scoreTextRect.y = 25

        #gold_string = ("Gold: %s" %self.gold)
        #gold_text = font.render(gold_string, True, (255,255,255))
        #goldTextRect = score_text.get_rect()
        #goldTextRect.x = MAX_WIDTH - 100
        #goldTextRect.y = 65


        #if self.classType == 'Wizard' and self.attacking:
            #self.__surface.blit(self.spell, self.rect)
        self.__surface.blit(self.animation[self.frame], self.rect)
        self.__surface.blit(live_text, liveTextRect)
        self.__surface.blit(score_text, scoreTextRect)
        #self.__surface.blit(gold_text, goldTextRect)

    def setAnimation(self):
        if self.deathAnimation:
            self.animation = self.death
            self.dx = 0
            self.dy = 0
            self.moving = 0
            return
        if self.direction == 'N':
            self.walk_animation = self.master_walk[1]
            self.attack_animation = self.master_attack[1]
            if self.attacking:
                self.animation = self.attack_animation
            else:
                self.animation = self.walk_animation
        if self.direction == 'S':
            self.walk_animation = self.master_walk[0]
            self.attack_animation = self.master_attack[0]
            if self.attacking:
                self.animation = self.attack_animation
            else:
                self.animation = self.walk_animation
        if self.direction == 'E':
            self.walk_animation = self.master_walk[3]
            self.attack_animation = self.master_attack[3]
            if self.attacking:
                self.animation = self.attack_animation
            else:
                self.animation = self.walk_animation
        if self.direction == 'W':
            self.walk_animation = self.master_walk[2]
            self.attack_animation = self.master_attack[2]
            if self.attacking:
                self.animation = self.attack_animation
            else:
                self.animation = self.walk_animation

    def checkAttack(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                #print("click")
                self.dx = 0
                self.dy = 0
                self.attacking = True
                self.moving = False
                self.frame = 0
                self.ms = 0
                #self.animation = setAnimation()
            #print("To be Implemented(Left Click)")
            if event.button == 3:
                self.dx = 0
                self.dy = 0
                self.attacking = True
                self.moving = False
                self.frame = 0
                self.ms = 0
                #self.animation = setAnimation()
            #print("To be Implemented(Right Click)")
    def updatePlayer(self, event):
        if event.type == KEYDOWN:
            key = event.key
            #print(key)
            if key == K_UP:
                self.dy = -.35
                self.direction = 'N'
                self.moving = True
            elif key == K_w:
                self.dy = -.35
                self.direction = 'N'
                self.moving = True

            elif key == K_DOWN:
                #print("KeyDown")
                self.dy = 0.35
                self.direction = 'S'
                self.moving = True
            elif key == K_s:
                #print("South")
                self.dy = 0.35
                self.direction = 'S'
                self.moving = True
                
            elif key == K_RIGHT:
                self.dx = 0.35
                self.direction = 'E'
                self.moving = True
                return
            elif key == K_d:
                self.dx = 0.35
                self.direction = 'E'
                self.moving = True
                return
            
            elif key == K_LEFT:
                self.dx = -0.35
                self.direction = 'W'
                self.moving = True
                
                
            elif key == K_a:
                self.dx = -0.35
                self.direction = 'W'
                self.moving = True
            elif key == K_SPACE:
                self.dx = 0
                self.dy = 0
                self.attacking = True
                self.moving = False
                self.frame = 0
                self.ms = 0
                
        elif event.type == KEYUP:
            key = event.key
            #print(key, pygame.key.name(key))
            if key == K_UP:
                self.frame = 0
                self.dy = 0
                self.direction = 'N'
                self.moving = False
            elif key == K_w:
                self.frame = 0
                self.dy = 0
                self.direction = 'N'
                self.moving = False
            elif key == K_DOWN or key == K_s:
                self.frame = 0
                self.dy = 0
                self.direction = 'S'
                self.moving = False
            elif key == K_LEFT or key == K_a:
                self.frame = 0
                self.dx = 0
                self.direction = 'W'
                self.moving = False
            elif key == K_RIGHT or key == K_d:
                self.frame = 0
                self.dx = 0
                self.direction = 'E'
                self.moving = False

    #TO-DO: Move Function
    def move(self, crystal):
        prect = Rect(self.rect)
        #print(self.dx, self.rect.x)
        prect.x = self.x + self.dx
        #print(prect.x)
        prect.y = self.y + self.dy
        if prect.colliderect(CRYSTAL_RECT):
            return
        if (self.rect.x + self.dx < MAX_WIDTH - (self.rect.w * 2) and self.rect.x + self.dx > self.rect.w):
            #print(self.rect.x + self.dx)
            self.x += self.dx
            self.rect.x = self.x
            #print(self.rect.x, self.dx)
        if self.rect.y + self.dy < MAX_HEIGHT - (self.rect.h * 2) and self.rect.y + self.dy > self.rect.h:
            self.y += self.dy
            self.rect.y = self.y
        
    #TO-DO: Run Function
    def run(self, crystal, event):
        if not self.attacking and not self.deathAnimation:
            self.checkAttack(event)
        if not self.attacking and not self.deathAnimation:
            self.updatePlayer(event)
        self.setAnimation()
        if self.moving:
            self.move(crystal)
        
    def updateFrame(self):
        if self.moving or self.attacking or self.deathAnimation:
            self.ms += 1
            if self.ms == 45:
                self.ms = 0
                if self.moving and not self.attacking:
                    if self.frame == 8:
                        self.reverse = True
                    if self.frame == 0:
                        self.reverse = False
                if self.attacking:
                    if self.frame < 0:
                        self.frame = 0
                        self.attacking = False
                    if self.frame == 4:
                        self.attacking = False
                        self.reverse = False
                        self.moving = False
                        self.frame = 0
                if self.deathAnimation:
                    if self.reverse:
                        self.reverse = False
                    if self.frame >= 5:
                        self.attacking = False
                        self.deathAnimation = False
                        self.reverse = False
                        self.moving = False
                        self.alive = True
                        self.frame = 0
                        self.lives -= 1
                        self.x = MAX_WIDTH / 2 - 32
                        self.y = MAX_HEIGHT / 2 - (75 + 32)
                        self.rect.x = self.x
                        self.rect.y = self.y
                if not self.reverse:
                    self.frame += 1
                else:
                    self.frame -=1
                
        else:
            self.ms = 0
            self.frame = 0
    






