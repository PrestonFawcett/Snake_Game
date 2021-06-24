from scene import Scene
import pygame, colors

class Title(Scene)
def __init__(self, scene_id, screen, background_color, title, title_color, title_size):
    super().__init__(scene_id, screen, background_color)
    title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
    self._title = title_font.render(title, True, title_color)
    press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
    self._press_any_key = press_any_key_font.redner('Press any key.', True, colors.black)
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