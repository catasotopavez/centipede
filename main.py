import pygame
import sys
from centipede import Centipede
from player import Player
from bullet import Bullet
from mushroom import Mushroom
import random

pygame.init()

screen_width = 640
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Centipede")

clock = pygame.time.Clock()

player = Player(screen)


centipedes = pygame.sprite.Group()
for i in range(8):  # Número de segmentos
    centipede_segment = Centipede(screen, i * 24, i, 1)
    centipedes.add(centipede_segment)

# Grupo de proyectiles
bullets = pygame.sprite.Group()
    
# Grupo de hongos
mushrooms = pygame.sprite.Group()
mushrooms_x = []
mushrooms_y = []
for j in range(20): # Número de hongos
    position_x = random.randint(20, screen_width - 20)
    while position_x in mushrooms_x or position_x + 20 in mushrooms_x or position_x - 20 in mushrooms_x:
        position_x = random.randint(20, screen_width - 20)
    mushrooms_x.append(position_x)
    position_y = random.randint(20, screen_height - 20)
    while position_y in mushrooms_y or position_y + 20 in mushrooms_y or position_y - 20 in mushrooms_y:
        position_y = random.randint(20, screen_width - 20)
    mushrooms_y.append(position_y)
    mushroom = Mushroom(screen, position_x, position_y)
    mushrooms.add(mushroom)
    

def display_game_over():
    '''Muestra un mensaje de Game Over en el centro de la pantalla.'''
    font = pygame.font.SysFont(None, 55)
    game_over_text = font.render("Game Over", True, (255, 0, 0))  # Texto rojo
    screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_SPACE:  # Disparar
                    bullet = Bullet(screen, player)
                    bullets.add(bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop()

        # Actualizar posiciones
        player.update()
        centipedes.update()
        bullets.update()  

        # Verificar colisión entre el jugador y el centipede
        if pygame.sprite.spritecollideany(player, centipedes):
            display_game_over()
            pygame.quit()
            sys.exit()

        # Verificar colisiones entre balas y segmentos del centipede
        collisions = pygame.sprite.groupcollide(bullets, centipedes, True, True)

        for bullet, hit_centipedes in collisions.items():
            new_mushroom = Mushroom(screen, hit_centipedes[0].rect.x, hit_centipedes[0].rect.y + 20)
            mushrooms.add(new_mushroom)
            

        if pygame.sprite.spritecollideany(player, centipedes):
            display_game_over()
            pygame.quit()
            sys.exit()
        
        centipede_numbers = [centipede.num for centipede in centipedes]
        for centipede in centipedes:
            # Verificar si el centipede quedo solo (solo una cabeza), para aumentar su velocidad.
            if centipede.num == len(centipedes) - 1: # Si es el último, solo hay que chequear que el penultimo exista 
                if centipede.num - 1 not in centipede_numbers:
                    centipede.increase_speed()
            elif centipede.num == 0: # Si es el primero, chequeamos que el segundo no exista
                if centipede.num + 1 not in centipede_numbers:
                    centipede.increase_speed()
            else: 
                if centipede.num + 1 not in centipede_numbers and centipede.num - 1 not in centipede_numbers:
                    centipede.increase_speed()
            
            # Verificar si este centipede en particular choca con algún hongo
            collided_mushrooms = pygame.sprite.spritecollide(centipede, mushrooms, False)
            
            if collided_mushrooms:
                # Si chocó con algún hongo, invierte la dirección del centipede
                centipede.collide_with_mushroom()
        
        for mushroom in mushrooms:
            # Verificar si el hongo fue chocado por una bala 
            collided_bullets = pygame.sprite.spritecollide(mushroom, bullets, False)
            
            if collided_bullets:
                mushroom.bullet_collision()
                collided_bullets[0].kill()
                

        # Dibujar 
        screen.fill((0, 0, 0))  
        centipedes.draw(screen)
        bullets.draw(screen)  
        mushrooms.draw(screen)
        screen.blit(player.image, player.rect)  

        pygame.display.flip()
        clock.tick(60)


game_loop()
