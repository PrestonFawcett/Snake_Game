#!/usr/bin/env python3

""" Snake game  main function """

import pygame, random, colors
from scene import Scene, Title, Level, GameOver
from player import Player
#from rungame import play

def display_info():
    """ Print info about display """
    print('The display is using the "{}" driver.'.format(pygame.display.get_driver()))
    print('Video Info: ')
    print(pygame.display.Info())

def main():
    pygame.init()
    display_info()
    window_size = (800, 800)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(window_size)
    title = 'Snake'
    pygame.display.set_caption(title)

    player = Player(screen, 1)
    scene_list = [Title(1, screen, colors.darkgreen, title, colors.red, 72), 
    Level(2, screen, colors.black, player), GameOver(3, screen, colors.black)]

    for scene in scene_list:
        scene.start_scene()
        while scene.is_valid():
            clock.tick(scene.frame_rate())
            for event in pygame.event.get():
                scene.process_event(event)
            scene.update()
            scene.draw()
            pygame.display.update()
        scene.end_scene()
    pygame.quit()

if __name__ == '__main__':
    main()
