from basescene import *
from gamescene import *
from button import *
import pygame
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        mouse = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())
            if event.type == pygame. KEYDOWN and event.key == pygame.K_j:
                print(1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                #button1
                #With Mouse array and mouse position array is 0 is X 1 is Y
                if ((self.mouse1[0]<mouse[0] and self.mouse1[0]+100>mouse[0])and (self.mouse1[1]<mouse[1] and self.mouse1[1]+40>mouse[1])):
                    print(mouse[1])

    def Update(self):
        pass

    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))
        #Test button
        self.mouse1 = [400,500]
        self.test1 = button(self.mouse1[0],self.mouse1[1], 100, 40, 'Test', (0, 13, 55), screen)
        self.test1.update()


