import pygame
from pygame.locals import * 
pygame.init()

Texture_pack = "C:\\Users\\Lenovo-PC\\Desktop\\Python\\Pygame_avanzado\\Pac Man\\Recursos\\Texture_pack.png"

pl_widt = 26
pl_height = 28

long = 5


def init(all_sprites1, wall_sprites1, player_sprites1, enemy_sprites1, tablet_sprites1):
    global all_sprites
    global wall_sprites
    global player_sprites
    global enemy_sprites
    global tablet_sprites
    
    all_sprites = all_sprites1
    wall_sprites =  wall_sprites1
    player_sprites =  player_sprites1
    enemy_sprites =  enemy_sprites1
    tablet_sprites =  tablet_sprites1


class Generate_player():
    def __init__(self):
        global player
        
        player = Player_Animation()
        all_sprites.add(player)
        player_sprites.add(player)
        
        central_box = central_hit_box(pl_height, pl_height/2, "x")
        all_sprites.add(central_box)
        
        central_box = central_hit_box(pl_height/2, pl_height, "y")
        all_sprites.add(central_box)
        
        lateral_box = lateral_hit_box(pl_height, 10, "up")
        all_sprites.add(lateral_box)
        
        lateral_box = lateral_hit_box(pl_height, 10, "down")
        all_sprites.add(lateral_box)
        
        lateral_box = lateral_hit_box(10, pl_height, "left")
        all_sprites.add(lateral_box)
        
        lateral_box = lateral_hit_box(10, pl_height, "right")
        all_sprites.add(lateral_box)
        
        # eat_box = eat_hit_box()
        # all_sprites.add(eat_box)


    def handle(self, event):
        player.handle(event)


class central_hit_box(pygame.sprite.Sprite):
    def __init__(self, width, height, axis):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 0, 0))
        
        self.image.set_colorkey((100, 0, 0))
 
        self.rect = self.image.get_rect()
        self.rect.y = player.rect.x
        self.rect.x = player.rect.y
        
        self.axis = axis


    def Teleport(self):
        if self.rect.x < 15:
            player.rect.x = 495

        if self.rect.x > 505:
            player.rect.x = 25


    def Movement(self):
        self.rect.center = player.rect.center

  
    def Collide_Wall(self):
        wall_impact = pygame.sprite.spritecollide(self, wall_sprites, False)
        for wall in wall_impact:
            if self.axis == "x":
                if player.speed_x > 0:
                    player.rect.right = wall.rect.left
                    
                if player.speed_x < 0:
                    player.rect.left = wall.rect.right
                    
                player.animation_x = False
                    
            if self.axis == "y":
                
                if player.speed_y > 0:
                    player.rect.bottom = wall.rect.top
                    
                if player.speed_y < 0:
                    player.rect.top = wall.rect.bottom 

                player.animation_y = False


    def update(self):
        self.Teleport()
        self.Movement()
        self.Collide_Wall()


class lateral_hit_box(pygame.sprite.Sprite):
    def __init__(self, width, height, direction):
        self.direction = direction
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 100, 0)) #(255, 0, 0)
        
        self.image.set_colorkey((0, 100, 0))
        
        self.rect = self.image.get_rect()
        
        
        if self.direction == "up":
            self.rect.x = player.rect.x
            self.rect.y = player.rect.y -10
        
        if self.direction == "left":
            self.rect.x = player.rect.x -10
            self.rect.y = player.rect.y
            
        if self.direction == "down":
            self.rect.x = player.rect.x
            self.rect.y = player.rect.y +pl_height

        if self.direction == "right":
            self.rect.x = player.rect.x +pl_height
            self.rect.y = player.rect.y 


    def redirection_n_restriction(self):
        if self.direction == "up":
            if pygame.sprite.spritecollide(self, wall_sprites, False):
                player.up = False
                
            else:
                player.up = True
                if player.save_direction == "up":
                    if player.save_direction != player.direction:
                    
                        player.direction = player.save_direction
    
    
        if self.direction == "left":
            if pygame.sprite.spritecollide(self, wall_sprites, False):
                player.left = False
                
            else:
                player.left = True
                if player.save_direction == "left":
                    if player.save_direction != player.direction:
                        player.direction = player.save_direction


        if self.direction == "down":
            if pygame.sprite.spritecollide(self, wall_sprites, False):
                player.down = False
                
            else:
                player.down = True
                if player.save_direction == "down":
                    if player.save_direction != player.direction:
                    
                        player.direction = player.save_direction

          
        if self.direction == "right":
            if pygame.sprite.spritecollide(self, wall_sprites, False):
                player.right = False
                
            else:
                player.right = True
                if player.save_direction == "right":
                    if player.save_direction != player.direction:
                    
                        player.direction = player.save_direction


    def update(self):
        self.redirection_n_restriction()
        
        if self.direction == "up":
            self.rect.x = player.rect.x
            self.rect.y = player.rect.y -10
        
        if self.direction == "left":
            self.rect.x = player.rect.x -10
            self.rect.y = player.rect.y 
            
        if self.direction == "down":
            self.rect.x = player.rect.x
            self.rect.y = player.rect.y +pl_height

        if self.direction == "right":
            self.rect.x = player.rect.x +pl_height
            self.rect.y = player.rect.y 


class eat_hit_box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 150, 0))
        
        self.image.set_colorkey((0, 150, 0))
 
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
        
    def frightened_enemy(self):
        hit_list = pygame.sprite.spritecollide(player, tablet_sprites, False)
        for tablet in hit_list:
            if tablet.score == 50:
                for enemy in enemy_sprites:
                    enemy.mode = 3
                    
    
    def eat_enemy(self):
        eaten_enemy_list = pygame.sprite.spritecollide(player, enemy_sprites, False)
    
        for enemy in eaten_enemy_list:
            if enemy.mode == 3:
                enemy.mode = 4
                
        
        
    def update(self):
        self.frightened_enemy()
        self.eat_enemy()
        
        self.rect.center = player.rect.center


class Player_Animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load(Texture_pack).convert()
        self.sheet.set_clip(pygame.Rect(4, 91, 12, 13))  # x, y, ancho+1, alto+1
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0, 0, 0))
        
        self.image = pygame.transform.scale(self.image, (pl_height, pl_height)) #14 = 12, 13 = 11
        
        self.rect = self.image.get_rect()
        self.rect.x = 246
        self.rect.y = 470
        
        self.speed_x = 0
        self.speed_y = 0
        
        self.speed = 2
        
        self.animation_x = True
        self.animation_y = True
        
        self.up =    True 
        self.up_states =    ((56, 92, 13, 12), (143, 72, 13, 12), (76, 92, 13, 12), (93, 92, 13, 12))
        
        self.left =  True
        self.left_states =  ((46, 91, 12, 13), (4, 91, 12, 13), (56, 91, 12, 13), (60, 91, 12, 13))
        
        self.down =  True
        self.down_states =  ((310, 92, 43, 12), (143, 92, 13, 82), (110, 92, 13, 12), (127, 95, 10, 12))
        
        self.right = True
        self.right_states = ((13, 91, 12, 13), (4, 91, 12, 13), (18, 91, 12, 13), (30, 91, 12, 13))
        
        self.direction = "?"
        self.save_direction = "?"
        
        self.frame = 0        
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

 
    def Animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:           
            self.last_update = now
            self.frame += 1
            
            
            if self.frame >= 4:
                 self.frame = 0     


            if self.animation_x == True:
                if self.direction == "left":
                    self.sheet.set_clip(pygame.Rect(self.left_states[self.frame]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_widt, pl_height))

                if self.direction == "right":
                    self.sheet.set_clip(pygame.Rect(self.right_states[self.frame]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_widt, pl_height))


            if self.animation_x == False:
                if self.direction == "left":
                    self.sheet.set_clip(pygame.Rect(self.left_states[0]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_widt, pl_height))

                if self.direction == "right":
                    self.sheet.set_clip(pygame.Rect(self.right_states[0]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_widt, pl_height))


            if self.animation_y == True:
                if self.direction == "up":
                    self.sheet.set_clip(pygame.Rect(self.up_states[self.frame]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_height, pl_widt))
                    
                if self.direction == "down":
                    self.sheet.set_clip(pygame.Rect(self.down_states[self.frame]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_height, pl_widt))


            if self.animation_y == False:
                if self.direction == "up":
                    self.sheet.set_clip(pygame.Rect(self.up_states[0]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_height, pl_widt))
                    
                if self.direction == "down":
                    self.sheet.set_clip(pygame.Rect(self.down_states[0]))
                    self.image = self.sheet.subsurface(self.sheet.get_clip())
                    self.image.set_colorkey((0, 0, 0))
                    self.image = pygame.transform.scale(self.image, (pl_height, pl_widt))
                    
                    
            if self.direction == "?":
                self.sheet = pygame.image.load(Texture_pack).convert()
                self.sheet.set_clip(pygame.Rect(4, 91, 12, 13)) 
                
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image.set_colorkey((0, 0, 0))
                
                self.image = pygame.transform.scale(self.image, (pl_height, pl_height))


    def Repair_Animation(self):
        if self.speed_x != 0:
            self.animation_x = True
            
        if self.speed_y != 0:
            self.animation_y = True


    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.up == True:
                    self.direction = "up"
                    self.save_direction = "up"

                if self.up == False:
                    self.save_direction = "up"
                
                
            elif event.key == pygame.K_a:
                if self.left == True:
                    self.direction = "left"
                    self.save_direction = "left"
                    
                if self.left == False:
                    self.save_direction = "left"
                    
                
            elif event.key == pygame.K_s:
                if self.down == True:
                    self.direction = "down"
                    self.save_direction = "down"
   
                if self.down == False:
                    self.save_direction = "down"
                
                
            elif event.key == pygame.K_d:
                if self.right == True:
                    self.direction = "right"
                    self.save_direction = "right"

                if self.right == False:
                    self.save_direction = "right"
                    
                    
            elif event.key ==  pygame.K_y:
                self.direction = "?"
                self.save_direction = "?"


    def Change_direction(self):
        if self.direction == "up":
            self.Block_speed_x()
            self.speed_y = self.speed*-1
            
            
        if self.direction == "left":
            self.Block_speed_y()
            self.speed_x = self.speed*-1
            
            
        if self.direction == "down":
            self.Block_speed_x()
            self.speed_y = self.speed
            
            
        if self.direction == "right":
            self.Block_speed_y()
            self.speed_x = self.speed
            
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
        self.Change_direction()
    
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.Animation()
        self.Repair_Animation()