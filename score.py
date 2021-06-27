import pygame, ospath

class Score():
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, 'data')
    def __init__(self, bonus_snd=None):
        self._score = 0
        if bonus_snd:
            bonus_snd_data = os.path.join(Score.data_dir, bonus_snd)
            try:
                self._bonus_snd = pygame.mixer.Sound(bonus_snd_data)
            except pygame.error:
                print('Cannot open {}'.format(self._bonus_snd_data))
                raise SystemExit(1)
        else:
            self._bonus_snd = None
    
    def add_bonus(self, bonus_points):
        if self._bonus_snd:
            self._bonus_snd.play()
        self._score += bonus_points
    
    def __str__(self):
        return '{}'.format(str(self._score))

class TimerScore(Score):
    def __init__(self, points_per_click=1, click_time_ms=3000):
        super().init__()
        self._points_per_click = points_per_click
        self._click_time= click_time_ms
        self._last_time = pygame.time.get_ticks()

    def click(self):
        current_time = pygame.get_ticks()
        elapsed = curent_time - self._last_time
        if elapsed > self._click_time:
            self._last_time = current_time
            self._score += self._points_per_click