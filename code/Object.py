from abc import ABC

import pygame.image

from code.Constants import OBJECT_SCORE


class Object(ABC):
    def __init__(self, name : str, position : tuple):
        self.name = name
        self.image = pygame.image.load(f'./Assets/{self.name}.png').convert_alpha()
        self.surface = pygame.transform.scale_by(self.image, 1.5)
        self.rect = self.surface.get_rect(center = position)
        self.speed = 4
        self.score = OBJECT_SCORE[self.name]

    def update(self):
        self.rect.centery += self.speed
