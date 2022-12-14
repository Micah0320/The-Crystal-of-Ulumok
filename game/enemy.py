import pygame, sys, random
from pygame.locals import *
from spritesheet import SpriteSheet
from config import *

backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('EnemyWalk.png')
enemy_image = spriteSheet.image_at(backWalkRect, -1)
enemyBackWalk = [enemy_image]
for i in range(1, 9):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect, -1)
    enemyBackWalk.append(enemy_image)

backWalkRect.x = 0
backWalkRect.y += 65
enemy_image = spriteSheet.image_at(backWalkRect, -1)
enemyLeftWalk = [enemy_image]
for i in range(1,9):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect, -1)
    enemyLeftWalk.append(enemy_image)


backWalkRect.x = 0
backWalkRect.y += 65
enemy_image = spriteSheet.image_at(backWalkRect, -1)
enemyForwardWalk = [enemy_image]
for i in range(1,9):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect, -1)
    enemyForwardWalk.append(enemy_image)

backWalkRect.x = 0
backWalkRect.y += 65
enemy_image = spriteSheet.image_at(backWalkRect, -1)
enemyRightWalk = [enemy_image]
for i in range(1,9):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect,-1)
    enemyRightWalk.append(enemy_image)

backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('EnemyAttack.png')
enemy_image = spriteSheet.image_at(backWalkRect, -1)
enemyBackAttack = [enemy_image]
for i in range(1, 5):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect, -1)
    enemyBackAttack.append(enemy_image)

backWalkRect.x = 0
backWalkRect.y += 65
enemy_image = spriteSheet.image_at(backWalkRect, -1)
enemyLeftAttack = [enemy_image]
for i in range(1,5):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect, -1)
    enemyLeftAttack.append(enemy_image)


backWalkRect.x = 0
backWalkRect.y += 65
enemty_image = spriteSheet.image_at(backWalkRect, -1)
enemyForwardAttack = [enemy_image]
for i in range(1,5):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect, -1)
    enemyForwardAttack.append(enemy_image)

backWalkRect.x = 0
backWalkRect.y += 65
enemy_image = spriteSheet.image_at(backWalkRect, -1)
enemyRightAttack = [enemy_image]
for i in range(1,5):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect,-1)
    enemyRightAttack.append(enemy_image)

backWalkRect = Rect(0,0, 64, 64)
spriteSheet = SpriteSheet('EnemyDeath.png')
enemy_image = spriteSheet.image_at(backWalkRect, -1)
enemyDeath = [enemy_image]
for i in range(1, 6):
    backWalkRect.x += 65
    enemy_image = spriteSheet.image_at(backWalkRect, -1)
    enemyDeath.append(enemy_image)

def get_start(num):
    i = random.randint(0, 3)
    if i == 0:
        return (MAX_WIDTH / 2, -64 - (num * 64))
    elif i == 1:
        return (MAX_WIDTH + (num * 64), MAX_HEIGHT / 2)

    elif i == 2:
        return (MAX_WIDTH / 2, MAX_HEIGHT + (num * 64))
    else:
        return (-64 - (num * 64), MAX_HEIGHT / 2)



def get_wave(ENEMY_COUNT = 0, WAVE = 1):
    base = 3 * ((WAVE // 5) + 1) + WAVE
    random_element = random.randint(1 + (WAVE // 5), WAVE + 1)
    #print("BASE: ", base, "RANDOM: ", random_element, "WAVE: ", WAVE)
    if ENEMY_COUNT == 0:
        ENEMY_COUNT = base + random_element
    #print(ENEMY_COUNT)
    ret = []
    for i in range(ENEMY_COUNT):
        x, y = get_start(i)
        e = enemy(Rect(x, y, 64, 64), surface, enemyForwardWalk, enemyBackWalk, enemyLeftWalk, enemyRightWalk, enemyForwardAttack, enemyBackAttack, enemyLeftAttack, enemyRightAttack, enemyDeath)
        ret.append(e)
    return ret
    

class enemy:
    def __init__(self, rect, surface, walkF, walkB, walkL, walkR, attackF, attackB, attackL, attackR, death, alive = True):
        self.dx = 0
        self.dy = 0
        self.x = rect.x
        self.y = rect.y
        self.frame = 0
        self.attacking = False
        self.moving = True
        self.reverse = False
        self.direction = 'N'
        self.ms = 0
        self.walk_animation = None
        self.master_walk = []
        self.attack_animation = None
        self.master_attack = []
        self.animation = walkF
        self.rect = Rect(rect)
        self.__surface = surface
        self.master_walk.append(walkF)
        self.master_walk.append(walkB)
        self.master_walk.append(walkL)
        self.master_walk.append(walkR)
        self.master_attack.append(attackF)
        self.master_attack.append(attackB)
        self.master_attack.append(attackL)
        self.master_attack.append(attackR)
        self.death = death
        self.distance_Player = 99999
        self.distance_goal = 99999
        self.alive = alive
        self.deathAnimation = False
        self.time = 0
        self.Target = 'NONE'
        self.pause = False
        self.sound = pygame.mixer.Sound('enemyDeath.wav')
        self.swingSound = pygame.mixer.Sound('SwordSound.mp3')
    def draw(self):
        #print(self.pause)
        #print(self.alive, self.moving, self.deathAnimation, self.attacking, self.pause, self.frame, self.ms)
        if self.alive:
            if self.deathAnimation and self.time == 0:
                self.__surface.blit(self.animation[self.time], self.rect)
            else:
                self.__surface.blit(self.animation[self.frame], self.rect)

    def setAnimation(self):
        if self.deathAnimation:
            self.animation = self.death
            #self.frame = 0
            #self.ms = 0
            return
        if self.dx == 0:
            if self.dy < 0 or self.y > MAX_HEIGHT:
                self.direction == 'N'
            else:
                self.direction == 'S'
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
    def get_distance(self, obj):
        return(abs(self.x - obj.x) + abs(self.y - obj.y))

    def get_player_dist(self, player):
        self.distance_Player = self.get_distance(player)

    def get_crystal_dist(self, crystal):
        self.distance_goal = self.get_distance(crystal)
    #To Fix
    def move(self, crystal):
        prect = Rect(self.rect)
        #print(self.dx, self.rect.x)
        prect.x = self.x + self.dx
        #print(prect.x)
        prect.y = self.y + self.dy
        #if prect.colliderect(CRYSTAL_RECT):
            #return
        #if (self.rect.x + self.dx < MAX_WIDTH - (self.rect.w * 2) and self.rect.x + self.dx > self.rect.w):
            #print(self.rect.x + self.dx)
        self.x += self.dx
        self.rect.x = self.x
            #print(self.rect.x, self.dx)
       # if self.rect.y + self.dy < MAX_HEIGHT - (self.rect.h * 2) and self.rect.y + self.dy > self.rect.h:
        self.y += self.dy
            #print("Moving Vertically")
            #print(self.y)
        self.rect.y = self.y
    #To Fix
    def run(self, player, crystal, WAVE = WAVE):
        #print(self.frame)
        self.get_player_dist(player.rect)
        self.get_crystal_dist(crystal)
        if self.alive and not self.deathAnimation:
            if self.distance_Player < self.distance_goal and not self.attacking:
                if self.distance_Player >= 50:
                    if self.x > player.x + 10:
                        self.direction = 'W'
                        self.dx = -.25
                    elif self.x < player.x + 10:
                        self.direction = 'E'
                        self.dx = .25
                    if self.rect.y < player.y:
                        #if self.y < 128:
                          #  self.direction = 'S'
                        
                        self.dy = .25
                    elif self.rect.y > player.y:
                        #print("UP")
                        #if self.y > 480:
                         #   self.direction = 'N'
                        self.dy = -.25
                        
                else:
                    #self.Target == 'PLAYER'
                    #print(self.Target, self.attacking, self)
                    if player.attacking and not self.deathAnimation:
                        self.deathAnimation = True
                        pygame.mixer.Sound.play(self.sound)
                        player.score += 50
                        if player.luck > 0:
                            player.gold += random.randint(1, player.luck) * 10
                        player.gold += random.randint(50, 75)
                        self.moving = False
                        self.pause = False
                        self.attaking = False
                        self.frame = 0
                        self.ms = 0
                    elif self.pause == False and not self.attacking:
                        self.pause = True
                        self.dx = 0
                        self.dy = 0
                        self.moving = False
                        self.reverse = False
                        self.frame = 0
            elif self.Target == 'NONE' and self.attacking:
                if self.distance_Player <= 50:
                    player.deathAnimation = True
                pygame.mixer.Sound.play(self.swingSound)
                #print(player.deathAnimation)
                #player.frame = 0
                #player.ms = 0
                self.Target = 'NONE'
            else:
                if self.distance_goal <= 50:
                    #(self.frame)
                    #print(self.attacking)
                    if not self.attacking:
                        if self.x < crystal.x:
                            self.direction = 'E'
                        else:   self.direction = 'W'
                        self.moving = False
                        self.attacking = True
                        pygame.mixer.Sound.play(self.swingSound)
                        self.reverse = False
                        self.Target = 'Crystal'
                        self.frame = 0
                        self.dx = 0
                        self.dy = 0
                    if self.attacking:
                        crystal.damage(.01 + (0.05 * (WAVE / 10)))
                else:
                    #print(self.dx)
                    if self.x > crystal.x + 16:
                        #if (self.y >= crystal.y + 32 and self.y <= crystal.y + 32):
                        self.direction = 'W'
                        self.dx = -.25
                    elif self.x < crystal.x:
                        #if (self.y >= crystal.y + 32 and self.y <= crystal.y + 32):
                        self.direction = 'E'
                        self.dx = .25
                    if self.y < crystal.y:
                        if self.dx  == 0:
                            self.direction = 'S'
                        self.dy = .25
                    elif self.y > crystal.y:
                        self.dy = -.25
                        if self.dx == 0:
                            self.direction = 'N'
            if self.moving:
                self.move(crystal.rect)

        
        self.setAnimation()
        #print(self.distance_Player, self.distance_goal)

    def updateFrame(self):
        if self.moving or self.attacking or self.deathAnimation:
            self.ms += 1
            if self.ms >= 45:
                self.ms = 0
                if self.moving and not self.attacking:
                    if self.frame == 8:
                        self.reverse = True
                    if self.frame == 0:
                        self.reverse = False
                if self.attacking:
                    if self.frame == 4:
                        self.attacking = False
                        self.reverse = False
                        self.moving = True
                        self.frame = 0
                        #self.Target = 'NONE'
                if self.deathAnimation:
                    #print(self.frame)
                    if self.reverse:
                        self.reverse = False
                    if self.frame == 3:
                        self.time += 1
                    if self.frame >= 5:
                        self.attacking = False
                        self.deathAnimation = False
                        self.reverse = False
                        self.moving = False
                        self.alive = False
                        self.frame = 0
                
                if not self.reverse:
                    self.frame += 1
                else:
                    self.frame -=1
        elif self.pause:
            self.ms += 1
            if self.ms >= 125:
                self.attacking = True
                self.ms = 0
                self.frame = 0
                self.pause = False
        elif not (self.pause or self.moving or self.attacking or self.deathAnimation):
            self.ms = 0
            self.deathAnimation = True
            self.frame = 0
                
        #else:
         #   self.ms = 0
          #  self.frame = 0
        
