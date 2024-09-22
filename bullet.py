import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        """Inicializa el proyectil desde la posición del jugador."""
        super().__init__()
        self.screen = screen

        # Crear el proyectil como un pequeño rectángulo
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 255))  # Blanco

        # Posicionar el proyectil justo por encima del jugador
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

        # Velocidad del proyectil
        self.speed_y = -10

    def update(self):
        """Actualiza la posición del proyectil en la pantalla."""
        # Mover el proyectil hacia arriba
        self.rect.y += self.speed_y

        # Si el proyectil sale de la pantalla, lo destruimos
        if self.rect.bottom < 0:
            self.kill()
