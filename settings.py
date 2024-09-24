import pygame

def load_and_scale_background(image_path, window_width, window_height):
    bg = pygame.image.load(image_path)
    return pygame.transform.scale(bg, (window_width, window_height))

WINDOW_WIDTH = 640 - 100
WINDOW_HEIGHT = 700 - 100

BACKGROUND = load_and_scale_background('assets/images/background.png', WINDOW_WIDTH, WINDOW_HEIGHT)
