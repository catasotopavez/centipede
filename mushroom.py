import pygame

class Mushroom(pygame.sprite.Sprite):

    def __init__(self, screen, position_x, position_y):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.poisoned = False 

        # Cargar las tres imágenes del hongo
        self.mushroom_images = [
            pygame.image.load('assets/mushroom_full.png').convert_alpha(),
            pygame.image.load('assets/mushroom_damaged.png').convert_alpha(),
            pygame.image.load('assets/mushroom_critical.png').convert_alpha()
        ]

        # Escalar las imágenes si es necesario (opcional)
        self.mushroom_images = [pygame.transform.scale(img, (20, 20)) for img in self.mushroom_images]

        # Establecer la primera imagen como la inicial
        self.image = self.mushroom_images[0]

        # Rectángulo para la posición del hongo
        self.rect = self.image.get_rect()
        self.rect.centerx = position_x
        self.rect.bottom = position_y

        # Estado del hongo (3 estados: completo, dañado, crítico)
        self.state = 0  # Comienza con la primera imagen

    def bullet_collision(self):
        """Cambia la imagen del hongo al ser golpeado por una bala."""

        # Incrementar el estado del hongo (cambiar de imagen)
        self.state += 1

        if self.state < len(self.mushroom_images):
            # Cambiar a la siguiente imagen de daño
            self.image = self.mushroom_images[self.state]
        else:
            # Si el estado es mayor que el número de imágenes, el hongo es destruido
            self.kill()
            return True  # Indicar que el hongo fue destruido

        return False  # El hongo no ha sido destruido aún
    def poison(self):
            """Envenena el hongo cambiando su color."""
            self.poisoned = True
            self.image = pygame.image.load('assets/mushroom_poisoned.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (20, 20)) 
