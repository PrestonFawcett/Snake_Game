import pygame, os.path, colors, time
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
        self._avatar = [(w/2, h/2)]
        self._last_key = None

    def intersecting(self):
        for body in self._avatar[1:]:
            if body[0] == self._avatar[0][0] and body[1] == self._avatar[0][1]:
                return True
        return False

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
        for coords in self._avatar:
            x = int(coords[0])
            y = int(coords[1])
            segment = pygame.Rect(x, y, 32, 32)
            pygame.draw.rect(self._screen, colors.blue, segment)

    def update(self):
        time.sleep(0.07)
        (head_pos_x, head_pos_y) = self._avatar[0]
        new_head = ((head_pos_x + self._direction[0]), (head_pos_y + self._direction[1]))
        # new_head = current_head.move(self._direction)
        self._avatar.insert(0, new_head)
        
        # self._avatar = self._avatar[0:len(self._avatar) - 1]