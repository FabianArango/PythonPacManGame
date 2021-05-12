import pygame, player, enemy, wall, decoration, Score
from pygame.locals import *
pygame.init()

all_sprites =  pygame.sprite.Group()
wall_sprites =  pygame.sprite.Group()
tablet_sprites =  pygame.sprite.Group()
decoration_sprites =  pygame.sprite.Group()
enemy_sprites =  pygame.sprite.Group()
player_sprites = pygame.sprite.Group()

class Game(object):
    def __init__(self):
        decoration.init(all_sprites, decoration_sprites)
        
        wall.init(all_sprites, wall_sprites, tablet_sprites)
        
        enemy.init(all_sprites, enemy_sprites, wall_sprites, player_sprites)
        
        Score.init(all_sprites, player_sprites, tablet_sprites)
        
        player.init(all_sprites, wall_sprites, player_sprites, enemy_sprites, tablet_sprites)

        self.Intro_1()
        self.Game_Start()
        
        
    def Intro_1(self):
        decoration.Generate_Decoration("        high score alpha", 0, 4, (255, 255, 255), "0")
        decoration.Flicker_Message("   1up", 0, 4, (255, 255, 255), 240, "0")


    def Game_Start(self):
        wall.Generate_tablets(55, 80)

        Score.Score()
        
        self.player = player.Generate_player()
        
        enemy.Generate_Enemy(245, 270, (255, 0, 0, 1), "blinky", (385, 130), 1)
        enemy.Generate_Enemy(245, 270, (250, 180, 250, 1), "pinky", (105, 130), 2)
        enemy.Generate_Enemy(245, 170, (1, 255, 255, 1), "inky", (325, 545), 3)
        enemy.Generate_Enemy(245, 170, (250, 190, 90, 1), "clyde", (165, 545), 4)

        wall.Generate_Stage(55, 80)
        
        


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                
      
            try:
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(self.mouse_pos)
                    
                if event.type == KEYDOWN:
                    if event.key == pygame.K_p:
                        pass
                        
                self.player.handle(event)
                
            except:
                pass


    def run_logic(self):
        all_sprites.update()
        self.mouse_pos = pygame.mouse.get_pos()


    def display_frame(self, screen):    
        screen.fill((0, 0, 0))
        
        all_sprites.draw(screen)
        
        pygame.display.flip()

   
def main():
    screen = pygame.display.set_mode((520, 690))
    pygame.display.set_caption("PAC MAN")
    clock = pygame.time.Clock()
    game = Game()
    
    done = False
    while not done:
        done = game.process_events()       
        game.run_logic()
        game.display_frame(screen)      
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
 
