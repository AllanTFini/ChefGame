import random
import pygame
from pygame import Font, Surface, Rect

from code.Constants import WINDOW_WIDTH, OBJECT_NAME, OBJECT_EVENT, OBJECT_SPAWN_TIME, WINDOW_HEIGHT, COLOR_WHITE, \
    OBJECT_SCORE, TIMEOUT_EVENT, TIMEOUT_STEP, TIMEOUT_LEVEL, COLOR_BLACK, PANEL_HEIGHT, PANEL_WIDTH, PANEL_POSITION, \
    COLOR_MENU_TITLE, COLOR_MENU_OPTIONS
from code.ObjectFactory import ObjectFactory
from code.ObjectMediator import ObjectMediator
from code.Player import Player


class Level:
    def __init__(self, window):
        self.window = window
        self.player = Player((WINDOW_WIDTH/3 , 300))
        self.object_list = []
        self.spawn_positions = [(WINDOW_WIDTH/3 - 64, 20), (WINDOW_WIDTH/3 + 64, 20)]
        pygame.time.set_timer(OBJECT_EVENT, OBJECT_SPAWN_TIME)
        pygame.time.set_timer(TIMEOUT_EVENT, TIMEOUT_STEP)
        self.mediator = ObjectMediator()
        self.timeout = TIMEOUT_LEVEL


    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            self.window.fill(COLOR_BLACK)

            self.write_text(f'{self.timeout / 1000:.1f}s', 30, COLOR_WHITE, (40, 20))

            pygame.draw.rect(self.window, COLOR_MENU_OPTIONS,(PANEL_POSITION[0], PANEL_POSITION[1], PANEL_WIDTH, PANEL_HEIGHT))

            self.write_text(f'SCORE: {self.player.score}', 30, COLOR_BLACK, (WINDOW_WIDTH / 1.5, 40))

            for i in range(6):
                obj_image = pygame.image.load(f'./Assets/{OBJECT_NAME[i]}.png').convert_alpha()
                self.window.blit(source=obj_image, dest=(WINDOW_WIDTH - (WINDOW_WIDTH / 4), WINDOW_HEIGHT / 10 * i + 60))
                self.write_text(f'{OBJECT_SCORE.get(OBJECT_NAME[i])}', 20, COLOR_BLACK,(WINDOW_WIDTH - (WINDOW_WIDTH / 4 -50), WINDOW_HEIGHT / 10 * i + 80))

            for j in range(6, 11):
                obj_image = pygame.image.load(f'./Assets/{OBJECT_NAME[j]}.png').convert_alpha()
                self.window.blit(source=obj_image, dest=(WINDOW_WIDTH / 1.8, WINDOW_HEIGHT / 10 * (j - 6) + 80))
                self.write_text(f'{OBJECT_SCORE.get(OBJECT_NAME[j])}', 20, COLOR_BLACK,(WINDOW_WIDTH / 1.8 +50, WINDOW_HEIGHT / 10 * (j - 6) + 95))

            self.mediator.handle_collision(player=self.player, object_list=self.object_list)

            self.player.rotate()
            self.player.draw(self.window)


            for obj in self.object_list:
                obj.update()
                self.window.blit(obj.surface, obj.rect)
                if obj.rect.top >= WINDOW_HEIGHT:
                    self.object_list.remove(obj)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == OBJECT_EVENT:
                    object_name = random.choice(OBJECT_NAME)
                    position = random.choice(self.spawn_positions)
                    new_object = ObjectFactory.create_object(object_name, position)
                    self.object_list.append(new_object)
                if event.type == TIMEOUT_EVENT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return self.player.score



            pygame.display.flip()

    def write_text(self, text: str, text_size: int, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(None, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)