import pygame
import sys
from centipede import Centipede
from player import Player
from bullet import Bullet
from mushroom import Mushroom
from ui import UI
import random

pygame.init()

screen = UI()
pygame.display.set_caption("Centipede")

clock = pygame.time.Clock()

player = Player(screen)


def show_ui(player, level, flip=True):
    """Muestra la cantidad de vidas y el nivel actual en la pantalla."""
    font = pygame.font.SysFont(None, 30)
    lives_text = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))
    screen.blit(level_text, (10, 40))
    if flip:
        pygame.display.flip()


def create_centipedes(level=1):
    centipedes = pygame.sprite.Group()
    for segments in range(8):  # Número de segmentos
        centipede_segment = Centipede(
            screen, segments * 24, segments, level
        )
        centipedes.add(centipede_segment)
    return centipedes


# Grupo de proyectiles
bullets = pygame.sprite.Group()

# Grupo de hongos
mushrooms = pygame.sprite.Group()
mushrooms_x = []
mushrooms_y = []
for j in range(20):  # Número de hongos
    position_x = random.randint(20, screen.screen_width - 20)
    while (
        position_x in mushrooms_x
        or position_x + 20 in mushrooms_x
        or position_x - 20 in mushrooms_x
    ):
        position_x = random.randint(20, screen.screen_width - 20)
    mushrooms_x.append(position_x)
    position_y = random.randint(20, screen.screen_height - 20)
    while (
        position_y in mushrooms_y
        or position_y + 20 in mushrooms_y
        or position_y - 20 in mushrooms_y
    ):
        position_y = random.randint(20, screen.screen_width - 20)
    mushrooms_y.append(position_y)
    mushroom = Mushroom(screen, position_x, position_y)
    mushrooms.add(mushroom)


def check_win(level):
    """Verifica si el jugador ha ganado el juego."""
    if level == 3:
        screen.display_win()
        pygame.quit()
        sys.exit()
    return False


def check_loss(player):
    """Verifica si el jugador ha perdido el juego."""
    if player.lives == 0:
        screen.display_game_over()
        pygame.quit()
        sys.exit()
    return False


def event_handler(event: pygame.event.Event):
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


def mushroom_collision_handler(mushroom, player):
    if (
        player.rect.right > mushroom.rect.left
        and player.rect.left < mushroom.rect.right
    ):
        if (
            player.rect.centery < mushroom.rect.centery
        ):  # Si el jugador está arriba
            player.rect.bottom = mushroom.rect.top
        elif (
            player.rect.centery > mushroom.rect.centery
        ):  # Si el jugador está abajo
            player.rect.top = mushroom.rect.bottom
    if (
        player.rect.bottom > mushroom.rect.top
        and player.rect.top < mushroom.rect.bottom
    ):
        if (
            player.rect.centerx < mushroom.rect.centerx
        ):  # Si el jugador está a la izquierda
            player.rect.right = mushroom.rect.left
        elif (
            player.rect.centerx > mushroom.rect.centerx
        ):  # Si el jugador está a la derecha
            player.rect.left = mushroom.rect.right


def game_loop():
    centipedes = create_centipedes()
    level = 1
    while True:
        # show_ui(player, level)
        for event in pygame.event.get():
            event_handler(event)

        # Actualizar posiciones
        player.update()
        centipedes.update()
        bullets.update()

        collided_mushroom = pygame.sprite.spritecollide(
            player, mushrooms, False
        )

        if collided_mushroom:
            # Ajustar la posición del jugador para evitar que traspase el hongo
            for mushroom in collided_mushroom:
                mushroom_collision_handler(mushroom, player)

        # Verificar colisión entre el jugador y el centipede
        if pygame.sprite.spritecollideany(player, centipedes):
            player.lives -= 1
            check_loss(player)
            player.rect.centerx = screen.screen_width // 2
            player.rect.bottom = screen.screen_height - 10

        # Verificar colisiones entre balas y segmentos del centipede
        collisions = pygame.sprite.groupcollide(
            bullets, centipedes, True, True
        )

        for bullet, hit_centipedes in collisions.items():
            new_mushroom = Mushroom(
                screen,
                hit_centipedes[0].rect.x,
                hit_centipedes[0].rect.y + 20,
            )
            mushrooms.add(new_mushroom)

        if pygame.sprite.spritecollideany(player, centipedes):
            screen.display_game_over()
            pygame.quit()
            sys.exit()

        centipede_numbers = [centipede.num for centipede in centipedes]
        for centipede in centipedes:
            # Verificar si el centipede quedo solo (solo una cabeza),
            # para aumentar su velocidad.
            if centipede.num == len(centipedes) - 1:  # Si es el último,
                # solo hay que chequear que el penultimo exista
                if centipede.num - 1 not in centipede_numbers:
                    centipede.increase_speed()
            elif (
                centipede.num == 0
            ):  # Si es el primero, chequeamos que el segundo no exista
                if centipede.num + 1 not in centipede_numbers:
                    centipede.increase_speed()
            else:
                if (
                    centipede.num + 1 not in centipede_numbers
                    and centipede.num - 1 not in centipede_numbers
                ):
                    centipede.increase_speed()

            # Verificar si este centipede en particular choca con algún hongo
            collided_mushrooms = pygame.sprite.spritecollide(
                centipede, mushrooms, False
            )

            if collided_mushrooms:
                # Si chocó con algún hongo, invierte la dirección del centipede
                centipede.collide_with_mushroom()

        if not centipedes and check_win(level) is False:
            centipedes = create_centipedes(level)
            for centipede in centipedes:
                centipede.increase_speed()
            level += 1

        for mushroom in mushrooms:
            # Verificar si el hongo fue chocado por una bala
            collided_bullets = pygame.sprite.spritecollide(
                mushroom, bullets, False
            )

            if collided_bullets:
                mushroom.bullet_collision()
                collided_bullets[0].kill()

        # Dibujar
        screen.screen.fill((0, 0, 0))
        centipedes.draw(screen.screen)
        bullets.draw(screen.screen)
        mushrooms.draw(screen.screen)
        screen.screen.blit(player.image, player.rect)

        pygame.display.flip()
        clock.tick(60)


game_loop()
