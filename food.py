import pygame, random, colors

class Food():
    def __init__(self, screen):
        self._screen = screen
        self._dimension = (32, 32)
        self._x = 32 * random.randint(0, 23) + 16
        self._y = 32 * random.randint(0, 23) + 16
        self._grape = pygame.Rect((self._x, self._y), self._dimension)
        self._exists = True
        
    def draw(self):
        pygame.draw.rect(self._screen, colors.purple, self._grape)

    def exists(self):
        return self._exists

    def set_not_exist(self):
        self._exists = False

    def update(self):
        current_grape = self._grape
        
        self._x = 32 * random.randint(0, 23) + 16
        self._y = 32 * random.randint(0, 23) + 16
        self._grape.move(self._x, self._y)