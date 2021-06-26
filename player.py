import pygame, os.path, colors
from scene import Scene

class Player:
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, 'data')
    #sprite_path = os.path.join(data_dir, 'my_snake.png')

    def  __init__(self, screen, speed):
        self._screen = screen
        self._dimension = (32, 32)
        self._direction = (0, 0)
        self._speed = speed * self._dimension[0]
        (w,h) = self._screen.get_size()
        self._avatar = [pygame.Rect((w/2, h/2), self._dimension)]
        self._last_key = None

    def intersecting(self):
        head = self._avatar[0]
        body_list = self._avatar[1:]
        hit = head.collidelist(body_list)
        return hit != -1

    def grow(self, n=1):
        for i in range(n):
            current_head = self._avatar[0]
            new_head = current_head.move(self._direction)
            self._avatar.insert(0, new_head)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self._last_key != pygame.K_LEFT:
                self._direction = (1 * self._speed, 0)
                self._last_key = event.key
            elif event.key == pygame.K_LEFT and self._last_key != pygame.K_RIGHT:
                self._direction = (-1 * self._speed, 0)
                self._last_key = event.key
            elif event.key == pygame.K_DOWN and self._last_key != pygame.K_UP:
                self._direction = (0, 1 * self._speed)
                self._last_key = event.key
            elif event.key == pygame.K_UP and self._last_key != pygame.K_DOWN:
                self._direction = (0, -1 * self._speed)
                self._last_key = event.key

    def draw(self):
        rect = self._avatar[0]
        pygame.draw.rect(self._screen, colors.blue, rect)

    def update(self):
        current_head = self._avatar[0]
        new_head = current_head.move(self._direction)
        self._avatar.insert(0, new_head)
        self._avatar = self._avatar[0:len(self._avatar) - 1]