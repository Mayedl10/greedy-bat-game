import os #used for file paths
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame #imports pygame
from pygame import mixer #for sounds and music
import time
import random
pygame.init()
pygame.mixer.init()
pygame.font.init() #used for text
pygame.mixer.init() #used for sound




FPS = 30 #Frames per second. How fast does the screen update?

WHITE = (255, 255, 255) #RGB value for white

WINDOW_NAME = "Greedy bat" #This text will be on top of the window
WIDTH, HEIGHT = 900, 500 #size of the screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(WINDOW_NAME) #sets the name of the window using WINDOW_NAME
Timer_Font = pygame.font.SysFont("comicsans", 40)

global bat_vel
global bat_y
bat_x, bat_y = 150, 224
bat_pic = (os.path.join("assets","bat.png"))
bat_vel = int(5)
bat_xel = int(0)
control = True
start = False
bat_dir = "right"
gem_x, gem_y = 650, 224
flame_x, flame_y = 700, 400
gem_pic = pygame.image.load(os.path.join("assets","blood_gem.png"))
flame_pic = pygame.image.load(os.path.join("assets","flame.png"))
bat_rect = pygame.Rect(bat_x, bat_y, 64, 52)
gem_rect = pygame.Rect(gem_x, gem_y, 21, 21)
flame_rect = pygame.Rect(flame_x, flame_y, 32, 52)
score = 0
content_r = None

invinc_cnt = 0

def first():
        control = False
        global bat_y
        global bat_x
        global score
        bat_x, bat_y = 150, 224

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(pygame.image.load(os.path.join("assets","cave_bg.jpg")),(0,0))
        WIN.blit(pygame.transform.scale(pygame.image.load(bat_pic),(64,52)),(bat_x, bat_y))        
        timer_text = Timer_Font.render("Game begins in: 3", 1, WHITE)
        WIN.blit(timer_text, (10, 10))
        pygame.display.update()
        pygame.time.wait(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(pygame.image.load(os.path.join("assets","cave_bg.jpg")),(0,0))
        WIN.blit(pygame.transform.scale(pygame.image.load(bat_pic),(64,52)),(bat_x, bat_y))        
        timer_text = Timer_Font.render("Game begins in: 2", 1, WHITE)
        WIN.blit(timer_text, (10, 10))
        pygame.display.update()
        pygame.time.wait(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.blit(pygame.image.load(os.path.join("assets","cave_bg.jpg")),(0,0))
        WIN.blit(pygame.transform.scale(pygame.image.load(bat_pic),(64,52)),(bat_x, bat_y))        
        timer_text = Timer_Font.render("Game begins in: 1", 1, WHITE)
        WIN.blit(timer_text, (10, 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        score = 0

        global flame_rect
        global bat_rect

        bat_rect = pygame.Rect(bat_x, bat_y, 64, 52)
        flame_rect = pygame.Rect(flame_x, flame_y, 32, 52)
        
        while bat_rect.colliderect(flame_rect):
                handle_gem_spawning()

        pygame.time.wait(1000)
        control = True

def death():
        global invinc_cnt
        if invinc_cnt == 0:

                death_sound = os.path.join("assets","death.mp3")
                mixer.music.load(death_sound)
                mixer.music.play()
                
                control = False
                global bat_y
                global bat_x
                global score
                bat_x, bat_y = 150, 224

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                WIN.blit(pygame.image.load(os.path.join("assets","cave_bg.jpg")),(0,0))
                WIN.blit(pygame.transform.scale(pygame.image.load(bat_pic),(64,52)),(bat_x, bat_y))        
                timer_text = Timer_Font.render("You'll be revived in: 3", 1, WHITE)
                WIN.blit(timer_text, (10, 10))
                pygame.display.update()
                pygame.time.wait(1000)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                WIN.blit(pygame.image.load(os.path.join("assets","cave_bg.jpg")),(0,0))
                WIN.blit(pygame.transform.scale(pygame.image.load(bat_pic),(64,52)),(bat_x, bat_y))        
                timer_text = Timer_Font.render("You'll be revived in: 2", 1, WHITE)
                WIN.blit(timer_text, (10, 10))
                pygame.display.update()
                pygame.time.wait(1000)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                
                WIN.blit(pygame.image.load(os.path.join("assets","cave_bg.jpg")),(0,0))
                WIN.blit(pygame.transform.scale(pygame.image.load(bat_pic),(64,52)),(bat_x, bat_y))        
                timer_text = Timer_Font.render("You'll be revived in: 1", 1, WHITE)
                WIN.blit(timer_text, (10, 10))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                score = 0

                global flame_rect
                global bat_rect

                bat_rect = pygame.Rect(bat_x, bat_y, 64, 52)
                flame_rect = pygame.Rect(flame_x, flame_y, 32, 52)
                
                while bat_rect.colliderect(flame_rect):
                        handle_gem_spawning()

                pygame.time.wait(1000)
                control = True


def handle_movement(keys_pressed): #handles movement
        if control:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_d]:
                        bat_xel = int(15)
                        global bat_dir
                        bat_dir = "right"
                elif keys_pressed[pygame.K_a]:
                        bat_xel = int(-15)
                        bat_dir = "left"
                else:
                        bat_xel = 0
                        
                if keys_pressed[pygame.K_w]:
                        bat_vel = int(-15)
                else:
                        bat_vel = int(5)
                        
                global bat_y
                bat_y = bat_y + bat_vel
                global bat_x
                bat_x = bat_x + bat_xel
                
                
def draw_window(): #Draws the sprites to the screen
        global gem_x
        global gem_y
        global flame_x, flame_y
        WIN.blit(pygame.image.load(os.path.join("assets","cave_bg.jpg")),(0,0))
        
        timer_text = Timer_Font.render(f"Score: {score}", 1, WHITE)
        WIN.blit(timer_text, (10, 390))

        highscore_text = Timer_Font.render(f"Highscore: {content_r}", 1, WHITE)
        WIN.blit(highscore_text, (10, 440))
        
        WIN.blit(gem_pic, (gem_x, gem_y))
        WIN.blit(pygame.transform.scale(flame_pic, (32,52)), (flame_x, flame_y))
        global bat_dir
        if bat_dir == "right":
                bat_pic = (os.path.join("assets","bat.png"))
        if bat_dir == "left":
                bat_pic = (os.path.join("assets","bat_l.png"))
        WIN.blit(pygame.transform.scale(pygame.image.load(bat_pic),(64,52)),(bat_x, bat_y))

        
       

        
        
        
        pygame.display.update()

def handle_gem_spawning():
        global gem_x
        global gem_y

        global bat_x
        global bat_y

        global flame_x, flame_y

        global invinc_cnt

        global flame_rect
        global bat_rect

        gem_x = random.randint(100,700)
        gem_y = random.randint(100,400)

        flame_x = random.randint(100, 700)
        flame_y = random.randint(100, 400)

        bat_rect = pygame.Rect(bat_x, bat_y, 64, 52)
        flame_rect = pygame.Rect(flame_x, flame_y, 32, 52)
        gem_rect = pygame.Rect(gem_x, gem_y, 21, 21)

        if flame_rect.collidepoint((bat_x,bat_y)):
                flame_x = random.randint(100, 700)
                flame_y = random.randint(100, 400)
                flame_rect = pygame.Rect(flame_x, flame_y, 32, 52)

        if flame_rect.colliderect(gem_rect):
                gem_x = random.randint(100,700)
                gem_y = random.randint(100,400)
                gem_rect = pygame.Rect(gem_x, gem_y, 21, 21)

        invinc_cnt = 30

def highscore_handle():
        global score
        global content_r

        file_r = open(os.path.join("assets","highscore.txt"))
        content_list = file_r.readlines()
        file_r.close()

        file_r = open(os.path.join("assets","highscore.txt"))
        content_r = file_r.read()
        print(content_r)


        if score > int(content_r):
                file_a = open(os.path.join("assets","highscore.txt"),"w") #"a" doesn't delete lines
                file_a.writelines(str(score))
                file_a.close()


                        


def main(): #MAIN GAME LOOP
    global bat_x
    global bat_y
    global score
    global bat_rect
    global gem_x
    global gem_y
    global invinc_cnt
    global flame_pic
    
    first()

    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        bat_rect = pygame.Rect(bat_x, bat_y, 64, 52)
        gem_rect = pygame.Rect(gem_x, gem_y, 21, 21)
        flame_rect = pygame.Rect(flame_x, flame_y, 32, 52)
        handle_movement(pygame.key.get_pressed())

        if flame_rect.colliderect(gem_rect):
                gem_x = random.randint(100,700)
                gem_y = random.randint(100,400)


        #gem collecting
        gem_collect = os.path.join("assets","gemcollect.mp3")
        gem_x10_collect = os.path.join("assets","10_gems.mp3")
    
        if bat_rect.colliderect(gem_rect): #collission with gem
                handle_gem_spawning()
                score = score + 1
                
                if score % 10 == 0:
                        mixer.music.load(gem_x10_collect)
                        mixer.music.play()

                else:
                        mixer.music.load(gem_collect)
                        mixer.music.play()
        if invinc_cnt > 0:
                invinc_cnt -=1
                flame_pic = pygame.image.load(os.path.join("assets","flame_out.png"))
        else:
                flame_pic = pygame.image.load(os.path.join("assets","flame.png"))


        
        if bat_y <= 0 or bat_y + 52 >= HEIGHT or bat_x <= 0 or bat_x >= 840 or bat_rect.colliderect(flame_rect): #conditions for death
                death()
        
        draw_window()
        highscore_handle()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    pygame.quit()
                

                
    
    
if __name__ == "__main__":
    main()
    
    

























