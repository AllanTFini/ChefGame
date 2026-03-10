import sys

import pygame

from code.Constants import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu


class GameManager:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        menu = Menu(self.window)
        menu_choice = menu.run()

        if menu_choice == MENU_OPTIONS[0]:
            level = Level(self.window)
            level.run()
        elif menu_choice == MENU_OPTIONS[1]:
            print("Go to score")
        elif menu_choice == MENU_OPTIONS[2]:
            print("Go to Credits")
        elif menu_choice == MENU_OPTIONS[3]:
            pygame.quit()
            sys.exit()
        else:
            pass