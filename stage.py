import pygame
from colours import *
from pygame import *
from physics import *
from player import *

global screen, running, player, res


def __init__():
    global screen, running, player, res

    pygame.display.set_caption('Game')
    res = Pair(512, 512)
    screen = display.set_mode(res.pair())
    pygame.display.flip()
    running = True
    player = Player(100, 20, 50, 50)


def set_stage():
    floor = draw.rect(screen, brown, (0, res.top_offset(20), 512, 20))
    draw.rect(screen, red, player.object())


def key_manager():
    global running
    for e in event.get():
        if e.type == QUIT:
            running = False

    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        running = False
    if keys[K_LEFT]:
        player.accel_left()
    if keys[K_RIGHT]:
        player.accel_right()


def run():
    while running:
        key_manager()
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.fill(base_colour)
        set_stage()
        player.move_player()

        pygame.time.delay(10)
        display.flip()
    quit()
