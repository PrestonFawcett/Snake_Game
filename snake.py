#!/usr/bin/env python3

""" Snake game  main function """

import pygame, random
import colors
from scene import Scene
from title import Title
from player import Player

def main():
    pygame.init()
    display_info()
    window_size = (800, 800)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(window_size)
    title = 'Snake'
    pygame.display.set_caption(title)

    player = Player(screen, 1)
    scene_list = [Title(1, screen, colors.darkgreen, title, colors.red, 72), Scene(2, screen), Scene(3, screen)]

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
