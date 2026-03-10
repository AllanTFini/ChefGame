import pygame.image
from pygame import Rect

from code.Constants import ROTATE_LEFT, ROTATE_RIGHT


class Player:
    def __init__(self, position : tuple):
        self.original_image = pygame.image.load('./Assets/Player.png').convert_alpha()
        self.surface = self.original_image
        self.rect = self.surface.get_rect(center=position)
        self.score = 0

        #attributes for platter for collision and score
        self.platter_image = pygame.image.load('./Assets/platter.png').convert_alpha()
        self.platter_surface = self.platter_image
        self.platter_distance = -64
        self.platter_rect = self.platter_surface.get_rect(center=(self.rect.centerx, self.rect.centery + self.platter_distance))


    def draw(self, screen):
        screen.blit(self.surface, self.rect)
        screen.blit(self.platter_surface, self.platter_rect)

    def rotate(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[ROTATE_LEFT]:
            self.surface = pygame.transform.rotate(self.original_image, 90)
            self.platter_rect.center = (self.rect.centerx + self.platter_distance, self.rect.centery)
        if pressed_key[ROTATE_RIGHT]:
            self.surface = pygame.transform.rotate(self.original_image, -90)
            self.platter_rect.center = (self.rect.centerx - self.platter_distance, self.rect.centery)

    def check_collision(self,  object_rect):
        return self.platter_rect.center  == object_rect