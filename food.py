import pygame, random, colors

class Food():
    def __init__(self, screen):
        self._screen = screen
        self._dimension = (32, 32)
        self._x = 32 * random.randint(0, 23) + 16
        self._y = 32 * random.randint(0, 23) + 16
        self._grape = (self._x, self._y)
        self._respawn = False
        
    def draw(self):
        if self._respawn:
            self._x = 32 * random.randint(0, 23) + 16
            self._y = 32 * random.randint(0, 23) + 16
            self._respawn = False
        grape = pygame.Rect(self._x, self._y, 32, 32)
        pygame.draw.rect(self._screen, colors.purple, grape)

    def get_rand_pos(self):
        return ((32 * random.randint(0, 23) + 16), (32 * random.randint(0, 23) + 16))

    def update(self):
        self._respawn = True