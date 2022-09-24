import pygame
from typing import List

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
D_BLUE = (0, 32, 96)
WIDTH, HEIGHT = 780, 450

def create_text(arr, font_size, color=BLACK) -> List[pygame.font.SysFont]:
    rv = []
    font = pygame.font.SysFont('chalkduster.tff', font_size)
    if type(arr) == list:
        for string in arr:
            rv.append(font.render(string, True, color))
    elif type(arr) == str:
        rv.append(font.render(arr, True, color))
    return rv

def create_text_str(arr, font_size, color=BLACK) -> pygame.font.SysFont:
    font = pygame.font.SysFont('chalkduster.tff', font_size)
    if type(arr) == list:
        raise TypeError("Use function create_text(...)")
    elif type(arr) == str:
        return font.render(arr, True, color)