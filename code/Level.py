import random
import pygame

from code.Constants import WINDOW_WIDTH, OBJECT_NAME, OBJECT_EVENT, OBJECT_SPAWN_TIME
from code.ObjectFactory import ObjectFactory
from code.Player import Player


class Level:
    def __init__(self, window):
        self.window = window
        self.player = Player((WINDOW_WIDTH/3 , 300))
        self.object_list = []
        self.spawn_positions = [(WINDOW_WIDTH/3 - 64, 20), (WINDOW_WIDTH/3 + 64, 20)]
        pygame.time.set_timer(OBJECT_EVENT, OBJECT_SPAWN_TIME)


    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            self.window.fill((0, 0, 0))

            self.player.rotate()
            self.player.draw(self.window)

            for obj in self.object_list:
                obj.update()
                self.window.blit(obj.surface, obj.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == OBJECT_EVENT:
                    object_name = random.choice(OBJECT_NAME)
                    position = random.choice(self.spawn_positions)
                    new_object = ObjectFactory.create_object(object_name, position)
                    self.object_list.append(new_object)

            pygame.display.flip()