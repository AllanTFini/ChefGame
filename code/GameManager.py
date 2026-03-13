import sys

import pygame

from code.Constants import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class GameManager:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        score = Score(self.window)
        menu = Menu(self.window)
        menu_choice = menu.run()

        if menu_choice == MENU_OPTIONS[0]:
            level = Level(self.window)
            final_score = level.run()

            score_screen = Score(self.window)
            score_screen.run(final_score)

        elif menu_choice == MENU_OPTIONS[1]:
            pygame.quit()
            sys.exit()
        else:
            pass