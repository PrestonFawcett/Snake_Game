#!/usr/bin/env python3

""" Snake game  main function """

import pygame, random
from scene import Scene
from title import Title
from player import Player

pygame.init()
display_info()
window_size = (800, 800)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window_size)
title = 'Snake'
pygame.display.set_caption(title)

player = Player(screen, 1)

if __name__ == '__main__':
    main()
