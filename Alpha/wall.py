import pygame, decoration
from pygame.locals import *
pygame.init()

Texture_pack = "C:\\Users\\Lenovo-PC\\Desktop\\Python\\Pygame_avanzado\\Pac Man\\Recursos\\Texture_pack.png"

def init(all_sprites1, wall_sprites1, tablet_sprites1):
    global all_sprites
    global wall_sprites
    global tablet_sprites
    
    all_sprites = all_sprites1
    wall_sprites =  wall_sprites1
    tablet_sprites =  tablet_sprites1
    decoration.init(all_sprites, all_sprites)
    

class Tablet(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
        super().__init__()
        self.score = score
        
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 185, 176)) #(0, 0, 255)
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Super_Tablet(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
        super().__init__()
        self.score = score
    
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(8, 79, 7, 7))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())  # 14 13
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (18, 18)) #14 = 12, 13 = 11
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Kill_Tablet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 185, 176)) #(0, 0, 255)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
        self.Chronometer1 = decoration.Chronometer(100)
        
    def update(self):
        tablet_n_wall = pygame.sprite.groupcollide(tablet_sprites, wall_sprites, True, False)
        if self.Chronometer1.Play():
            self.Chronometer1.kill()
            self.kill()


def Generate_tablets(x, y):
    init_x = x
    init_y = y

    # Parte superior --------------------
    
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+23, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
    
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+43, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
    
    # super tablet -------------------------------
    
    x = init_x
    super_tablet = Super_Tablet(x+16, y+56, 50)
    all_sprites.add(super_tablet)
    tablet_sprites.add(super_tablet)
    
    # super tablet -------------------------------
        
    x = init_x
    for n in range(17):
        tablet = Tablet(x+43, y+63, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    # super tablet -------------------------------
        
    x = init_x
    super_tablet = Super_Tablet(x+376, y+56, 50)
    all_sprites.add(super_tablet)
    tablet_sprites.add(super_tablet)
    
    # super tablet -------------------------------
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+83, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+103, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+123, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20 
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+143, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+163, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    # Parte superior --------------------
        
    # Parte central ---------------------
    
    x = init_x
    y = init_y
    for n in range(9):
        tablet = Tablet(x+103, y+183, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        y += 20
        
    x = init_x
    y = init_y
    for n in range(9):
        tablet = Tablet(x+303, y+183, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        y += 20

    y =  init_y
    
    # Parte central ---------------------

    # Parte inferior --------------------
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+363, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20 

    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+383, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
    
    # super tablet -------------------------------
    
    x = init_x
    super_tablet = Super_Tablet(x+16, y+396, 50)
    all_sprites.add(super_tablet)
    tablet_sprites.add(super_tablet)

    # super tablet -------------------------------

    x = init_x
    for n in range(8):
        tablet = Tablet(x+43, y+403, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    x = init_x
    for n in range(8):
        tablet = Tablet(x+223, y+403, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
     
    # super tablet -------------------------------
        
    x = init_x
    super_tablet = Super_Tablet(x+376, y+396, 50)
    all_sprites.add(super_tablet)
    tablet_sprites.add(super_tablet)
    
    # super tablet -------------------------------
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+423, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+443, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20  

    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+463, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20

    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+483, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    x = init_x
    for n in range(19):
        tablet = Tablet(x+23, y+503, 10)
        all_sprites.add(tablet)
        tablet_sprites.add(tablet)
        x += 20
        
    # Parte inferior --------------------
          
    
    # eliminando tabletas que estan entre las paredes
    
    kill_tablets = Kill_Tablet()
    all_sprites.add(kill_tablets)


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(371, 4, 164, 212))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (410, 530))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x#60
        self.rect.y = y#100
        
    def update(self):
        pass

   
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, weidth, height, color_key=True):
        super().__init__()
 
        self.image = pygame.Surface([weidth, height])
        self.image.fill((0, 0, 0)) #(0, 0, 255)
        
        if color_key == True: self.image.set_colorkey((0, 0, 0))
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


def Generate_Wall(x, y, weidth, height, Transpareance=False, color_key=True):
    wall = Wall(x, y, weidth, height, color_key)
    all_sprites.add(wall)
    
    if Transpareance == False:
        wall_sprites.add(wall)

  
def Generate_Stage(x, y):
    # ----Barras horizontales-------
    
    Generate_Wall(x,    y,     410, 10)
    Generate_Wall(x,    y+520, 410, 10)
    
    Generate_Wall(x+40, y+480,  130, 10)
    Generate_Wall(x+240, y+480, 130, 10)
    
    Generate_Wall(x+40, y+380, 50, 10)
    Generate_Wall(x+120, y+380, 50, 10)
    Generate_Wall(x+240, y+380, 50, 10)
    Generate_Wall(x+320, y+380, 50, 10)
    
    Generate_Wall(x+120, y+180, 50, 10)
    Generate_Wall(x+240, y+180, 50, 10)
    
    Generate_Wall(x+170, y+220, 70, 10)
    Generate_Wall(x+170, y+280, 70, 10)
   
    
    # ----Barras horizontales-------
    
    
    # ------Barras verticales--------

    Generate_Wall(x,     y    , 10, 190)
    Generate_Wall(x+400, y    , 10, 190)
    
    Generate_Wall(x,     y+340, 10, 190)
    Generate_Wall(x+400, y+340, 10, 190)
    
    Generate_Wall(x+200, y+10  , 10, 80)
    
    Generate_Wall(x+120, y+120, 10, 130)
    Generate_Wall(x+280, y+120, 10, 130)
    
    Generate_Wall(x+120, y+280, 10, 70)
    Generate_Wall(x+280, y+280, 10, 70)
    
    Generate_Wall(x+80, y+380, 10, 70)
    Generate_Wall(x+320, y+380, 10, 70)
    
    Generate_Wall(x+120, y+420, 10, 70)
    Generate_Wall(x+280, y+420, 10, 70)
    
    Generate_Wall(x+200, y+150, 10, 40)
    Generate_Wall(x+200, y+350, 10, 40)
    Generate_Wall(x+200, y+450, 10, 40)
    
    Generate_Wall(x+160, y+220, 10, 70)
    Generate_Wall(x+240, y+220, 10, 70)
   
    
    # ------Barras verticales--------
    
    
    # -----Cuadrados ----------------
    
    Generate_Wall(x+40   ,y+40  , 50, 50)
    Generate_Wall(x+120  ,y+40  , 50, 50)
    
    Generate_Wall(x+240  ,y+40  , 50, 50)
    Generate_Wall(x+320  ,y+40  , 50, 50)
    
    Generate_Wall(x+40   ,y+120  , 50, 30)
    Generate_Wall(x+160   ,y+120 , 90, 30)
    Generate_Wall(x+320   ,y+120 , 50, 30)
    
    Generate_Wall(x+160   ,y+320 , 90, 30)
    Generate_Wall(x+160   ,y+420 , 90, 30)
    
    Generate_Wall(x       ,y+420 , 50, 30)
    Generate_Wall(x+360   ,y+420 , 50, 30)
    
    Generate_Wall(x+320   ,y+180 , 150, 70)
    Generate_Wall(x+320   ,y+280 , 150, 70)
    
    Generate_Wall(x-60   ,y+180 , 150, 70)
    Generate_Wall(x-60   ,y+280 , 150, 70)
    
    # -----Cuadrados ----------------
    
    #Fondo --------------------------
    
    background = Background(x, y)
    all_sprites.add(background)
    
    #Fondo --------------------------
    
    # ---- Cuadrados ----------------
    Generate_Wall(x-60, y+180, 60, 170, True, False)
    Generate_Wall(x+410, y+180, 60, 170, True, False)
    
    # ---- Cuadrados ----------------
    
    
    