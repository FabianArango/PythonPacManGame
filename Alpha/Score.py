import pygame, decoration
from pygame .locals import *
pygame.init()

score = 0

def init(all_sprites1, player_sprites1, tablet_sprites1):
    global all_sprites
    global player_sprites
    global tablet_sprites
    
    all_sprites =  all_sprites1
    player_sprites =  player_sprites1
    tablet_sprites = tablet_sprites1


class Score_Part(decoration.Decoration_part):
    def __init__(self, pos, pos_x, pos_y):
        decoration.init(all_sprites, all_sprites)
        decoration.Decoration_part.__init__(self, 0, 0, 26, (255, 255, 255), "s")
        self.pos = pos
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def Get_points(self):
        global score
    
        tablet_list = pygame.sprite.groupcollide(tablet_sprites, player_sprites, True, False)
        for tablet in tablet_list:
            score += tablet.score
            
            
    def display(self):
        local_score = str(score)
        if len(local_score) >= 8:
            local_score = "error"

        if len(local_score) == 1:
            local_score = "     00"+local_score
            
        if len(local_score) == 2:
            local_score = "     "+local_score
            
        if len(local_score) == 3:
            local_score = "    "+local_score
            
        if len(local_score) == 4:
            local_score = "   "+local_score
            
        if len(local_score) == 5:
            local_score = "  "+local_score
            
        if len(local_score) == 6:
            local_score = " "+local_score
            
        if len(local_score) == 7:
            local_score = local_score

        
            
        v = list()
        for n in local_score:
            if n == "0":
                n = 31
            if n == "1":
                n = 32
            if n == "2":
                n = 33
            if n == "3":
                n = 34
            if n == "4":
                n = 35
            if n == "5":
                n = 36
            if n == "6":
                n = 37
            if n == "7":
                n = 38
            if n == "8":
                n = 39
            if n == "9":
                n = 40
            if n == " ":
                n = 29
            if n == "e":
                n = 4
            if n == "o":
                n = 14  
            if n == "r":
                n = 17
            
            v.append(n)
            
        local_score = v
        
        self.sheet.set_clip(pygame.Rect(self.sprite_sheet[local_score[self.pos]]+(8, 8)))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((0, 0, 0, 1), (0, 0, 1, 1))
        
        self.image.set_colorkey((0, 0, 1, 1))
        
        self.image = pygame.transform.scale(self.image, (18, 24))
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
    def update(self):
        self.Get_points()
        self.display()


def Score():
    x = 0
    y = 26
    for n in range(7):
        score_a = Score_Part(n, x, y)
        all_sprites.add(score_a)
        x += 20 
