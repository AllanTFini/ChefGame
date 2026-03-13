import pygame
from pygame import Font, Surface, Rect

from code.Constants import COLOR_WHITE, WINDOW_HEIGHT, WINDOW_WIDTH, COLOR_MENU_SELECTED, COLOR_BLACK, COLOR_MENU_TITLE


class Score:
    def __init__(self, window):
        self.window = window
        self.image = pygame.image.load('./Assets/menu_background.png').convert_alpha()
        self.surface = pygame.transform.scale(self.image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self, final_score):
        self.window.blit(self.surface, self.rect)

        while True:
            self.write_text('GAME OVER', 100, COLOR_BLACK, (WINDOW_WIDTH/2, 50))
            self.write_text(f'FINAL SCORE: {final_score}', 40, COLOR_BLACK, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            self.write_text('Press ENTER to Exit', 60, COLOR_BLACK, (WINDOW_WIDTH/2, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        quit()

            pygame.display.flip()



    def write_text(self, text: str, text_size: int, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(None, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
