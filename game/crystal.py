import pygame, sys
from pygame.locals import *
from spritesheet import SpriteSheet
from config import *


class Crystal:
    def __init__(self, surface, image, rect):
        self.image = image
        self.rect = Rect(rect)
        self.max_health = 1000
        self.health = 1000
        self.__surface = surface
        self.HealthRect = Rect(250, 570, 300, 4)
        self.x = self.rect.x
        self.y = self.rect.y
    def draw(self):
        self.__surface.blit(self.image, self.rect)
        #To Do: Draw Health Bar
        pygame.draw.rect(self.__surface, (255,0,0), self.HealthRect)
        ratio = self.health / self.max_health
        gRect = Rect(self.HealthRect)
        gRect.w *= ratio
        pygame.draw.rect(self.__surface, (0,255,0), gRect)

    def damage(self, points):
        self.health -= points
        
        
