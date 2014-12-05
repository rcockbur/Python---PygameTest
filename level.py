import pygame
from tile import *

b = BlueTile()
r = RedTile()
g = GreenTile()

class Level(object):
    def __init__(self, file_name):
        super(Level, self).__init__()
        level_file = open(file_name)
        self.tiles = level_file.readlines()
        for x in range(len(self.tiles)):
            self.tiles[x] = self.tiles[x].strip('\n').split(',')
        while self.tiles[-1] == ['']:
            self.tiles.pop()
        
    def drawTiles(self, surface):
        for row in range(len(self.tiles)):
            for column in range(len(self.tiles[row])):
                #print('x = ' + str(column))
                #print('y = ' + str(row))
                #print('value = ' + self.tiles[row][column])
                #print('')
                if self.tiles[row][column] == '0':
                    b.draw(surface, column, row)
                if self.tiles[row][column] == '1':
                    r.draw(surface, column, row)
                if self.tiles[row][column] == '2':
                    g.draw(surface, column, row)



                
