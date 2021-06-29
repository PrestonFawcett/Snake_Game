#!/usr/bin/env python3

""" Snake game  main function """

import pygame
import colors
from scene import Title,Instruction, Level, GameOver
from player import Player
from food import Food

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

def display_info():
    """ Print info about display """
    print('The display is using the "{}" driver.'.format(pygame.display.get_driver()))
    print('Video Info: ')
    print(pygame.display.Info())

def main():
    """ Runs game """
    pygame.init()
    display_info()
    window_size = (800, 800)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Snake')

    player = Player(screen, 1)
    food = Food(screen)
    scene_list = [Title(1, screen, colors.darkgreen),
                  Instruction(2, screen, colors.black),
                  Level(3, screen, colors.black, player),
                  GameOver(4, screen, colors.black)]

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
