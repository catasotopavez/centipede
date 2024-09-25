import pygame
import random

class Scorpion(pygame.sprite.Sprite):
    def __init__(self, screen, mushrooms):
        """Inicializa el escorpión que se mueve horizontalmente y envenena hongos."""
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.mushrooms = mushrooms  # Referencia al grupo de hongos

        # Cargar la imagen del escorpión
        self.image = pygame.image.load('assets/scorpion.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Establecer la posición inicial (en una coordenada y aleatoria, moviéndose de izquierda a derecha)
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(100, self.__screen.screen_height - 100)  # Movimiento a mitad de pantalla
        self.rect.x = 0  # Comienza desde el lado izquierdo

        # Velocidad de movimiento
        self.__dx = 3

    def update(self):
        """Actualiza la posición del escorpión y envenena hongos si colisiona."""
        self.rect.x += self.__dx  # Movimiento horizontal

        # Si el escorpión sale de la pantalla, lo eliminamos
        if self.rect.x > self.__screen.screen_width:
            self.kill()

        # Verificar colisión con hongos
        collided_mushrooms = pygame.sprite.spritecollide(self, self.mushrooms, False)
        for mushroom in collided_mushrooms:
            mushroom.poison()  # Envenenar el hongo
