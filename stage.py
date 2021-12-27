import pygame
from pygame import *
from player import *


class Stage:
    mouse_x, mouse_y, mouse_b = None, None, None

    def __init__(self):
        # Initialize display window
        pygame.display.set_caption('Game')
        self.window = Pair(512, 512)
        self.screen = display.set_mode(self.window.pair())
        pygame.display.flip()

        self.running = True
        self.player = Player(100, 20, 50, 50)

    def floor(self):
        return draw.rect(self.screen, BROWN, (0, self.window.top_offset(20), 512, 20))

    def set_stage(self):
        self.screen.fill(BASE)
        draw.rect(self.screen, BROWN, (0, self.window.top_offset(20), 512, 20))
        self.player.draw_player(self.screen)
        self.floor()

    def event_manager(self):
        # Mouse events
        mouse_x, mouse_y = mouse.get_pos()
        mouse_b = mouse.get_pressed()

        # Interrupt & key events
        for e in event.get():
            if e.type == QUIT:
                self.running = False
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            self.running = False
        if keys[K_LEFT]:
            self.player.accel_left()
        if keys[K_RIGHT]:
            self.player.accel_right()
        if keys[K_UP]:
            self.player.jump(self.floor())


    def player_manager(self):
        self.player.move_player()
        self.player.fall(self.floor())

    def run(self):
        while self.running:
            self.event_manager()
            self.set_stage()
            self.player_manager()

            pygame.time.delay(16)
            display.flip()
        quit()
