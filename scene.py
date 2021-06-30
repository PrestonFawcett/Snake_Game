
""" Scene class and subclasses """

import pygame
import colors
from food import Food
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
        self._restart = False
        self._frame_rate = 60

    def draw(self):
        """ Draws screen """
        if self._screen:
            self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """ Process events to leave scene """
        if event.type == pygame.QUIT:
            print('Quiting program')
            pygame.quit()
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

    def restart(self):
        """ Get restart """
        return self._restart

    def set_restart(self):
        """ Set to resart """
        self._restart = True

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
    def __init__(self, scene_id, screen, background_color):
        super().__init__(scene_id, screen, background_color)
        title_font = pygame.font.Font(pygame.font.get_default_font(), 72)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 22)
        self._title = title_font.render('Snake', True, colors.red)
        self._press_any_key = press_any_key_font.render('Press any key.', True, colors.black)
        self._title_pos = self._title.get_rect(center=(400, 400))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(400, 750))

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

class Instruction(Scene):
    """ subclass for Instruction scene """
    def __init__(self, scene_id, screen, background_color):
        super().__init__(scene_id, screen, background_color)
        header_str = 'Instructions'
        line1_str = 'Use arrow keys to move'
        line2_str = 'Every 3 seconds you will score 1 point'
        line3_str = 'every food you eat will award you 5 points'
        line4_str = 'If you hit yourself or the wall you will lose'
        header_font = pygame.font.Font(pygame.font.get_default_font(), 50)
        line1_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        line2_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        line3_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        line4_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 22)
        self._header = header_font.render(header_str, True, colors.white)
        self._line1 = line1_font.render(line1_str, True, colors.white)
        self._line2 = line2_font.render(line2_str, True, colors.white)
        self._line3 = line3_font.render(line3_str, True, colors.white)
        self._line4 = line4_font.render(line4_str, True, colors.white)
        self._press_any_key = press_any_key_font.render('Press any key.', True, colors.white)
        self._header_pos = self._header.get_rect(center=(400, 100))
        self._line1_pos = self._line1.get_rect(center=(400, 150))
        self._line2_pos = self._line2.get_rect(center=(400, 200))
        self._line3_pos = self._line3.get_rect(center=(400, 250))
        self._line4_pos = self._line4.get_rect(center=(400, 300))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(400, 750))

    def draw(self):
        """ Draws the instructions """
        super().draw()
        self._screen.blit(self._header, self._header_pos)
        self._screen.blit(self._line1, self._line1_pos)
        self._screen.blit(self._line2, self._line2_pos)
        self._screen.blit(self._line3, self._line3_pos)
        self._screen.blit(self._line4, self._line4_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)
    
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self.set_not_valid()
        

class Level(Scene):
    """ Subclass for Level scene """
    def __init__(self, scene_id, screen, background_color, player):
        super().__init__(scene_id, screen, background_color)
        self._field = (16, 16, 768, 768)
        self._player = player
        self._food = Food(screen)
        self._score = TimerScore()
        self._score_font = pygame.font.Font(pygame.font.get_default_font(), 25)
        self._display_score = self._score_font.render(
            'Score: {}'.format(self._score), True, colors.white)
        self._score_pos = self._display_score.get_rect(topleft=(32, 32))

    def draw(self):
        """ Draws level scene """
        super().draw()
        pygame.draw.rect(self._screen, colors.darkgreen, self._field)
        self._player.draw()
        self._food.draw()
        self._screen.blit(self._display_score, self._score_pos)

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
        index = 0
        for coords in self._food._food:
            if coords[0] == x and coords[1] == y:
                del self._food._food[index]
                return True
            index += 1
        return False
            # if body[0] == self._avatar[0][0] and body[1] == self._avatar[0][1]:

    def process_event(self, event):
        """ Processes all events associated with level """
        super().process_event(event)
        self._player.process_event(event)

    def update(self):
        """ updates the game for every state change """
        self._player.update()
        self._food.update()
        if self.eat_food():
            self._score.add_bonus(5)
            print('Ate food')
            print('Grew one segment')
        else:
            del self._player._avatar[-1]
        if self._player.intersecting() or self.out_of_bounds():
            print('Score: {}'.format(self._score))
            write(self._score._score)
            read()
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
        high_score_font = pygame.font.Font(pygame.font.get_default_font(), 60)
        self._high_score = high_score_font.render('High Score', True, colors.white)
        play_again_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        self._play_again = play_again_font.render(
            'Press \'r\' to restart. Press \'q\' to quit.', True, colors.white)
        (w, h) = self._screen.get_size()
        self._header_pos = self._header.get_rect(center=(w/2, 100))
        self._high_score_pos = self._high_score.get_rect(center=(w/2, 200))
        self._play_again_pos = self._play_again.get_rect(center=(w/2, h - 50))
        self._leader_board_list = read()

    def draw(self):
        """ Draws the game over scene """
        super().draw()
        leader_board_list = read()
        self._screen.blit(self._header, self._header_pos)
        self._screen.blit(self._high_score, self._high_score_pos)
        for i in range(len(self._leader_board_list)):
            leader_board_font = pygame.font.Font(pygame.font.get_default_font(), 40)
            self._leader_board = leader_board_font.render('{}: {}'.format(i+1, leader_board_list[i]), True, colors.white)
            self._leader_board_pos = self._leader_board.get_rect(center=(400, (250 + i * 50)))
            self._screen.blit(self._leader_board, self._leader_board_pos)
        self._screen.blit(self._play_again, self._play_again_pos)

    def process_event(self, event):
        """ Restarts or quits game """
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.set_restart()
                self.set_not_valid()
            elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                pygame.quit()
