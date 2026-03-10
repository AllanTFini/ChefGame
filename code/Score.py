import pygame
from pygame import Font, Surface, Rect

from code.Constants import COLOR_WHITE, WINDOW_HEIGHT, WINDOW_WIDTH


class Score:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('./Assets/grand_canyon.png').convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self, final_score):
        self.window.blit(self.surface, self.rect)

        while True:
            self.write_text('GAME OVER', 50, COLOR_WHITE, (WINDOW_WIDTH/2, 50))
            self.write_text(f'FINAL SCORE: {final_score}', 40, COLOR_WHITE, (WINDOW_WIDTH/2, 100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.flip()



    def write_text(self, text: str, text_size: int, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(None, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
