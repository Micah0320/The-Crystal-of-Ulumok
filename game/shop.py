import pygame
from player import *
from pygame.locals import *
import random
def shop(surface, player, crystal):
    item = pygame.image.load('itemGem.png')
    itemRect1 = item.get_rect(topleft=(MAX_WIDTH/2 - 16, MAX_HEIGHT/2 - 16))
    itemRect0 = Rect(itemRect1)
    itemRect0.x -= 32 * 6
    itemRect2 = Rect(itemRect1)
    itemRect2.x += 32 * 6
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render('Tiny\'s Big Item Shop', True, (255,255,255))
    textRect = text.get_rect()
    textRect.x = 210
    textRect.y = 150

    goldtext = font.render('Gold: ' + str(player.gold), True, (255,255,255))
    goldtextRect = goldtext.get_rect()
    goldtextRect.x = 210
    goldtextRect.y = 180
    
    background = pygame.image.load('tavern.jpg')
    frame = 0
    items = ['Crystal of Life', 'Speed Crystal', 'Crystal Rabbit\'s Foot', 'Reinforced Gem-Plating', 'Gem Buffing', 'Heart of Ulumok']
    itemPrice = [500, 750, 1000, 1500, 500, 1750]
    itemGet = []
    itemsPurchased = []
    #Puts the items in the shop randomly
    while len(itemGet) < 3:
        stock = random.randint(0, len(items) - 1)
        #if the item already in shop, get new item
        itemGet.append(stock)
        s = set(itemGet)
        itemGet = list(s)
    font = pygame.font.Font('freesansbold.ttf', 16)

    textItem0 = font.render(items[itemGet[0]], True, (255,255,255))
    textItem0Rect = textItem0.get_rect()
    textItem0Rect.x = itemRect0.x - textItem0Rect.w / 2
    textItem0Rect.y = itemRect0.y + 50

    textItemPrice0 = font.render(str(itemPrice[itemGet[0]]), True, (255,255,255))
    textItemPrice0Rect = textItemPrice0.get_rect()
    textItemPrice0Rect.x = itemRect0.x 
    textItemPrice0Rect.y = itemRect0.y + 75

    textItem1 = font.render(items[itemGet[1]], True, (255,255,255))
    textItem1Rect = textItem1.get_rect()
    textItem1Rect.x = itemRect1.x - textItem1Rect.w / 2
    textItem1Rect.y = itemRect1.y + 50

    textItemPrice1 = font.render(str(itemPrice[itemGet[1]]), True, (255,255,255))
    textItemPrice1Rect = textItemPrice1.get_rect()
    textItemPrice1Rect.x = itemRect1.x
    textItemPrice1Rect.y = itemRect1.y + 75

    textItem2 = font.render(items[itemGet[2]], True, (255,255,255))
    textItem2Rect = textItem2.get_rect()
    textItem2Rect.x = itemRect2.x - textItem2Rect.w / 2
    textItem2Rect.y = itemRect2.y + 50

    textItemPrice2 = font.render(str(itemPrice[itemGet[2]]), True, (255,255,255))
    textItemPrice2Rect = textItemPrice2.get_rect()
    textItemPrice2Rect.x = itemRect2.x
    textItemPrice2Rect.y = itemRect2.y + 75

    Exit = False
    option = 0
    oRect = Rect(itemRect0)
    oRect.w += 1
    oRect.h += 2
    # Shop Loop
    while(not Exit):
        oRect.x = itemRect0.x + (32 * 6 * option)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == K_a or event.key == K_LEFT):
                    #print("a pressed")
                    if option > 0:
                        option -= 1
                    break
                if (event.key == K_d or event.key == K_RIGHT):
                    if option < 2:
                        option += 1

                if event.key == K_RETURN:
                    price = itemPrice[itemGet[option]]
                    if player.gold >= price:
                        if itemGet[option] == 0:
                            player.lives += 1
                            player.gold -= price
                        elif itemGet[option] == 1:
                            if player.speed_level <= 5:
                                player.speed_level += 1
                                player.gold -= price
                        elif itemGet[option] == 2:
                            player.luck += 1
                            player.gold -= price
                        elif itemGet[option] == 3:
                            crystal.max_health += 250
                            crystal.health += 250
                            player.gold -= price
                        elif itemGet[option] == 4:
                            if crystal.health + 250 > crystal.max_health:
                                crystal.health = crystal.max_health
                            else:
                                crystal.health += 250
                            player.gold -= price
                        elif itemGet[option] == 5:
                            if crystal.regen <= 5:
                                crystal.regen += 1
                            player.gold -= price
                if event.key == K_ESCAPE:
                    Exit = True
        font = pygame.font.Font('freesansbold.ttf', 32)
        goldtext = font.render('Gold: ' + str(player.gold), True, (255,255,255))
        goldtextRect = goldtext.get_rect()
        goldtextRect.x = 210
        goldtextRect.y = 180
        surface.blit(background, (0,0))
        pygame.draw.rect(surface, (255, 255,0), oRect)
        
        surface.blit(item, itemRect0)
        surface.blit(textItem0, textItem0Rect)
        surface.blit(textItemPrice0, textItemPrice0Rect)

        surface.blit(item, itemRect1)
        surface.blit(textItem1, textItem1Rect)
        surface.blit(textItemPrice1, textItemPrice1Rect)

        surface.blit(item, itemRect2)
        surface.blit(textItem2, textItem2Rect)
        surface.blit(textItemPrice2, textItemPrice2Rect)

        surface.blit(text, textRect)
        surface.blit(goldtext, goldtextRect)
        #pygame.draw.rect(surface, (255, 255,0), oRect)
        pygame.display.flip()
        pygame.time.delay(1)
