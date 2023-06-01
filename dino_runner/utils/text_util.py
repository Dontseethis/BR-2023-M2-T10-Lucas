import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_COLOR = (0, 0, 0)
FONT_SIZE = 30
FONT_STYLE = "freesansbold.ttf"

#Cores
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
AQUAMARINE = (127,255,212)
CHOCOLATE = (210,105,30)
RED = (255,0,0)


def draw_message_component(message, screen, font_color=FONT_COLOR, font_size=FONT_SIZE, pos_y_center=SCREEN_HEIGHT // 2, pos_x_center=SCREEN_WIDTH // 2):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)
