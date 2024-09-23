import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        """Inicializa el jugador con su imagen, posición y velocidad."""
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.image = pygame.image.load('assets/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.rect = self.image.get_rect()
        self.lives = 3

        # Posición inicial del jugador
        self.rect.centerx = self.__screen.screen_width // 2
        self.rect.bottom = self.__screen.screen_height - 10

        # Velocidad de movimiento
        self.__dx = 0
        self.__dy = 0
        self.__speed = 5

    def update(self):
        """Actualiza la posición del jugador basado en el input del teclado."""
        # Actualizar posición horizontal
        self.rect.x += self.__dx
        self.rect.y += self.__dy

        # Evitar que el jugador salga de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.__screen.screen_width:
            self.rect.right = self.__screen.screen_width

        # Evitar que el jugador suba más que un quinto de la pantalla
        limit_top = (4 / 5) * self.__screen.screen_height
        if self.rect.top < limit_top:
            self.rect.top = limit_top

        # Evitar que el jugador baje más del límite inferior de la pantalla
        if self.rect.bottom > self.__screen.screen_height:
            self.rect.bottom = self.__screen.screen_height

    def move_left(self):
        self.__dx = -self.__speed

    def move_right(self):
        self.__dx = self.__speed

    def move_up(self):
        self.__dy = -self.__speed

    def move_down(self):
        self.__dy = self.__speed

    def stop(self):
        self.__dx = 0
