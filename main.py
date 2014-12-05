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
#while gameLoop:
render()





    #Check for keyboard or mouse input
#    for event in pygame.event.get():
#            
#        if event.type==pygame.QUIT:
#            pygame.display.quit()
#            sys.exit()

#    window.blit(tile_blue, (0, 0))
#    render() #screen refresh
#    clock.tick(60) #limits game speed
    
