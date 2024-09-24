import pygame
import random
from mushroom import Mushroom

import pygame
import random

class Flea(pygame.sprite.Sprite):
    def __init__(self, screen, mushrooms):
        """Inicializa la pulga que cae verticalmente y genera hongos."""
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.mushrooms = mushrooms  
        self.image = pygame.image.load('assets/flea.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.__screen.screen_width - self.rect.width)
        self.rect.y = 0 

        # Velocidad de caída
        self.__dy = 3

        self.sound = pygame.mixer.Sound('sounds/flea_sound.mp3')  # Reemplaza con tu archivo de sonido
        self.sound.play(loops=-1)

        # Intervalo entre la generación de hongos (aumentado para menos hongos)
        self.hongo_interval = 100  # Generar un hongo cada 100 píxeles 
        self.last_hongo_y = self.rect.y  


    def update(self):
        """Actualiza la posición de la pulga y genera hongos mientras cae."""
        self.rect.y += self.__dy

        # Verificar si es momento de generar un hongo
        if abs(self.rect.y - self.last_hongo_y) >= self.hongo_interval:
            if random.random() < 0.5:
                self.generate_hongo()
            self.last_hongo_y = self.rect.y

        # Si llega al fondo, eliminar la pulga
        if self.rect.y > self.__screen.screen_height:
            self.sound.stop() 
            self.kill()

    def generate_hongo(self):
        """Genera un hongo en la posición actual de la pulga."""
        new_mushroom = Mushroom(self.__screen, self.rect.x, self.rect.y)
        self.mushrooms.add(new_mushroom)
    
    def kill(self):
        """Cuando se destruye la pulga, detener el sonido y eliminar el sprite."""
        self.sound.stop()  # Detener el sonido al eliminar la pulga
        super().kill()