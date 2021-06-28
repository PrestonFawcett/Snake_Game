""" File for keeping score during game """

import os.path
import pygame

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

class Score():
    """ Base class for score """
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, 'data')
    def __init__(self):
        self._score = 0

    def add_bonus(self, bonus_points):
        """ Add extra points for any event """
        self._score += bonus_points

    def __str__(self):
        """ Writes score as string """
        return '{}'.format(str(self._score))

class TimerScore(Score):
    """ Subclass for time score """
    def __init__(self, points_per_click=1, click_time_ms=3000):
        super().__init__()
        self._points_per_click = points_per_click
        self._click_time = click_time_ms
        self._last_time = pygame.time.get_ticks()

    def click(self):
        """ Grants one point every three seconds """
        current_time = pygame.time.get_ticks()
        elapsed = current_time - self._last_time
        if elapsed > self._click_time:
            self._last_time = current_time
            self._score += self._points_per_click
