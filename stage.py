import pygame
from pygame import *
from physics import *
from player import *

global screen, running, player, window, floor


def __init__():
    global screen, running, player, window, floor
    pygame.display.set_caption('Game')
    window = Pair(512, 512)
    screen = display.set_mode(window.pair())
    pygame.display.flip()
    running = True
    player = Player(100, 20, 50, 50)
    floor = draw.rect(screen, BROWN, (0, window.top_offset(20), 512, 20))


def set_stage():
    screen.fill(BASE)
    draw.rect(screen, BROWN, (0, window.top_offset(20), 512, 20))
    player.draw_player(screen)
    # draw.rect(screen, ORANGE, player.object())


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


def player_manager():
    player.move_player()
    player.fall(floor)


def run():
    while running:
        key_manager()
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        set_stage()
        player_manager()

        pygame.time.delay(16)
        display.flip()
    quit()
