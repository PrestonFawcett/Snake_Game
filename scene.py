import pygame, colors

class Scene():
    def __init__(self, scene_id, screen, background_color=colors.black):
        self._id = scene_id
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(background_color)
        self._is_valid = True
        self._frame_rate = 60

    def draw(self):
        if self._screen:
            self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        if event.type == pygame.QUIT:
            print('Quiting program')
            self.set_not_valid()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.set_not_valid()

    def is_valid(self):
        return self._is_valid

    def set_not_valid(self):
        self._is_valid = False

    def update(self):
        pass

    def start_scene(self):
        print('starting {}'.format(self))

    def end_scene(self):
        print('ending {}'.format(self))

    def frame_rate(self):
        return self._frame_rate

    def __str__(self):
        return 'Scene {}'.format(self._id)

class Title(Scene):
    def __init__(self, scene_id, screen, background_color, title, title_color, title_size):
        super().__init__(scene_id, screen, background_color)
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, title_color)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, colors.black)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center = (w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center = (w/2, h - 50))

    def draw(self):
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)

    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self.set_not_valid()

class Level(Scene):
    def __init__(self, scene_id, screen, background_color, player):
        super().__init__(scene_id, screen, background_color)
        self._field = (16, 16, 768, 768)
        self._player = player
        #self._score = TimerScore()

    def draw(self):
        super().draw()
        pygame.draw.rect(self._screen, colors.green, self._field)
        self._player.draw()
        #print('The score is {}'.format(self._score))

    def out_of_bounds(self):
        head = self._player._avatar[0]
        in_bounds = head.colliderect(self._field)
        return in_bounds != 1

    def process_event(self, event):
        super().process_event(event)
        self._player.process_event(event)

    def update(self):
        self._player.update()
        if self._player.intersecting():
            print('You collided with yourself')
        if self.out_of_bounds():
            print('You collided with the wall')
            super().set_not_valid()
        
        #self._score_click()
        #self._player.process_event(event)

class GameOver(Scene):
    def __init__(self, scene_id, screen, background_color):
        super().__init__(scene_id, screen, background_color)
        header_font = pygame.font.Font(pygame.font.get_default_font(), 80)
        self._header = header_font.render('Game Over', True, colors.white)
        play_again_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        self._play_again = play_again_font.render('Press \'y\' to play again',
         True, colors.white)
        (w, h) = self._screen.get_size()
        self._header_pos = self._header.get_rect(center = (w/2, h/2))
        self._play_again_pos = self._play_again.get_rect(center = (w/2, h - 50))

    def draw(self):
        super().draw()
        self._screen.blit(self._header, self._header_pos)
        self._screen.blit(self._play_again, self._play_again_pos)

    # def process_event(self, event):
    #     super().process_event(event)
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_y
    #            restart()

    # def restart(self):
        