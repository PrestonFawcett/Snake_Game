import pygame

class Scene():
    def __init__(self, scene_id):
        self._id = scene_id
        self._is_valid = True
        self._frame_rate = 60

    def draw(self):
        pass

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.set_not_valid()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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