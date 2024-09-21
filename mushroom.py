import pygame

class Mushroom(pygame.sprite.Sprite):
    
    def __init__(self, screen, position_x, position_y):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        
        # Definir el tamaño inicial del hongo
        self.width = 20
        self.height = 20
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((46, 54, 185))  # Color del hongo
        self.rect = self.image.get_rect()
        
        self.rect.centerx = position_x
        self.rect.bottom = position_y
    
    def bullet_collision(self):
        '''Reduce el tamaño del hongo en el eje y tras colisión con una bala.'''
        
        # Reducir la altura en 5 píxeles
        self.height -= 5
        
        if self.height > 0:
            # Crear una nueva superficie con el nuevo tamaño
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill((46, 54, 185))  # Volver a colorear el hongo
            
            # Actualizar el rectángulo (rect)
            self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        else:
            # Si la altura es 0 o menor, eliminar el hongo
            self.kill()  
