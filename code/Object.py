from abc import ABC

import pygame.image


class Object(ABC):
    def __init__(self, name : str, position : tuple):
        self.name = name
        self.surface = pygame.image.load(f'./Assets/{self.name}.png').convert_alpha()
        self.rect = self.surface.get_rect(center = position)
        self.speed = 10

    def update(self):
        self.rect.centery += self.speed
