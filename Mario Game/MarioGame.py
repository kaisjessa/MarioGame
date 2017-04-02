'''
Kais Jessa
June 11 2016
v0.0.2
'''

#import modules
import pygame
import sys
import random

#create Coin class
class Coin:
    def __init__(self, x, y):
        self.image = pygame.image.load("Coin.png")
        self.coinx = x
        self.coiny = y

# create Game class
class Game:

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.init()
        # set global variables
        self.movex = 0
        self.movey = 0
        self.lmovex = 0
        self.lmovey = 0
        self.points = 0
        self.x = 10
        self.y = 10
        self.lx = 10
        self.ly = 950
        self.swidth = 1920
        self.sheight = 1080
        # fullscreen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)
        # captions and font
        pygame.display.set_caption("Welcome to MarioGame! Pick up coins to get points!")
        global font
        # change the font below if you don't want to use the font in the folder
        font = pygame.font.SysFont("04b_30", 35)
        self.gametext = font.render("Who can get the most coins?", 1, (255, 255, 255))
        info = pygame.display.Info()
        global width
        global height
        width, height = info.current_w, info.current_h
        self.gametext_pos = (500, 0)
        self.full = True
        self.mario_controls = pygame.image.load("MarioGameControls2.png")
        self.mario_controlspos = width-500, height-225
        global numcoins
        numcoins = 10
        self.mpoints = 0
        self.mstring = "0"
        self.lpoints = 0
        self.lstring = "0"
        self.mpoints_pos = width - 250, 0
        self.coin_sound = pygame.mixer.Sound("Pickup.wav")
        self.maintheme = pygame.mixer.Sound("Maintheme.wav")
        self.maintheme.play(-1)
        self.mcolor = 255, 0, 0
        self.lcolor = 0, 255, 0


        
    def run(self):
# sets variable for the mario and luigi sprites
        mariocycle = 0
        mario1 = pygame.image.load("mario1.png")
        mario2 = pygame.image.load("mario2.png")
        mario3 = pygame.image.load("mario3.png")
        mario4 = pygame.image.load("mario4.png")
        mario = mario1
        self.timenum = 0
        self.timetarget = 20


        lcycle = 0
        luigi1 = pygame.image.load("luigi1.png")
        luigi2 = pygame.image.load("luigi2.png")
        luigi3 = pygame.image.load("luigi3.png")
        luigi4 = pygame.image.load("luigi4.png")
        luigi = luigi1
        self.ltimenum = 0
   # random coin spawns     
        mylist = []
        for i in range(numcoins):
            x = random.randint(0, width - 100)
            y = random.randint(0,height - 100)
            instance = Coin(x, y)
            mylist.append(instance)
            
        
        gameloop = True
        while gameloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                     
                     # lets you move
                    if event.key == pygame.K_LEFT:
                        self.movex = -2
                        mario1 = pygame.image.load("bmario1.png")
                        mario2 = pygame.image.load("bmario2.png")
                        mario3 = pygame.image.load("bmario3.png")
                        mario4 = pygame.image.load("bmario4.png")
                        mario = mario1
                    if event.key == pygame.K_RIGHT:
                        self.movex = 2
                        mario1 = pygame.image.load("mario1.png")
                        mario2 = pygame.image.load("mario2.png")
                        mario3 = pygame.image.load("mario3.png")
                        mario4 = pygame.image.load("mario4.png")
                        mario = mario1
                    if event.key == pygame.K_UP:
                        self.movey = -2
                    if event.key == pygame.K_DOWN:
                        self.movey = 2
                    
                    if event.key == pygame.K_a:
                        self.lmovex = -2
                        luigi1 = pygame.image.load("bluigi1.png")
                        luigi2 = pygame.image.load("bluigi2.png")
                        luigi3 = pygame.image.load("bluigi3.png")
                        luigi4 = pygame.image.load("bluigi4.png")
                        luigi = luigi1
                    if event.key == pygame.K_d:
                        self.lmovex = 2
                        luigi1 = pygame.image.load("luigi1.png")
                        luigi2 = pygame.image.load("luigi2.png")
                        luigi3 = pygame.image.load("luigi3.png")
                        luigi4 = pygame.image.load("luigi4.png")
                        luigi = luigi1
                    if event.key == pygame.K_w:
                        self.lmovey = -2
                    if event.key == pygame.K_s:
                        self.lmovey = 2
                        # toggle fullscreen
                    if event.key == pygame.K_RSHIFT:
                        if self.full == False:
                            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                            self.full = True
                        elif self.full == True:
                            pygame.display.set_mode((0, 0), pygame.RESIZABLE)
                            self.full = False
                     # stop moving when you stop pressing a key   
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movex = 0
                    if event.key == pygame.K_RIGHT:
                        self.movex = 0
                    if event.key == pygame.K_UP:
                        self.movey = 0
                    if event.key == pygame.K_DOWN:
                        self.movey = 0
                    if event.key == pygame.K_a:
                        self.lmovex = 0
                    if event.key == pygame.K_d:
                        self.lmovex = 0
                    if event.key == pygame.K_w:
                        self.lmovey = 0
                    if event.key == pygame.K_s:
                        self.lmovey = 0
# keeps mario and luigi inside the game
            if 0 <= (self.x + self.movex) <= (self.swidth - 100) and self.movex != 0:
                self.x += self.movex
                if self.timenum == self.timetarget:
                    self.timenum = 0
                    if mario == mario1:
                        mario = mario2
                    elif mario == mario2:
                        mario = mario3
                    elif mario == mario3:
                        mario = mario4
                    elif mario == mario4:
                        mario = mario1
                else:
                    self.timenum += 1
                    # cycles through the mario and luigi sprites
            if 0 <= (self.y + self.movey) <= (self.sheight - 100) and self.movey != 0:
                self.y += self.movey
                if self.timenum == self.timetarget:
                    self.timenum = 0
                    if mario == mario1:
                        mario = mario2
                    elif mario == mario2:
                        mario = mario3
                    elif mario == mario3:
                        mario = mario4
                    elif mario == mario4:
                        mario = mario1    
                else:
                    self.timenum += 1
            if self.movex == 0 and self.movey == 0:
                mario = mario1

            if 0 <= (self.lx + self.lmovex) <= (self.swidth - 100) and self.lmovex != 0:
                self.lx += self.lmovex
                if self.ltimenum == self.timetarget:
                    self.ltimenum = 0
                    if luigi == luigi1:
                        luigi = luigi2
                    elif luigi == luigi2:
                        luigi = luigi3
                    elif luigi == luigi3:
                        luigi = luigi4
                    elif luigi == luigi4:
                        luigi = luigi1
                else:
                    self.ltimenum += 1

            if 0 <= (self.ly + self.lmovey) <= (self.sheight - 100) and self.lmovey != 0:
                self.ly += self.lmovey
                if self.ltimenum == self.timetarget:
                    self.ltimenum = 0
                    if luigi == luigi1:
                        luigi = luigi2
                    elif luigi == luigi2:
                        luigi = luigi3
                    elif luigi == luigi3:
                        luigi = luigi4
                    elif luigi == luigi4:
                        luigi = luigi1
                else:
                    self.ltimenum += 1
            if self.lmovex == 0 and self.lmovey == 0:
                luigi = luigi1

             # lets you pickup coins and play coin sound
            for q in mylist:
                coinrectx = q.coinx
                coinrecty = q.coiny
                if self.x - 100 <= coinrectx <= self.x + 100 and self.y - 100 <= coinrecty <= self.y + 100:
                    self.coin_sound.play()
                    mylist.remove(q)
                    self.mpoints += 1
                    self.mstring = str(self.mpoints)
                    
                elif self.lx - 100 <= coinrectx <= self.lx + 100 and self.ly - 100 <= coinrecty <= self.ly + 100:
                    self.coin_sound.play()
                    mylist.remove(q)
                    self.lpoints += 1
                    self.lstring = str(self.lpoints)
                    # counts points
                if self.mpoints >= 10 and self.mpoints < 1000:
                    self.mpoints_pos = width - 300, 0
                elif self.mpoints >= 1000:
                    self.mpoints_pos = width - 350, 0
                if mylist == []:
                    for i in range(numcoins):
                        x = random.randint(0, width - 100)
                        y = random.randint(0,height - 100)
                        instance = Coin(x, y)
                        mylist.append(instance)

# blit images and render font
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.mario_controls, self.mario_controlspos)
            for c in mylist:
                self.screen.blit(c.image, (c.coinx, c.coiny))
            self.screen.blit(mario, (self.x, self.y))
            self.screen.blit(luigi, (self.lx, self.ly))
            self.screen.blit(self.gametext, self.gametext_pos)
            self.mtext = font.render("Points: "+ self.mstring, 1, (self.mcolor))
            self.screen.blit(self.mtext, self.mpoints_pos)
            self.ltext = font.render("Points: "+ self.lstring, 1, (self.lcolor))
            self.lpoints_pos = 0, 0
            self.screen.blit(self.ltext, self.lpoints_pos)
            

            
            pygame.display.update()

    # refresh rate        
clock = pygame.time.Clock()
clock.tick(60)

# runs game
mygame = Game()
mygame.run()

                
