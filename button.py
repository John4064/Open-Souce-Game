import pygame as pg
class button(pg.sprite.Sprite):
    def update(self, *args, **kwargs):
        # defining a font
        #smallfont = pg.font.SysFont('Corbel', 35)
        #text = smallfont.render('quit', True, (255, 255, 0))
        pg.draw.rect(self.screen,self.color,[self.x,self.y,self.w,self.h])
        font1 = pg.font.SysFont('chalkduster.ttf', 36)
        img1 = font1.render(self.text, True, (0,0,255))
        self.screen.blit(img1, (self.x+20, self.y+10))
        #screen.blit(text, (self.x + 50, self.y))
        return
    def input(self,mouseX,mouseY):
        #Checks the bounds
        if ((mouseX>self.x and mouseX<self.x+self.w) and (mouseY>self.y and mouseY<self.y+self.h)):
            self.color = (128,0,127)
            global scene
            scene = 1
        return
    def __init__(self,x,y,w,h,text,color,screen):
        pg.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.w = w
        self.h=h
        self.text=text
        self.color =color
        self.screen = screen