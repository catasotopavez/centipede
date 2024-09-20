import pygame

class Centipede(pygame.sprite.Sprite):
    def __init__(self, screen, right, number, level):
        '''Inicializador que toma la pantalla, coordenada right, número, y nivel.'''
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.__num = number
        self.__right = right
        self.__reached_bottom = False
        self.__level = level


        if self.__level == 1:
            self.image = pygame.Surface((20, 20))
            self.image.fill((0, 255, 0)) 
            self.__dx = -2
        elif self.__level == 2:
            self.image = pygame.Surface((20, 20))
            self.image.fill((0, 0, 255))  
            self.__dx = -4

        self.rect = self.image.get_rect()
        self.rect.right = self.__screen.get_width() - self.__right
        self.rect.top = 64

    def update(self):
        '''Actualiza la posición del centipede en la pantalla.'''
        # Movimiento horizontal
        self.rect.right += self.__dx

        # Ver si ha tocado los bordes para cambiar de dirección
        if not self.__reached_bottom:
            if self.rect.left <= 0 or self.rect.right >= self.__screen.get_width():
                self.rect.top += 16
                self.__dx = -self.__dx
            if self.rect.bottom == (self.__screen.get_height() + 16):
                self.__reached_bottom = True
                self.rect.top -= 32
        else:
            if self.rect.left <= 0 or self.rect.right >= self.__screen.get_width():
                self.rect.top -= 16
                self.__dx = -self.__dx
            if self.rect.top == self.__screen.get_height() - 128:
                self.rect.top += 32
                self.__reached_bottom = False
