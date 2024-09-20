import pygame
import sys
from centipede import Centipede  


pygame.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Centipede")
clock = pygame.time.Clock()


centipedes = pygame.sprite.Group()
for i in range(8):  
    centipede_segment = Centipede(screen, i * 24, 7 if i == 0 else i, 1)
    centipedes.add(centipede_segment)

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        centipedes.update() # Actualiza las posiciones de los segmentos del centipede
        screen.fill((0, 0, 0))
        centipedes.draw(screen)
        pygame.display.flip()
        clock.tick(60)

game_loop()
