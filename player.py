import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        '''Inicializa el jugador con su imagen, posición y velocidad.'''
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen

        self.image = pygame.Surface((40, 20))
        self.image.fill((255, 255, 255)) 
        self.rect = self.image.get_rect()

        # Posición inicial del jugador
        self.rect.centerx = self.__screen.get_width() // 2
        self.rect.bottom = self.__screen.get_height() - 10

        # Velocidad de movimiento
        self.__dx = 0
        self.__speed = 5

    def update(self):
        '''Actualiza la posición del jugador basado en la entrada del teclado.'''
        # Actualizar posición horizontal
        self.rect.x += self.__dx

        # Evitar que el jugador salga de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.__screen.get_width():
            self.rect.right = self.__screen.get_width()

    def move_left(self):
        self.__dx = -self.__speed

    def move_right(self):
        self.__dx = self.__speed

    def stop(self):
        self.__dx = 0
