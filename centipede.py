import pygame


class Centipede(pygame.sprite.Sprite):
    def __init__(self, screen, right, number, level):
        """Inicializador que toma la pantalla,
        coordenada right, número, y nivel."""
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.num = number
        self.__right = right
        self.__reached_bottom = False
        self.__level = level
        self.speed_increased = False
        if number == 7:
            self.is_head = True
        else:
            self.is_head = False

        if self.__level == 1:
            self.__dx = -2
        elif self.__level == 2:
            self.__dx = -4
        
        if self.is_head:
            self.image = pygame.image.load('assets/centipede_head.png').convert_alpha()
        else:
            self.image = pygame.image.load('assets/centipede_segment.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.right = self.__screen.screen_width - self.__right
        self.rect.top = 64

    def update(self):
        """Actualiza la posición del centipede en la pantalla."""
        # Movimiento horizontal
        self.rect.right += self.__dx

        # Ver si ha tocado los bordes para cambiar de dirección
        if not self.__reached_bottom:
            if (
                self.rect.left <= 0
                or self.rect.right >= self.__screen.screen_width
            ):
                self.rect.top += 20
                self.__dx = -self.__dx
            if self.rect.bottom == (self.__screen.screen_height + 16):
                self.__reached_bottom = True
                self.rect.top -= 32
        else:
            if (
                self.rect.left <= 0
                or self.rect.right >= self.__screen.screen_width
            ):
                self.rect.top -= 16
                self.__dx = -self.__dx
            if self.rect.top == self.__screen.screen_height - 128:
                self.rect.top += 32
                self.__reached_bottom = False

    # Si choca con un hongo, cambia el sentido del movimiento
    def collide_with_mushroom(self):
        self.__dx = -self.__dx  # Invierte la dirección horizontal
        self.rect.top += 20

    def increase_speed(self):
        """Aumenta la velocidad del centipede."""
        if not self.speed_increased:
            if self.__dx < 0:
                self.__dx -= 1  # Aumentar velocidad negativa (izquierda)
            else:
                self.__dx += 1  # Aumentar velocidad positiva (derecha)
            self.speed_increased = True
