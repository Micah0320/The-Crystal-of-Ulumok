import pygame
from pygame.locals import *
pygame.init()
global WAVE
WAVE = 1
ENEMY_COUNT = 0
BLACK = (0,0,0)
BLUE = (0, 0, 255)
MAX_WIDTH = 800
MAX_HEIGHT = 600
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64
delay = True
moving = False
attacking = False
playerX = MAX_WIDTH / 2 - 32
playerY = MAX_HEIGHT / 2 - (75 + 32)
dx = 0
dy = 0

surface = pygame.display.set_mode([MAX_WIDTH, MAX_HEIGHT])
background = pygame.image.load('map.jpg')

CRYSTAL_IMG = pygame.image.load('crystal.png')
pygame.display.set_icon(CRYSTAL_IMG)
CRYSTAL_RECT = CRYSTAL_IMG.get_rect(topleft=(MAX_WIDTH/2 - 16, MAX_HEIGHT/2 - 16))

playerRect = Rect(playerX - 32, playerY -32, 64, 64)

font = pygame.font.Font('freesansbold.ttf', 20)
#wave_text = font.render(Wave_string, False, (255,255,255))


def drawWave(wave_text, waveTextRect):
    surface.blit(wave_text, waveTextRect)
