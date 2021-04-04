import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from config import *
pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# Run until the user asks to quit
running = True
class player(pg.sprite.Sprite):
    def update(self, *args, **kwargs):
        pg.draw.circle(screen, (0, 0, 255), (self.x,self.y), 25)
        return
    def input(self,userI):
        if event.key == K_UP:
            self.y-=15
            print(self.y)
        if event.key == K_DOWN:
            self.y+=15
            print(self.y)
        if event.key == K_LEFT:
            self.x-=15
            print(self.x)
        if event.key == K_RIGHT:
            self.x+=15
            print(self.x)
        return

    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.x =x
        self.y=y
        #h is height w is width
        self.h = 30
        self.w = 20
class button():
    def update(self, *args, **kwargs):
        # defining a font
        smallfont = pg.font.SysFont('Corbel', 35)
        text = smallfont.render('quit', True, (255, 255, 0))
        pg.draw.rect(screen,self.color,[self.x,self.x,self.y+40,self.y-60])
        screen.blit(text, (self.x + 50, self.y))
        return
    def input(self,mouseX,mouseY):
        if ((mouseX>self.x and mouseX<self.x+140) and (mouseY>self.y and mouseY<self.y+40)):
            self.color = (128,0,127)
        return
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.color =(255,0,0)
class enemy(pg.sprite.Sprite):
    def update(self, *args, **kwargs):
        pg.draw.rect(screen,(255,0,0),[100,100,140,40])
        return
    def __init__(self,x,y):
        self.x=x
        self.y=y

#Declaring the player
myPlayer = player(300,500)
test1 = button(100,100)
while running:
    #Getting the Mouse Position
    mouse = pg.mouse.get_pos()
    for event in pg.event.get():
        #User Input

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                #Exits the game if escape is pressed
                running = False

            #This just handles the input of the user
            myPlayer.input(event.key)
        elif event.type == QUIT:
            running = False
        #if mouse press
        if event.type == pg.MOUSEBUTTONDOWN:
            test1.input(mouse[0],mouse[1])
    #color for background
    screen.fill((255, 255, 255))
    #draws the player based on theinput
    myPlayer.update()
    test1.update()
    pg.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    pg.time.Clock().tick(30)

pg.quit()
