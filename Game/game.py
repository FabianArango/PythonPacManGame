import pygame, sys #dev 16 jul/19 aug 2020
from pygame.locals import *
pygame.init()

from Player import player, hit_box_player, live_count

from Enemy import enemy, target_tile, hit_box_enemy, enemy_sounds

from Background import background, pellets

from Text import animation, decoration, score, cursor

from Game_Controllers import game_controll, music

#update

version = "   v-1.4"

def init(all_sprites1, player_sprites1, enemy_sprites1, decoration_sprites1, pellets_sprites1):
    global all_sprites, player_sprites, enemy_sprites, decoration_sprites, pellets_sprites
    all_sprites, player_sprites, enemy_sprites, decoration_sprites = all_sprites1, player_sprites1, enemy_sprites1, decoration_sprites1
    pellets_sprites = pellets_sprites1


class Class(object):
    def __init__(self):
        self.exe = False

    def execute(self):
        self.exe = True
 
    def handle(self, event):
        if self.exe:
            pass

    def update(self, delta_time):
        if self.exe:
            pass


class Intro(pygame.sprite.Sprite):
    def __init__(self, execobj):
        super().__init__()
        
        self.execobj = execobj
       
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = 100
        self.rect.y = 700

        decoration.Generate_Decoration("1up    hi-score " + version, 100, 66, (255, 0, 0, 1), "go_up")
        decoration.Generate_Decoration(score.return_hi_score(), 240, 88, (255, 255, 255), "go_up")
        decoration.Generate_Decoration("   00", 100, 88, (255, 255, 255), "go_up")
        decoration.Generate_Decoration("*", 100, 132, (255, 255, 255), "go_up")
        
        decoration.Generate_Decoration("   start game!   ", 180, 286, (255, 255, 255), "go_up")
        decoration.Generate_Decoration(">", 200, 286, (255, 255, 255), "go_up")
        decoration.Generate_Decoration("   credits...", 180, 330, (255, 255, 255), "go_up")
        decoration.Generate_Decoration("   quit game    ", 180, 374, (255, 255, 255), "go_up")

        decoration.Generate_Decoration("|", 240, 413, (255, 255, 255), "go_up")
        
        decoration.Generate_Decoration("+ 1980,1984 namco ltd.", 100, 484, (255, 255, 255), "go_up")
        decoration.Generate_Decoration(" licenced to nintendo ", 100, 528, (255, 255, 255), "go_up")

        self.Go_Down()

    def Go_Down(self):
        for sprite in decoration_sprites:
            if sprite.identifier == "go_up":
                sprite.rect.y += 634
        
        
    def Go_Up(self, delta_time):
        if self.rect.y > 66:
            self.rect.y -= round(120*delta_time, 0)
            for sprite in decoration_sprites:
                if sprite.identifier == "go_up":
                    sprite.rect.y -= round(120*delta_time, 0)
                    
                    
        else:
            decoration.Kill_Identifier("go_up")
            self.kill()
            self.execobj.execute()

    def update(self, delta_time):
        self.Go_Up(delta_time)


class Main_Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
            
        self.execobj = None
            
        self.exe = False

 
    def execute(self):
        self.exe = True
        
        self.time = decoration.Chronometer(8)
        
        decoration.Kill_Identifier("score")
        decoration.Kill_Identifier("PAC_MAN")
        
        decoration.Generate_Decoration("1up    hi-score " + version, 100, 66, (255, 0, 0, 1), "score")
        decoration.Generate_Decoration(score.return_hi_score(), 240, 88, (255, 255, 255), "score")
        decoration.Generate_Decoration("   00", 100, 88, (255, 255, 255), "score")
        decoration.Generate_Decoration("*", 100, 132, (255, 255, 255), "PAC_MAN")
        
        decoration.Generate_Decoration("   start game!   ", 180, 286, (255, 255, 255), "options")
        decoration.Generate_Decoration("   credits...", 180, 330, (255, 255, 255), "options")
        decoration.Generate_Decoration("   quit game    ", 180, 374, (255, 255, 255), "options")

        decoration.Generate_Decoration("|", 240, 413, (255, 255, 255), "main_menu")
        
        decoration.Generate_Decoration("+ 1980,1984 namco ltd.", 100, 484, (255, 255, 255), "main_menu")
        decoration.Generate_Decoration(" licenced to nintendo ", 100, 528, (255, 255, 255), "main_menu")
        
        self.cursor = cursor.Main_Cursor()
        all_sprites.add(self.cursor)

        self.black_rect_flickter = cursor.Black_rect(self.cursor)
        all_sprites.add(self.black_rect_flickter)


    def handle(self, event):
        if self.exe:
            self.cursor.handle(event)
            if event.type == pygame.KEYDOWN:
                self.time = decoration.Chronometer(8)
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if self.cursor.rect.y == 286:
                        self.cursor.kill()
                        self.black_rect_flickter.kill()
                        
                        decoration.Kill_Identifier("score")
                        decoration.Kill_Identifier("PAC_MAN")
                        decoration.Kill_Identifier("options")
                        decoration.Kill_Identifier("main_menu")
                        
                        self.exe = False
                        return 0
                    
                    if self.cursor.rect.y == 330:
                        self.cursor.kill()
                        self.black_rect_flickter.kill()
                        
                        decoration.Kill_Identifier("options")
                        decoration.Kill_Identifier("main_menu")
                    
                        self.exe = False # Desactivar el handle
                        return 1
                        
                    if self.cursor.rect.y == 374:
                        self.exe = False
                        return 2
                
                if event.key == pygame.K_l:
                    print(len(decoration_sprites))


    def presentation(self):
        if self.time.time_over():
            self.time = decoration.Chronometer(8)
            self.cursor.kill()
            self.black_rect_flickter.kill()
            
            decoration.Kill_Identifier("PAC_MAN")
            decoration.Kill_Identifier("options")
            decoration.Kill_Identifier("main_menu")
            
            self.exe = False
            self.execobj.execute()

    def update(self, delta_time):
        if self.exe:
            self.presentation()


class Presentation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        
        self.rect.x = 10
        self.rect.y = 0
    
        self.exe = False
        self.animation = False

        self.stop = False
        
        self.point_count = 0
        
        self.animated_ghost = pygame.sprite.Group()
        self.animation_sprites = pygame.sprite.Group()
        
    def execute(self):
        self.exe = True

        self.animation = False
        self.stop = False
        self.point_count = 0
        
        self.chronometer_1 = decoration.Chronometer(11)
        
        self.chronometer_2 = decoration.Chronometer(4.6)
        
        self.chronometer_3 = decoration.Chronometer(1)

        decoration.Generate_Decoration(" character / nickname", 100, 154, (255, 255, 255), "presentation")
        
        decoration.Write_Message("{", 100, 210, -30, 0, 1200, (255, 0, 0, 1), "presentation", (255, 0, 0, 1))
        decoration.Write_Message("-shadow", 160, 220, 0, 18, 1200, (255, 0, 0, 1), "presentation")
        decoration.Write_Message("'blinky'", 360, 220, 0, 18, 1800, (255, 0, 0, 1), "presentation")
        
        decoration.Write_Message("{", 100, 276, -30, 0, 3000, (250, 180, 250, 1), "presentation", (255, 0, 0, 1))
        decoration.Write_Message("-speedy", 160, 286, 0, 18, 3000, (250, 180, 250, 1), "presentation")
        decoration.Write_Message("'pinky'", 360, 286, 0, 18, 3600, (250, 180, 250, 1), "presentation")
       
        decoration.Write_Message("{", 100, 342, -30, 0, 4800, (1, 255, 255, 1), "presentation", (255, 0, 0, 1))
        decoration.Write_Message("-bashful", 160, 352, 0, 18, 4800, (1, 255, 255, 1), "presentation")
        decoration.Write_Message("'inky'", 360, 352, 0, 18, 5400, (1, 255, 255, 1), "presentation")
        
        decoration.Write_Message("{", 100, 408, -30, 0, 6600, (250, 190, 90, 1), "presentation", (255, 0, 0, 1))
        decoration.Write_Message("-pokey", 160, 418, 0, 18, 6600, (250, 190, 90, 1), "presentation")
        decoration.Write_Message("'clyde'", 360, 418, 0, 18, 7200, (250, 190, 90, 1), "presentation")
        

        decoration.Write_Message("    ( 10 pts", 160, 462, 0, 18, 7800, (255, 255, 255), "animation")
        decoration.Write_Message("    ) 50 pts", 160, 506, 0, 18, 7800, (255, 255, 255), "animation")
        
        decoration.Write_Message("|", 240, 550, 0, 25, 7800, (255, 255, 255), "presentation")


    def handle(self, event):
        if self.exe:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.exe = False
                    self.chronometer_1.kill()
                    self.chronometer_2.kill()
                    self.chronometer_3.kill()
                    decoration.Kill_Identifier("animation")
                    decoration.Kill_Identifier("pellet")
                    decoration.Kill_Identifier("presentation")
                    
                    for animated in self.animation_sprites:
                        animated.kill()
                    
                    
                    try:
                        self.point.kill()
                    except:
                        pass
                    return 0


    def Create_Animation(self):
        if not self.animation:
            if self.chronometer_1.time_over():
                self.chronometer_1.kill()
                self.animation = True
                decoration.Kill_Identifier("animation")
                
                decoration.Flicker_Message(")", 140, 488, 200, (250, 190, 90, 1), "pellet")
        
                self.pac_man_eater = animation.Pac_man_eater(640, 484, 140)

                self.ghost_chased = animation.Chasing_n_Chased(685, 484, (255, 0, 0, 1), self.pac_man_eater)
                all_sprites.add(self.ghost_chased)
                self.animation_sprites.add(self.ghost_chased)
                self.animated_ghost.add(self.ghost_chased)
                
                self.ghost_chased = animation.Chasing_n_Chased(717, 484, (250, 180, 250, 1), self.pac_man_eater)
                all_sprites.add(self.ghost_chased)
                self.animation_sprites.add(self.ghost_chased)
                self.animated_ghost.add(self.ghost_chased)
                
                self.ghost_chased = animation.Chasing_n_Chased(749, 484, (1, 255, 255, 1), self.pac_man_eater)
                all_sprites.add(self.ghost_chased)
                self.animation_sprites.add(self.ghost_chased)
                self.animated_ghost.add(self.ghost_chased)
                
                self.ghost_chased = animation.Chasing_n_Chased(781, 484, (250, 190, 90, 1), self.pac_man_eater)
                all_sprites.add(self.ghost_chased)
                self.animation_sprites.add(self.ghost_chased)
                self.animated_ghost.add(self.ghost_chased)
                
                all_sprites.add(self.pac_man_eater)
                self.animation_sprites.add(self.pac_man_eater)


    def Control_Animation(self):
        if self.animation:
            if self.chronometer_2.time_over():
                self.chronometer_2.kill()
                decoration.Kill_Identifier("pellet")
        
        
            pac_man = pygame.sprite.spritecollide(self.pac_man_eater, self.animated_ghost, True)
            for collide in pac_man:
                self.point = animation.Generate_Point(self.point_count, self.pac_man_eater.rect.x-10, self.pac_man_eater.rect.y)
                
                self.pac_man_eater.Stop()
                
                for animated in self.animation_sprites:
                    animated.Stop()
                    
                self.point_count += 1
                 
                self.stop = True
            
            if self.stop:
                if self.chronometer_3.time_over():
                    self.chronometer_3.kill()
                    self.chronometer_3 = decoration.Chronometer(1)
                
                    self.pac_man_eater.Play()
                    for animated in self.animation_sprites:
                        animated.Play()
                
                    self.point.kill()
                    
                    self.stop = False


    def update(self, delta_time):
        if self.exe:
            self.Create_Animation()
            self.Control_Animation()


class Credits(object):
    def __init__(self):
        self.exe = False


    def execute(self):
        self.exe = True
        decoration.Generate_Decoration("fan made and progaming by", 90, 286, (255, 0, 0), "credits")
        decoration.Generate_Decoration("    fabian santiago     ", 90, 308, (255, 255, 255), "credits")
        
        decoration.Generate_Decoration("     art/graphics by     ", 90, 352, (1, 255, 255, 1), "credits")
        decoration.Generate_Decoration("deviantart.com/supastarfox", 70, 374, (255, 255, 255), "credits")
        
        decoration.Generate_Decoration("       sound fx             ", 90, 418, (250, 190, 90, 1), "credits")
        decoration.Generate_Decoration("   sounds-resource.com   ", 70, 440, (255, 255, 255), "credits")

        decoration.Generate_Decoration("     done   ", 170, 484, (255, 255, 255), "credits")
        decoration.Flicker_Message(">", 240, 484, 300, (255, 255, 255), "credits")
        
        decoration.Generate_Decoration("    original game by", 90, 526, (255, 0, 0), "credits")
        decoration.Generate_Decoration("|", 240, 550, (255, 255, 255), "credits")


    def handle(self, event):
        if self.exe:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    decoration.Kill_Identifier("credits")
                
                    self.exe = False
                    return 0


class Game_Play(object):
    def __init__(self):
        self.exe = False
        self.execobj = None

    def execute(self):
        self.exe = True
        
        decoration.Generate_Decoration("hi-score", 440, 66, (255, 0, 0, 1), "game")
        decoration.Flicker_Message(" 1up", 440, 132, 240, (255, 0, 0, 1),   "game")
        
        decoration.Generate_Decoration("level", 440, 198, (255, 0, 0, 1), "game")
        decoration.Generate_Decoration("1", 550, 198, (255, 255, 255), "level")
        
        score.Score()
        score.Hi_Score()
        
        ba = background.Background(20, 45)
        all_sprites.add(ba)
        
        self.player = player.Player() # Generando al jugador ------------------
        all_sprites.add(self.player)
        player_sprites.add(self.player)
        
        self.blinky = enemy.Enemy(210, 235, (255, 0, 0, 1), 1, 0) # blinky ----
        self.blinky.start_val[0] = "Out"
        self.blinky.start_val[1] = "Normal"
        self.blinky.start_val[4] = False
        self.blinky.start_val[5] = True
        self.blinky.start_val[8] = "left"
        all_sprites.add(self.blinky)
        enemy_sprites.add(self.blinky)
        
        self.clyde = enemy.Enemy(230, 290, (250, 190, 90, 1), 4, 60) # clyde --
        all_sprites.add(self.clyde)
        enemy_sprites.add(self.clyde)
        
        self.inky = enemy.Enemy(190, 290, (1, 255, 255, 1), 3, 30) # inky -----
        all_sprites.add(self.inky)
        enemy_sprites.add(self.inky)
        
        self.pinky = enemy.Enemy(210, 290, (250, 180, 250, 1), 2, 0) # pinky --
        all_sprites.add(self.pinky)
        enemy_sprites.add(self.pinky)
        
        background.Generate_Stage(20, 45) # Cargando el escenario -------------
        pellets.Generate_pellets(20, 45) # Cargando a los pellet --------------
        
        # Controladores del juego ---------------------------------------------
        all_sprites.add(enemy.Frame_control())
        all_sprites.add(game_controll.Intro())
        all_sprites.add(game_controll.Dead_Reset())
        all_sprites.add(game_controll.Pellet_Reset())
        
        self.game_over = game_controll.Game_Over()
        all_sprites.add(self.game_over)
        
        all_sprites.add(game_controll.Fruit_Per_Level())
        
        self.pause = game_controll.Pause()
        
        all_sprites.add(enemy_sounds.Enemy_Sound_Controller())
        # Controladores del juego ---------------------------------------------

 
    def handle(self, event):
        if self.exe:
            self.player.handle(event)
            self.pause.handle(event)


    def update(self, delta_time):
        if self.exe:
            if self.game_over.get_game_over():
                self.exe = False
                return 0
