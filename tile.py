import pygame
origin_x = 400-16


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super(Tile, self).__init__()
        #self.isoX = isoX
        #self.isoY = isoY
        
    #def updateRect(self):
        #self.rect.x = self.isoX - self.isoY
        #self.rect.y = (self.isoX + self.isoY)/2

    def draw(self, surface, col, row):
        surface.blit(self.image, (16*(col - row) + origin_x, 16*(col + row)/2))

class BlueTile(Tile):
    def __init__(self):
        super(BlueTile, self).__init__()
        self.image = pygame.image.load("tile_blue.png").convert_alpha()
        #self.rect = self.image.get_rect()
        #super(BlueTile,self).updateRect()

class GreenTile(Tile):
    def __init__(self):
        super(GreenTile, self).__init__()
        self.image = pygame.image.load("tile_green.png").convert_alpha()
        #self.rect = self.image.get_rect()
        #super(GreenTile,self).updateRect()

class RedTile(Tile):
    def __init__(self):
        super(RedTile, self).__init__()
        self.image = pygame.image.load("tile_red.png").convert_alpha()
        #self.rect = self.image.get_rect()
        #super(RedTile,self).updateRect()
