# C
import pygame

COLOR_MENU_TITLE = (255, 215, 0)
COLOR_MENU_OPTIONS = (245, 245, 220)
COLOR_MENU_SELECTED = (220, 20, 60)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# M
MENU_OPTIONS = { 0 : 'PLAY GAME',
                 1 : 'QUIT'
}

# O
OBJECT_NAME = ['bacon', 'cheese', 'chip', 'egg', 'watermelon', 'energy_drink', 'bulb', 'duck', 'glove', 'toilet_paper', 'outlet']
OBJECT_EVENT = pygame.USEREVENT + 1
OBJECT_SPAWN_TIME = 1000
OBJECT_SCORE = {'bacon' : 100,
                'cheese' : 200,
                'chip' : 50,
                'egg' : 150,
                'watermelon' : 300,
                'energy_drink' : 250,
                'bulb' : -50,
                'duck' : -100,
                'glove' : -200,
                'toilet_paper' : -300,
                'outlet' : -250
               }

# R
ROTATE_LEFT = pygame.K_LEFT
ROTATE_RIGHT = pygame.K_RIGHT

# T
TIMEOUT_EVENT = pygame.USEREVENT + 2
TIMEOUT_STEP = 1000
TIMEOUT_LEVEL = 20000

# W
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 640

# P
PANEL_HEIGHT = 290
PANEL_WIDTH = 250
PANEL_POSITION = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 21)