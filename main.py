# Final project submission for cmput 275
# Ross Cockburn - section B1
# Ammar Mahdi   - section B2

import pygame
import sys
import time
import tile



pygame.init()

#initialize screen
window = pygame.display.set_mode((800,600))
import level
pygame.display.set_caption("test game")

#pygame variables
tile_blue = pygame.image.load("tile_blue.png").convert_alpha()
tile_green = pygame.image.load("tile_green.png").convert_alpha()
tile_red = pygame.image.load("tile_red.png").convert_alpha()
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

g = pygame.sprite.Group()
#g.add(bt)
window.fill(white)
l = level.Level('level1.txt')
l.drawTiles(window)

#game state variables
cameraPos = (0,0)
horScroll = 0
vertScroll = 0




def draw():
    g.draw(window)
    render()

#brings up menu
def menuLoop():
    window.fill(black)
    render()
    display_menu(window)

def render(): 
    pygame.display.flip()

gameLoop = True    
while gameLoop:
    clock.tick(60) #limits game speed
    render()





    #Check for keyboard or mouse input
    for event in pygame.event.get():
           
        if event.type==pygame.QUIT:
            pygame.display.quit()
            sys.exit()


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_RIGHT:
                horScroll = 1
            elif event.key == pygame.K_LEFT:
                horScroll = -1
            elif event.key == pygame.K_UP:
                vertScroll = -1
            elif event.key == pygame.K_DOWN:
                vertScroll = 1
            
                            
        elif event.type == pygame.KEYUP:
            #stop moving
            if event.key == pygame.K_RIGHT:
                if pygame.key.get_pressed()[K_LEFT] == True:
                    horScroll = -1
                else:
                    horScroll = 0

            if event.key == pygame.K_LEFT:
                if pygame.key.get_pressed()[K_RIGHT] == True:
                    horScroll = 1
                else:
                    horScroll = 0

            if event.key == pygame.K_UP:
                if pygame.key.get_pressed()[K_DOWN] == True:
                    vertScroll = 1
                else:
                    vertScroll = 0

            if event.key == pygame.K_DOWN:
                if pygame.key.get_pressed()[K_UP] == True:
                    vertScroll = -1
                else:
                    vertScroll = 0
           
                


    window.blit(tile_blue, (0, 0))
    render() #screen refresh
    clock.tick(60) #limits game speed
    
