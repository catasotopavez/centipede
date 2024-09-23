import pygame
import random

class Spider(pygame.sprite.Sprite):
    def __init__(self, screen):
        """Inicializa la araña con su imagen, posición y velocidad."""
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen

        # Cargar la imagen de la araña
        self.image = pygame.image.load('assets/spider.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))  # Ajusta el tamaño si es necesario

        self.rect = self.image.get_rect()

        # Posición inicial en la parte inferior de la pantalla
        self.rect.x = random.randint(0, self.__screen.screen_width - self.rect.width)
        self.rect.y = random.randint(self.__screen.screen_height - 100, self.__screen.screen_height - 50)

        # Velocidad de movimiento
        self.__dx = random.choice([-2, 2])  # Movimiento horizontal aleatorio
        self.__dy = 1  # Movimiento vertical para el zigzag
        self.moving_up = True  # Controla si la araña está subiendo o bajando

        # Temporizador para vida útil de la araña
        self.lifetime = random.randint(3000, 5000)  # Duración de la araña en milisegundos (3-5 segundos)
        self.creation_time = pygame.time.get_ticks()  # Momento en que la araña fue creada

    def update(self):
        """Actualiza la posición de la araña en un movimiento en zigzag."""
        current_time = pygame.time.get_ticks()

        # Movimiento horizontal
        self.rect.x += self.__dx

        # Movimiento en zigzag vertical
        if self.moving_up:
            self.rect.y -= self.__dy
            if self.rect.y <= self.__screen.screen_height - 100:
                self.moving_up = False
        else:
            self.rect.y += self.__dy
            if self.rect.y >= self.__screen.screen_height - 50:
                self.moving_up = True

        # Invertir la dirección si toca los bordes horizontales
        if self.rect.left < 0 or self.rect.right > self.__screen.screen_width:
            self.__dx = -self.__dx

        # Desaparecer después de un tiempo
        if current_time - self.creation_time > self.lifetime:
            self.kill()  # Elimina la araña cuando su tiempo de vida ha terminado
