import pygame, decoration, random
from pygame.locals import *

Texture_pack = "C:\\Users\\Lenovo-PC\\Desktop\\Python\\Pygame_avanzado\\Pac Man\\Recursos\\Texture_pack.png"

en_width = 28
en_height = 28
val = 4

target_sprites =  pygame.sprite.Group()
chronometer = pygame.sprite.Group()


def init(all_sprites1, enemy_sprites1, wall_sprites1, player_sprites1):
    global all_sprites
    global enemy_sprites
    global wall_sprites
    global player_sprites
    
    all_sprites = all_sprites1
    enemy_sprites = enemy_sprites1
    wall_sprites =  wall_sprites1
    player_sprites = player_sprites1
    decoration.init(all_sprites, all_sprites)
    
    
def Generate_Enemy(x, y, color, identifier, scatter_xy, lever_target):
    enemy = Enemy(x, y, color, identifier)
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)
    
    target_tile = Target_Tile(identifier, scatter_xy, lever_target)
    all_sprites.add(target_tile)
    target_sprites.add(target_tile)
    
    if lever_target == 3:
        special_target = Target_Tile("none", (0, 0), "3")
        all_sprites.add(special_target)
        target_sprites.add(special_target)
    
    central_box = central_hit_box(en_width, en_width/2, "x", identifier)
    all_sprites.add(central_box)
    
    central_box = central_hit_box(en_width/2, en_width, "y", identifier)
    all_sprites.add(central_box)
    
    lateral_box = lateral_hit_box(en_width, val, "up", identifier)
    all_sprites.add(lateral_box)
    
    lateral_box = lateral_hit_box(en_width, val, "down", identifier)
    all_sprites.add(lateral_box)
    
    lateral_box = lateral_hit_box(val, en_width, "left", identifier)
    all_sprites.add(lateral_box)
    
    lateral_box = lateral_hit_box(val, en_width, "right", identifier)
    all_sprites.add(lateral_box)
    
    
class Target_Tile(pygame.sprite.Sprite):
    def __init__(self, identifier, scatter_xy, lever_target):
        super().__init__()
        self.identifier =  identifier
        self.lever_target = lever_target
        
        self.rev = False
        
        self.image = pygame.Surface((28, 28))
        self.image.fill((255, 0, 0))
        
        # if self.lever_target == 1:
            # self.image.fill((255, 0, 0))
            # self.image.set_colorkey((255, 0, 0))
            
        # if self.lever_target == 2:
            # self.image.fill((250, 180, 250, 1))
            
        if self.lever_target == "3":
            self.image.fill((255, 255, 255, 1))
            
        if self.lever_target == 3:
            self.image.fill((1, 255, 255, 1))
            
        # if self.lever_target == 4:
            # self.image.fill((250, 190, 90, 1))
            
            
        
        self.image.set_colorkey((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 465
        self.rect.y = 60

        
        self.scatter_xy = scatter_xy
        
        self.chronometer_mode_1 = decoration.Chronometer(7000)
        chronometer.add(self.chronometer_mode_1)
        
        self.chronometer_mode_2 = decoration.Chronometer(20000)
        chronometer.add(self.chronometer_mode_2)
 
        self.mode = 1
 
        
        for player in player_sprites:
            self.player = player
        
        for enemy in enemy_sprites:
            if enemy.identifier == self.identifier:
                self.enemy = enemy
        
            else:
                if enemy.identifier == "inky":
                    self.enemy = enemy
            
        

    def Level_1(self):
        self.rect.center = self.player.rect.center


    def Level_2(self):
        if self.player.direction == "up": 
            self.rect.x = self.player.rect.x - 56
            self.rect.y = self.player.rect.y - 56
            
        if self.player.direction == "down":
            self.rect.x = self.player.rect.x
            self.rect.y = self.player.rect.y + 56
            
        if self.player.direction == "left":
            self.rect.x = self.player.rect.x - 56
            self.rect.y = self.player.rect.y 
            
        if self.player.direction == "right":
            self.rect.x = self.player.rect.x + 56
            self.rect.y = self.player.rect.y 

 
    def Level_3_1(self):
        if self.player.direction == "up": 
            self.rect.x = self.player.rect.x - 28
            self.rect.y = self.player.rect.y - 28
            
        if self.player.direction == "down":
            self.rect.x = self.player.rect.x
            self.rect.y = self.player.rect.y + 28
            
        if self.player.direction == "left":
            self.rect.x = self.player.rect.x - 28
            self.rect.y = self.player.rect.y 
            
        if self.player.direction == "right":
            self.rect.x = self.player.rect.x + 28
            self.rect.y = self.player.rect.y 


    def Level_3_2(self):
        for enemy in enemy_sprites:
                if enemy.identifier == "blinky":
                    self.enemy_3 = enemy
                    
        for target in target_sprites:
            if target.identifier == "none":
                self.special_target = target
    
        self.rect.x = self.special_target.rect.x + (self.special_target.rect.x - self.enemy_3.rect.x)
        self.rect.y = self.special_target.rect.y + (self.special_target.rect.y - self.enemy_3.rect.y)


    def Level_4(self):
        for enemy in enemy_sprites:
            if enemy.identifier == "clyde":
                radian_enemy = enemy
                
        if radian_enemy.rect.x > self.player.rect.x:
            if radian_enemy.rect.x - self.player.rect.x <= 112:
                self.rect.x = 165
                self.rect.y = 545
                
            else:
                self.rect.center = self.player.rect.center
                
        if radian_enemy.rect.x < self.player.rect.x:
            if radian_enemy.rect.x - self.player.rect.x >= -112:
                self.rect.x = 165
                self.rect.y = 545
                
            else:
                self.rect.center = self.player.rect.center
                
                
        if radian_enemy.rect.y > self.player.rect.y:
            if radian_enemy.rect.y - self.player.rect.y <= 112:
                self.rect.x = 165
                self.rect.y = 545
                
            else:
                self.rect.center = self.player.rect.center
                
        if radian_enemy.rect.y < self.player.rect.y:
            if radian_enemy.rect.y - self.player.rect.y >= -112:
                self.rect.x = 165
                self.rect.y = 545
                
            else:
                self.rect.center = self.player.rect.center


    def update(self):
        if self.mode >= 3:
            self.mode = 1
            
        if self.mode == 1:
            if self.chronometer_mode_1.Play():
                self.mode += 1
                self.chronometer_mode_1.kill()
                
                self.chronometer_mode_2 = decoration.Chronometer(20000)
                chronometer.add(self.chronometer_mode_2)
                
        if self.mode == 2:
            if self.chronometer_mode_2.Play():
                self.mode += 1
                self.chronometer_mode_2.kill()
                
                self.chronometer_mode_1 = decoration.Chronometer(7000)
                chronometer.add(self.chronometer_mode_1)
            
            

        if self.enemy.mode == 2:
            if self.mode == 1:
                self.rect.x = self.scatter_xy[0]
                self.rect.y = self.scatter_xy[1]
        
            if self.mode == 2:
                if self.lever_target == 1:
                    self.Level_1()
                    
                if self.lever_target == 2:
                    self.Level_2()
                    
                if self.lever_target == "3":
                    self.Level_3_1()
                    
                if self.lever_target == 3:
                    self.Level_3_2()
                    
                if self.lever_target == 4:
                    self.Level_4()

        if self.enemy.mode == 3:
            self.rect.x = self.scatter_xy[0]
            self.rect.y = self.scatter_xy[1]
            
        if self.enemy.mode == 4:
            self.rect.x = 245
            self.rect.y = 270
   

class central_hit_box(pygame.sprite.Sprite):
    def __init__(self, width, height, axis, identifier):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 0, 0))
        
        self.image.set_colorkey((100, 0, 0))
 
        self.rect = self.image.get_rect()
        
        self.identifier = identifier
        
        for enemy in enemy_sprites:
            if self.identifier == enemy.identifier:
                self.enemy = enemy
        
        
        self.rect.y = self.enemy.rect.x
        self.rect.x = self.enemy.rect.y
        
        self.axis = axis


    def Teleport(self):
        if self.rect.x < 15:
            self.enemy.rect.x = 495

        if self.rect.x > 505:
            self.enemy.rect.x = 25


    def Movement(self):
        self.rect.center = self.enemy.rect.center

  
    def Collide_Wall(self):
        wall_impact = pygame.sprite.spritecollide(self, wall_sprites, False)
        for wall in wall_impact:
            if self.axis == "x":
                if self.enemy.speed_x > 0:
                    self.enemy.rect.right = wall.rect.left
                    
                if self.enemy.speed_x < 0:
                    self.enemy.rect.left = wall.rect.right
                    
            if self.axis == "y":
                
                if self.enemy.speed_y > 0:
                    self.enemy.rect.bottom = wall.rect.top
                    
                if self.enemy.speed_y < 0:
                    self.enemy.rect.top = wall.rect.bottom 


    def update(self):
        self.Teleport()
        self.Movement()
        self.Collide_Wall()


class lateral_hit_box(pygame.sprite.Sprite):
    def __init__(self, width, height, direction, identifier):
        self.direction = direction
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 100, 0)) #(255, 0, 0)
        
        self.image.set_colorkey((0, 100, 0))
        
        self.identifier =  identifier
        
        self.rect = self.image.get_rect()
        for enemy in enemy_sprites:
            if self.identifier == enemy.identifier:
                self.enemy = enemy
        
        
        if self.direction == "up":
            self.rect.x = self.enemy.rect.x
            self.rect.y = self.enemy.rect.y +val*-1
        
        if self.direction == "left":
            self.rect.x = self.enemy.rect.x +val*-1
            self.rect.y = self.enemy.rect.y
            
        if self.direction == "down":
            self.rect.x = self.enemy.rect.x
            self.rect.y = self.enemy.rect.y +en_width

        if self.direction == "right":
            self.rect.x = self.enemy.rect.x +en_width
            self.rect.y = self.enemy.rect.y 


    def redirection_n_restriction(self):
        if self.direction == "up":
            if pygame.sprite.spritecollide(self, wall_sprites, False):
                self.enemy.up = False
                
            else:
                self.enemy.up = True
    
    
        if self.direction == "left":
            if pygame.sprite.spritecollide(self, wall_sprites, False):
                self.enemy.left = False
                
            else:
                self.enemy.left = True


        if self.direction == "down":
            if pygame.sprite.spritecollide(self, wall_sprites, False):
                self.enemy.down = False
                
            else:
                self.enemy.down = True

          
        if self.direction == "right":
            if pygame.sprite.spritecollide(self, wall_sprites, False):
                self.enemy.right = False
                
            else:
                self.enemy.right = True


    def update(self):
        self.redirection_n_restriction()
        
        if self.direction == "up":
            self.rect.x = self.enemy.rect.x
            self.rect.y = self.enemy.rect.y +val*-1
        
        if self.direction == "left":
            self.rect.x = self.enemy.rect.x +val*-1
            self.rect.y = self.enemy.rect.y 
            
        if self.direction == "down":
            self.rect.x = self.enemy.rect.x
            self.rect.y = self.enemy.rect.y +en_width

        if self.direction == "right":
            self.rect.x = self.enemy.rect.x +en_width
            self.rect.y = self.enemy.rect.y 


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color, identifier):
        super().__init__()
        self.identifier = identifier
        
        self.color = color
        
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(3, 125, 1, 1))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())  # 14 13
        self.image.set_colorkey((0, 0, 0))
        
        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((255, 0, 0, 1), self.color)
        
        self.image = pygame.transform.scale(self.image, (en_width, en_width)) #14 = 12, 13 = 11
        
        self.animation_mode = 0
        self.mode = 2
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed_x = 0
        self.speed_y = 0
        
        self.speed = 2
        
        self.up_dir = True
        self.up =    True 
        self.up_states =    ((71, 125), (88, 125))
        
        self.left_dir =  True
        self.left =  True
        self.left_states =  ((37, 125), (54, 125))
        
        self.down_dir =  True
        self.down =  True
        self.down_states =  ((105, 125), (122, 125))
        
        self.right_dir = True
        self.right = True
        self.right_states = ((3, 125), (20, 125))
        
        self.frightened_sates_1 = ((3, 197), (20, 197))
        self.frightened_sates_2 = ((37, 197), (54, 197), (3, 197), (20, 197))
        
        self.eaten_sates = ((69, 197), (88, 197), (103, 197), (120, 197))
        
        self.direction = "down"

        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 120 
    

    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:           
            self.last_update = now
            self.frame += 1
  
            if self.animation_mode == 1:
                if self.frame >= 2:
                    self.frame = 0
            
                 
                if self.direction == "up":
                    self.sheet.set_clip(pygame.Rect(self.up_states[self.frame]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    
                    
                if self.direction == "left":
                    self.sheet.set_clip(pygame.Rect(self.left_states[self.frame]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                   
                    
                if self.direction == "down":
                    self.sheet.set_clip(pygame.Rect(self.down_states[self.frame]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())


                if self.direction == "right":
                    self.sheet.set_clip(pygame.Rect(self.right_states[self.frame]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    
                    
                self.image.set_colorkey((0, 0, 0))
                self.image_pixel_array = pygame.PixelArray(self.image)
                self.image_pixel_array.replace((255, 0, 0, 1), self.color)
                self.image = pygame.transform.scale(self.image, (en_width, en_height))
                
                
            if self.animation_mode == 2:
                if self.frame >= 2:
                    self.frame = 0
            
                self.sheet.set_clip(pygame.Rect(self.frightened_sates_1[self.frame]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                self.image = pygame.transform.scale(self.image, (en_width, en_height))
                
            
            if self.animation_mode == 3:
                if self.frame >= 4:
                    self.frame = 0
            
                self.sheet.set_clip(pygame.Rect(self.frightened_sates_2[self.frame]+(14, 13)))
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                self.image = pygame.transform.scale(self.image, (en_width, en_height))
                
                
            if self.animation_mode == 4:
                if self.frame >= 2:
                    self.frame = 0
            
                if self.direction == "up":
                    self.sheet.set_clip(pygame.Rect(self.eaten_sates[2]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    
                if self.direction == "left":
                    self.sheet.set_clip(pygame.Rect(self.eaten_sates[1]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    
                if self.direction == "down":
                    self.sheet.set_clip(pygame.Rect(self.eaten_sates[3]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    
                if self.direction == "right":
                    self.sheet.set_clip(pygame.Rect(self.eaten_sates[0]+(14, 13)))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
  
                self.image.set_colorkey((0, 0, 0))
                self.image = pygame.transform.scale(self.image, (en_width, en_height))


    def Scatter_Chase(self):
        self.animation_mode = 1
        self.Follow_Target()
        self.Change_direction()


    def Frightened(self):
        self.animation_mode = 2
        self.Random_direction()
        self.Change_direction()


    def Eaten(self):
        self.animation_mode = 4
        self.Follow_Target()
        self.Change_direction()
 
 
    def Random_direction(self):
        for target  in target_sprites:
            if self.identifier == target.identifier:
            
                if target.rect.y < self.rect.x:  # Movimiento en eje x ----------------
                    if self.left_dir:
                        if self.left:
                            self.direction = "left"

                if target.rect.x > self.rect.y:
                    if self.right_dir:
                        if self.right:
                            self.direction = "right"


                if not self.left:
                    if self.direction == "left":
                        if not self.up:
                            self.direction = "down"
                            
                        elif not self.down:
                            self.direction = "up"
                            
                        else:
                            self.direction = "down"
                        
                    
                if not self.right:
                    if self.direction == "right":
                        if not self.up:
                            self.direction = "down"
                            
                        elif not self.down:
                            self.direction = "up" 
                            
                        else:
                            self.direction = "up" # Movimiento en eje x ------------------
                            
                            
                            
                if target.rect.x < self.rect.y: # Movimiento en eje y ------------------
                    if self.up_dir:
                        if self.up:
                            self.direction = "up"

                if target.rect.y > self.rect.x:
                    if self.down_dir:
                        if self.down:
                            self.direction = "down"

 
                if not self.up:
                    if self.direction == "up":
                        if not self.left:
                            self.direction = "right"
                            
                        elif not self.right:
                            self.direction = "left"
                            
                        else:
                            self.direction = "right"
                            
                if not self.down:
                    if self.direction == "down":
                        if not self.left:
                            self.direction = "right"
                            
                        elif not self.right:
                            self.direction = "left" 
                            
                        else:
                            self.direction = "left" # Movimiento en eje y ------------------


    def Follow_Target(self):
        for target  in target_sprites:
            if self.identifier == target.identifier:
            
                if target.rect.x < self.rect.x: # Movimiento en eje x ------------------
                    if self.left_dir:
                        if self.left:
                            self.direction = "left"

                if target.rect.x > self.rect.x:
                    if self.right_dir:
                        if self.right:
                            self.direction = "right"


                if not self.left:
                    if self.direction == "left":
                        if not self.up:
                            self.direction = "down"
                            
                        elif not self.down:
                            self.direction = "up"
                            
                        else:
                            self.direction = "down"
                        
                    
                if not self.right:
                    if self.direction == "right":
                        if not self.up:
                            self.direction = "down"
                            
                        elif not self.down:
                            self.direction = "up" 
                            
                        else:
                            self.direction = "up" # Movimiento en eje x ------------------
                            
                            
                            
                if target.rect.y < self.rect.y: # Movimiento en eje y ------------------
                    if self.up_dir:
                        if self.up:
                            self.direction = "up"

                if target.rect.y > self.rect.y:
                    if self.down_dir:
                        if self.down:
                            self.direction = "down"

 
                if not self.up:
                    if self.direction == "up":
                        if not self.left:
                            self.direction = "right"
                            
                        elif not self.right:
                            self.direction = "left"
                            
                        else:
                            self.direction = "right"
                            
                if not self.down:
                    if self.direction == "down":
                        if not self.left:
                            self.direction = "right"
                            
                        elif not self.right:
                            self.direction = "left" 
                            
                        else:
                            self.direction = "left" # Movimiento en eje y ------------------


    def Change_direction(self):
        if self.direction == "up":
            self.Block_speed_x()
            self.speed_y = self.speed*-1
            self.down_dir = False
            
            if self.left == False and self.right == False:
                self.left_dir = True
                self.right_dir = True
                
                
        if self.direction == "down":
            self.Block_speed_x()
            self.speed_y = self.speed
            self.up_dir = False
            
            if self.left == False and self.right == False:
                self.left_dir = True
                self.right_dir = True
            
            
        if self.direction == "left":
            self.Block_speed_y()
            self.speed_x = self.speed*-1
            self.right_dir = False
            
            if self.down == False and self.up == False:
                self.up_dir = True
                self.down_dir = True
                
                
        if self.direction == "right":
            self.Block_speed_y()
            self.speed_x = self.speed
            self.left_dir = False
            
            if self.down == False and self.up == False:
                self.up_dir = True
                self.down_dir = True
                
            
        if self.direction == "?":
            self.Block_speed_x()
            self.Block_speed_y()


    def Block_speed_x(self):
        if self.speed_x < 0:
            self.speed_x += self.speed
                
        if self.speed_x > 0:
            self.speed_x += self.speed*-1


    def Block_speed_y(self):
        if self.speed_y < 0:
            self.speed_y += self.speed
                
        if self.speed_y > 0:
            self.speed_y += self.speed*-1


    def update(self):
        if self.mode == 1:
            pass
            
        if self.mode == 2:
            self.Scatter_Chase()
            
        if self.mode == 3:
            self.Frightened()
            
        if self.mode == 4:
            self.Eaten()
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        
        self.Animation()
