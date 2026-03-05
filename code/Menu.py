import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Constants import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTIONS, COLOR_MENU_TITLE, COLOR_MENU_SELECTED, \
    COLOR_MENU_OPTIONS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('./Assets/grand_canyon.png').convert_alpha()
        self.rect = self.surface.get_rect(left =0, top=0)
    
    def run(self):
        menu_choice = 0

        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.write_text('CHEF GAME', 80, COLOR_MENU_TITLE, (WINDOW_WIDTH/2, 90))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_choice:
                    self.write_text( MENU_OPTIONS[i], 40,COLOR_MENU_SELECTED, ((WINDOW_WIDTH / 2), 200 + 25 * i))
                else:
                    self.write_text(MENU_OPTIONS[i], 40, COLOR_MENU_OPTIONS, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_choice < len(MENU_OPTIONS) - 1:
                            menu_choice += 1
                        else:
                            menu_choice = 0
                    if event.key == pygame.K_UP:
                        if menu_choice > 0:
                            menu_choice -= 1
                        else:
                            menu_choice = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_choice]

            pygame.display.flip()


    def write_text(self, text : str, text_size : int, text_color : tuple, text_center_position : tuple):
        text_font : Font = pygame.font.SysFont(None, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
        