import pygame
import sys
from centipede import Centipede
from player import Player

pygame.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Centipede")

clock = pygame.time.Clock()

player = Player(screen)

centipedes = pygame.sprite.Group()
for i in range(8):  # Número de segmentos del centipede
    centipede_segment = Centipede(screen, i * 24, 7 if i == 0 else i, 1)
    centipedes.add(centipede_segment)

def display_game_over():
    '''Muestra un mensaje de Game Over en el centro de la pantalla.'''
    font = pygame.font.SysFont(None, 55)
    game_over_text = font.render("Game Over", True, (255, 0, 0))  # Texto rojo
    screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 30))
    pygame.display.flip()

    # Pausa para que el jugador vea el mensaje
    pygame.time.wait(2000)

def game_loop():
    while True:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop()

        # Actualizar posiciones
        player.update()
        centipedes.update()

        # Verificar colisión entre el jugador y el centipede
        if pygame.sprite.spritecollideany(player, centipedes):
            display_game_over()  
            pygame.quit()
            sys.exit()

        # Dibujar en pantalla
        screen.fill((0, 0, 0))  
        centipedes.draw(screen)
        screen.blit(player.image, player.rect)  

        pygame.display.flip()
        clock.tick(60)


game_loop()
