import pygame.image

from code.Constants import ROTATE_LEFT, ROTATE_RIGHT


class Player:
    def __init__(self, position : tuple):
        self.original_image = pygame.image.load('./Assets/Player.png').convert_alpha()
        self.surface = self.original_image
        self.rect = self.surface.get_rect(center=position)

    def rotate(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[ROTATE_LEFT]:
            self.surface = pygame.transform.rotate(self.original_image, 90)
        if pressed_key[ROTATE_RIGHT]:
            self.surface = pygame.transform.rotate(self.original_image, -90)