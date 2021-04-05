#from gamescene import *
from titlescene import *
from button import *
import pygame

class game:
    def run_game(self,width, height, starting_scene):
        pg.init()
        screen = pg.display.set_mode((width, height))
        clock = pg.time.Clock()

        active_scene = starting_scene

        while active_scene != None:
            pressed_keys = pg.key.get_pressed()

            # Event filtering
            filtered_events = []
            for event in pg.event.get():
                quit_attempt = False
                if event.type == pg.QUIT:
                    quit_attempt = True
                elif event.type == pg.KEYDOWN:
                    alt_pressed = pressed_keys[pg.K_LALT] or \
                                  pressed_keys[pg.K_RALT]
                    if event.key == pg.K_ESCAPE:
                        quit_attempt = True
                    elif event.key == pg.K_F4 and alt_pressed:
                        quit_attempt = True

                if quit_attempt:
                    active_scene.Terminate()
                else:
                    filtered_events.append(event)

            active_scene.ProcessInput(filtered_events, pressed_keys)
            active_scene.Update()
            active_scene.Render(screen)

            active_scene = active_scene.next

            pg.display.flip()
            #60 fps
            clock.tick(60)
    def __init__(self):
        self.run_game(800, 600, TitleScene())

Fusemore = game()