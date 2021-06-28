
""" Scene class and subclasses """

import pygame
import colors
from score import TimerScore
from highscore import write, read

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

class Scene():
    """ Parent class for scene """
    def __init__(self, scene_id, screen, background_color=colors.black):
        self._id = scene_id
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(background_color)
        self._is_valid = True
        self._frame_rate = 60

    def draw(self):
        """ Draws screen """
        if self._screen:
            self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """ Process events to leave scene """
        if event.type == pygame.QUIT:
            print('Quiting program')
            self.set_not_valid()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.set_not_valid()

    def update(self):
        """ Base update function for scene """
        pass

    def is_valid(self):
        """ Allows the scene to be active """
        return self._is_valid

    def set_not_valid(self):
        """ Set not valid, continues to next scene """
        self._is_valid = False

    def start_scene(self):
        """ Console info notifying scene has started """
        print('starting {}'.format(self))

    def end_scene(self):
        """ Console info notifying scene has ended """
        print('ending {}'.format(self))

    def frame_rate(self):
        """ Returns frame rate """
        return self._frame_rate

    def __str__(self):
        """ Returns scenes id number """
        return 'Scene {}'.format(self._id)

class Title(Scene):
    """ subclass for Title scene """
    def __init__(self, scene_id, screen, background_color,
                 title='Snake', title_color=colors.red, title_size=72):
        super().__init__(scene_id, screen, background_color)
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, title_color)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 22)
        self._press_any_key = press_any_key_font.render('Press any key.', True, colors.black)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))

    def draw(self):
        """ Draws title and related info """
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)

    def process_event(self, event):
        """ Processes events to continue to next scene """
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self.set_not_valid()

class Level(Scene):
    """ Subclass for Level scene """
    def __init__(self, scene_id, screen, background_color, player, food):
        super().__init__(scene_id, screen, background_color)
        self._field = (16, 16, 768, 768)
        self._player = player
        self._food = food
        self._score = TimerScore()
        self._score_font = pygame.font.Font(pygame.font.get_default_font(), 25)
        self._display_score = self._score_font.render(
            'Score: {}'.format(self._score), True, colors.white)
        self._score_pos = self._display_score.get_rect(center=(710, 32))

    def draw(self):
        """ Draws level scene """
        super().draw()
        pygame.draw.rect(self._screen, colors.darkgreen, self._field)
        self._player.draw()
        self._food.draw()
        self._screen.blit(self._display_score, self._score_pos)
        # print('The score is {}'.format(self._score))

    def out_of_bounds(self):
        """ Return true if player hits wall """
        (x, y) = self._player._avatar[0]
        if x < 16 or x > 768 or y < 16 or y > 768:
            print('You collided with the wall')
            return True
        return False

    def eat_food(self):
        """ Return true player eats food """
        (x, y) = self._player._avatar[0]
        if x == self._food._x and y == self._food._y:
            return True
        return False

    def process_event(self, event):
        """ Processes all events associated with level """
        super().process_event(event)
        self._player.process_event(event)

    def update(self):
        """ updates the game for every state change """
        self._player.update()
        if self.eat_food():
            self._food.update()
            self._score.add_bonus(1)
            print('Ate food')
            print('Grew one segment')
        else:
            del self._player._avatar[-1]
        if self._player.intersecting() or self.out_of_bounds():
            write(self._score)
            super().set_not_valid()
        self._score.click()
        self._display_score = self._score_font.render(
            'Score: {}'.format(self._score), True, colors.white)

class GameOver(Scene):
    """ Subclass for Game Over scene """
    def __init__(self, scene_id, screen, background_color):
        super().__init__(scene_id, screen, background_color)
        header_font = pygame.font.Font(pygame.font.get_default_font(), 80)
        self._header = header_font.render('Game Over', True, colors.white)
        play_again_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        self._play_again = play_again_font.render(
            'Press \'y\' to play again', True, colors.white)
        (w, h) = self._screen.get_size()
        self._header_pos = self._header.get_rect(center=(w/2, h/2))
        self._play_again_pos = self._play_again.get_rect(center=(w/2, h - 50))

    def draw(self):
        """ Draws the game over scene """
        super().draw()
        self._screen.blit(self._header, self._header_pos)
        self._screen.blit(self._play_again, self._play_again_pos)
