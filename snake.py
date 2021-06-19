#!/usr/bin/env python3

""" Snake game  main function """

import pygame, random
from scene import Scene

def display_info():
    """ Print info about display """
    print('The display is using the {} driver'.format(pygame.display.get_driver()))
    print('Video Info: ')
    print(pygame.display.Info())

def run_game():
    start_x = 400
    start_y = 400

def main():
    print('Initiating game')
    # Setup
    fps = 60
    window = pygame.display.set_mode((800, 800))
    cellsize = 40
    cell_height = 20
    cell_width = 20

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
  
    scene = Scene(1)
    while scene.is_valid():
        for event in pygame.event.get():
            scene.process_event(event)
            print(event)
  
    # if not pygame.font:
    #     print('Waring, fonts disabled')
    # if not pygame.mixer:
    #     print('Waring, sound disabled')

    # pygame.init()
    # display_info()
    # window_size = (800, 800)
    # clock = pygame.time.Clock()
    # title = 'Snake!'
    # pygame.display.set_caption(title)

    # scene_list = [Scene(1), Scene(2), Scene(3)]

    # for scene in scene_list:
    #     scene.start_scene()

    #     while scene.is_valid():
    #         clock.tick(scene.frame_rate())
    #         for event in pygame.event.get():
    #             scene.process_event(event)
    #             print(event)
    #         scene.update()
    #         scene.draw()
    #     scene.end_scene()
    
    pygame.quit()

if __name__ == '__main__':
    main()
