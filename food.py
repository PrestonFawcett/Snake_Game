""" File to create food """

import random
import pygame
import colors

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

class Food():
    """ Structure for food item """
    def __init__(self, screen):
        self._screen = screen
        self._dimension = (32, 32)
        self._x = 32 * random.randint(0, 23) + 16
        self._y = 32 * random.randint(0, 23) + 16
        self._food = [(self._x, self._y)]
        self._respawn = False
        self._last_time = 3000

    def draw(self):
        """ Draws food """
        for coords in self._food:
            x = int(coords[0])
            y = int(coords[1])
            # self._x = 32 * random.randint(0, 23) + 16
            # self._y = 32 * random.randint(0, 23) + 16
            food = pygame.Rect(x, y, 32, 32)
            pygame.draw.rect(self._screen, colors.purple, food)


        # for coords in self._avatar:
        #     x = int(coords[0])
        #     y = int(coords[1])
        #     segment = pygame.Rect(x, y, 32, 32)
        #     pygame.draw.rect(self._screen, colors.blue, segment)

    def update(self):
        """ Updates to respawn food """
        current_time = pygame.time.get_ticks()
        elapsed = current_time - self._last_time
        if elapsed > 3000:
            self._last_time = current_time
            x = 32 * random.randint(0, 23) + 16
            y = 32 * random.randint(0, 23) + 16
            new_food = (x, y)
            self._food.append(new_food)
            print('spawn new food')

        # time.sleep(0.07)
        # (head_pos_x, head_pos_y) = self._avatar[0]
        # new_head = ((head_pos_x + self._direction[0]), (head_pos_y + self._direction[1]))
        # self._avatar.insert(0, new_head)
