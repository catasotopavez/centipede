import pygame
import sys
from centipede import Centipede
from player import Player
from bullet import Bullet
from mushroom import Mushroom
from spider import Spider
from flea import Flea
from scorpion import Scorpion
import time
import sounds
from settings import WINDOW_WIDTH

from ui import UI
import random

pygame.init()
pygame.mixer.init()

screen = UI()
pygame.display.set_caption("Centipede")

clock = pygame.time.Clock()

shoot_sound = pygame.mixer.Sound('sounds/shoot.mp3')

def create_centipedes(level=1):
    centipedes = pygame.sprite.Group()
    for segments in range(8):  # Número de segmentos
        centipede_segment = Centipede(screen, segments * 24 , segments, level)
        centipedes.add(centipede_segment)
    return centipedes

def generate_mushrooms(mushrooms):
    # Grupo de hongos
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
    return mushrooms


def check_win(level):
    """Verifica si el jugador ha ganado el juego."""
    if level == 3:
        if screen.you_win_menu():
            game_loop()
        else:
            pygame.quit()
            sys.exit()
    return False

 
def check_loss(player, fleas):
    """Verifica si el jugador ha perdido el juego."""
    if player.lives == 0:
        if screen.game_over_menu():
            for flea in fleas:
                flea.kill()
            game_loop()
        else:
            pygame.quit()
            sys.exit()
    return False

def handle_life_loss(current_time, fleas, spiders, level, centipedes, bullets):
    global animate_mushrooms  # Asegúrate de que esta variable sea global
    animate_mushrooms = True
    
    # Elimina todos los enemigos
    for flea in fleas:
        flea.kill()  
    for spider in spiders:
        spider.kill()
    for centipede in centipedes:
        centipede.kill()
    for bullet in bullets:
        bullet.kill()
    
    # Aquí puedes pausar brevemente para dar tiempo a la reanimación de hongos
    pygame.time.wait(2000)  # Pausa de 1 segundo
    pygame.display.flip() 
    
    # Crear nuevos centípedos para el reinicio del nivel
    centipedes = create_centipedes(level)
    last_spider_spawn = current_time
    last_scorpion_spawn = current_time

    cannot_pass_level = True
    
    return last_spider_spawn, last_scorpion_spawn, animate_mushrooms, cannot_pass_level, centipedes

def event_handler(event: pygame.event.Event, player, bullets):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # Combine KEYDOWN checks into a single block
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:  # Pause the game
            if not screen.pause_menu('PAUSED'):
                running = False
                return
        elif event.key == pygame.K_LEFT:
            player.move_left()
        elif event.key == pygame.K_RIGHT:
            player.move_right()
        elif event.key == pygame.K_SPACE:  # Shoot bullet
            bullet = Bullet(screen, player)
            sounds.shooting()
            bullets.add(bullet)

    # Handle stopping movement when keys are released
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

    screen.start_menu()

    centipedes = create_centipedes()
    level = 1
    score = 0
    first_generation = True
    player = Player(screen)
    animate_mushrooms = False
    cannot_pass_level = False

    # Grupo para hongos animados
    animated_mushrooms = pygame.sprite.Group()
    animate_mushrooms = False
    
    # Grupo de proyectiles
    bullets = pygame.sprite.Group()

    fleas = pygame.sprite.Group()
    flea_spawn_time = 7000
    last_flea_spawn = pygame.time.get_ticks()

    sprites_to_draw = 0
    animation_speed = 1  # Velocidad de la animación (0.5 segundos entre sprites)
    last_time = time.time()
    
    mushrooms_group = pygame.sprite.Group()
    mushrooms = generate_mushrooms(mushrooms_group)

    spiders = pygame.sprite.Group()
    spider_spawn_time = 7000
    last_spider_spawn = pygame.time.get_ticks()

    scorpions = pygame.sprite.Group()
    scorpion_spawn_time = 10000
    last_scorpion_spawn = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            event_handler(event, player, bullets)

        # Actualizar posiciones
        player.update()
        centipedes.update()
        bullets.update()
        spiders.update()
        fleas.update()
        scorpions.update()

        #MODIFICAR ACA EL NIVEL DE LA PULGA
        if level >= 1 and current_time - last_flea_spawn > flea_spawn_time:
            flea = Flea(screen, mushrooms)
            fleas.add(flea)
            last_flea_spawn = current_time

        # Crear un nuevo escorpión cada cierto tiempo
        if current_time - last_scorpion_spawn > scorpion_spawn_time:
            scorpion = Scorpion(screen, mushrooms)
            scorpions.add(scorpion)
            last_scorpion_spawn = current_time

        # Verificar colisión entre las balas y las pulgas
        flea_collisions = pygame.sprite.groupcollide(bullets, fleas, True, True)
        if flea_collisions:
            score += 50  # Sumar puntos por cada pulga eliminada
            for flea in flea_collisions.values():
                flea[0].kill()  # Asegurarse de que la pulga se elimina correctamente
            print("Pulga eliminada")

         # Verificar colisiones entre jugador y pulgas
        if pygame.sprite.spritecollideany(player, fleas):
            player.lives -= 1  # Reducir la vida del jugador
            check_loss(player, fleas)  # Verificar si el jugador ha perdido todas las vidas
            last_spider_spawn, last_scorpion_spawn, animate_mushrooms, cannot_pass_level, centipedes = handle_life_loss(current_time, fleas, spiders, level, centipedes, bullets)
            player.rect.centerx = screen.screen_width // 2
            player.rect.bottom = screen.screen_height - 10

        # Crear una nueva araña
        if current_time - last_spider_spawn > spider_spawn_time:
            spider = Spider(screen)
            spiders.add(spider)
            last_spider_spawn = current_time

        # Colisiones entre balas y arañas
        spider_collisions = pygame.sprite.groupcollide(bullets, spiders, True, True)
        if spider_collisions:
            score += 20  # Aumentar puntaje por cada araña eliminada
            print("Araña eliminada")

        # Colisión con hongos
        collided_mushroom = pygame.sprite.spritecollide(player, mushrooms, False)
        if collided_mushroom:
            for mushroom in collided_mushroom:
                mushroom_collision_handler(mushroom, player)

        # Verificar colisión con centipede
        if pygame.sprite.spritecollideany(player, centipedes):
            player.lives -= 1
            check_loss(player, fleas)
            animate_mushrooms = True
            last_spider_spawn, last_scorpion_spawn, animate_mushrooms, cannot_pass_level, centipedes = handle_life_loss(current_time, fleas, spiders, level, centipedes, bullets)
            player.rect.centerx = screen.screen_width // 2
            player.rect.bottom = screen.screen_height - 10

        # Colisiones entre balas y centipede
        collisions = pygame.sprite.groupcollide(bullets, centipedes, True, True)
        centipede_numbers = [centipede.num for centipede in centipedes]

        for bullet, hit_centipedes in collisions.items():
            new_mushroom = Mushroom(
                screen,
                hit_centipedes[0].rect.x,
                hit_centipedes[0].rect.y + 20,
            )
            score += 10 * len(hit_centipedes)


            # Cambiar la cabeza del centipede si corresponde
            if hit_centipedes[0].num - 1 in centipede_numbers:
                position_in_centipedes = centipede_numbers.index(hit_centipedes[0].num - 1)
                new_head = centipedes.sprites()[position_in_centipedes]
                new_head.is_head = True
                new_head.image = pygame.image.load('assets/centipede_head.png').convert_alpha()
                new_head.image = pygame.transform.scale(new_head.image, (20, 20))

        # Verificar colisiones con arañas
        if pygame.sprite.spritecollideany(player, spiders):
            player.lives -= 1
            check_loss(player, fleas)
            last_spider_spawn, last_scorpion_spawn, animate_mushrooms, cannot_pass_level, centipedes = handle_life_loss(current_time, fleas, spiders, level, centipedes, bullets)
            player.rect.centerx = screen.screen_width // 2
            player.rect.bottom = screen.screen_height - 10

        for centipede in centipedes:
            if centipede.is_head:
                if centipede.num - 1 not in centipede_numbers:
                    centipede.increase_speed()

            collided_mushrooms = pygame.sprite.spritecollide(centipede, mushrooms, False)
            if collided_mushrooms:
                centipede.collide_with_mushroom()

        if not centipedes and check_win(level) is False and not cannot_pass_level:
            centipedes = create_centipedes(level)
            for centipede in centipedes:
                centipede.increase_speed()
            level += 1

        # Colisiones entre balas y escorpiones
        scorpion_collisions = pygame.sprite.groupcollide(bullets, scorpions, True, True)
        if scorpion_collisions:
            score += 30  # Sumar puntos por cada escorpión eliminado
            print("Escorpión eliminado")
            for scorpion in scorpion_collisions.values():
                scorpion[0].kill()

        # Colisiones entre balas y hongos
        for mushroom in mushrooms:
            collided_bullets = pygame.sprite.spritecollide(mushroom, bullets, False)
            if collided_bullets:
                if mushroom.bullet_collision():
                    score += 1
                    new_mushroom = Mushroom(screen, mushroom.rect.centerx, mushroom.rect.bottom)
                    animated_mushrooms.add(new_mushroom)
                    sounds.mushroom_destroyed()
                    print("Elimino un hongo")
                collided_bullets[0].kill()

        # Dibujar
        screen.screen.fill((0, 0, 0))
        bullets.draw(screen.screen)

        # Animar hongos golpeados (en `animated_mushrooms`)
        if animate_mushrooms:
            current_time = time.time()
            if current_time - last_time > animation_speed and sprites_to_draw < len(animated_mushrooms):
                sprites_to_draw += 1
                last_time = current_time
                sounds.animate_mushroom_sound()

            # Dibuja los hongos animados uno por uno
            for i, sprite in enumerate(animated_mushrooms):
                if i < sprites_to_draw:
                    screen.screen.blit(sprite.image, sprite.rect)

            # Si todos los hongos fueron dibujados, muévelos al grupo `mushrooms`
            if sprites_to_draw >= len(animated_mushrooms):
                for mushroom in animated_mushrooms:
                    mushrooms.add(mushroom)
                animated_mushrooms.empty()  # Vacía el grupo de hongos animados
                sprites_to_draw = 0
                animate_mushrooms = False
                time.sleep(0.5)

        # Dibujar otros elementos
        if first_generation:
            mushrooms.draw(screen.screen)
            pygame.display.flip()
            first_generation = False
            time.sleep(2)
        else:
            mushrooms.draw(screen.screen)
        if animate_mushrooms and len(animated_mushrooms) == 0:
            screen.screen.blit(player.image, player.rect)
            spiders.draw(screen.screen)
            fleas.draw(screen.screen)
            scorpions.draw(screen.screen)
            centipedes.draw(screen.screen)
            cannot_pass_level = False
        if not animate_mushrooms:
            screen.screen.blit(player.image, player.rect)
            spiders.draw(screen.screen)
            fleas.draw(screen.screen)
            scorpions.draw(screen.screen)
            centipedes.draw(screen.screen)
        screen.display_score(score)
        screen.show_ui(player, level)
        screen.show_pause()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
