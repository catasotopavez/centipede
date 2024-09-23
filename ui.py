import pygame

class UI:
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 700
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        pygame.display.set_caption("Centipede")

    def display_game_over(self):
        """Muestra un mensaje de Game Over en el centro de la pantalla."""
        font = pygame.font.SysFont(None, 55)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(
            game_over_text,
            (self.screen_width // 2 - 100, self.screen_height // 2 - 30),
        )
        pygame.display.flip()
        pygame.time.wait(2000)

    def display_win(self):
        """Muestra un mensaje de victoria en el centro de la pantalla."""
        font = pygame.font.SysFont(None, 55)
        win_text = font.render("You Win!", True, (0, 255, 0))  # Texto verde
        self.screen.blit(
            win_text,
            (self.screen_width // 2 - 100, self.screen_height // 2 - 30),
        )
        pygame.display.flip()
        pygame.time.wait(2000)

    def display_score(self, score):
        """Muestra el puntaje en la pantalla."""
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def show_ui(self, player, level, flip=True):
        """Muestra la cantidad de vidas y el nivel actual en la pantalla."""
        font = pygame.font.SysFont(None, 30)
        lives_text = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
        level_text = font.render(f"Level: {level}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 40))  # Just below the score
        self.screen.blit(level_text, (10, 70))
        if flip:
            pygame.display.flip()
