import pygame

from code.Constants import WINDOW_WIDTH
from code.Player import Player


class Level:
    def __init__(self, window):
        self.window = window
        self.player = Player((WINDOW_WIDTH/2 , 300))


    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            self.window.fill((0, 0, 0))

            self.player.rotate()

            self.window.blit(self.player.surface, self.player.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.flip()