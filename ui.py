import pygame
from button import Button
from settings import *
import sounds

class UI:
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 700
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        pygame.display.set_caption("Centipede")

    def display_score(self, score):
        """Muestra el puntaje en la pantalla."""
        score_text = self.get_font(14).render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def show_pause(self):
        """Muestra el puntaje en la pantalla."""
        score_text = self.get_font(14).render(f"P to Pause", True, (255, 255, 255))
        self.screen.blit(score_text, (450, 10))

    def show_ui(self, player, level, flip=True):
        """Muestra la cantidad de vidas y el nivel actual en la pantalla."""

        filled_heart_img = pygame.image.load("assets/images/filled_heart.png")
        desired_width = 20
        desired_height = 20
        filled_heart_img = pygame.transform.scale(filled_heart_img, (desired_width, desired_height))

        for i in range(3):
            x_position = (20 + 10) * (i + 1)
            y_position = 40
            if i < player.lives:
                self.screen.blit(filled_heart_img, (x_position, y_position))

        level_text = self.get_font(12).render(f"Level: {level}", True, (255, 255, 255))
        self.screen.blit(level_text, (10, 70))
        if flip:
            pygame.display.flip()

    def pause_menu(self, reason):
        """Display pause menu with continue and quit options."""
        bg = BACKGROUND
        menu_running = True
        while menu_running:
            self.screen.blit(bg, (50, 50))
            mouse_pos = pygame.mouse.get_pos()

            pause_text = self.get_font(36).render(f"{reason}", True, (255, 255, 255))
            pause_rect = pause_text.get_rect(center=(self.screen_width // 2, 100))

            continue_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(50 + WINDOW_WIDTH // 2, 250),
                text_input="CONTINUE",
                font=self.get_font(25),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            quit_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(50 + WINDOW_WIDTH // 2, 400),
                text_input="QUIT",
                font=self.get_font(25),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            self.screen.blit(pause_text, pause_rect)

            # Update and draw buttons
            for button in [continue_button, quit_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if continue_button.checkForInput(mouse_pos):
                        menu_running = False  # Exit pause menu to continue the game
                    if quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

    def start_menu(self):
        """Display pause menu with continue and quit options."""
        sounds.menu()

        bg = BACKGROUND
        menu_running = True
        while menu_running:
            self.screen.blit(bg, (50, 50))
            mouse_pos = pygame.mouse.get_pos()

            menu_text = self.get_font(36).render(f"Start Menu", True, (255, 255, 255))
            menu_rect = menu_text.get_rect(center=(self.screen_width // 2, 100))

            play_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(50 + WINDOW_WIDTH // 2, 250),
                text_input="Start",
                font=self.get_font(25),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            quit_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(50 + WINDOW_WIDTH // 2, 400),
                text_input="QUIT",
                font=self.get_font(25),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            self.screen.blit(menu_text, menu_rect)

            for button in [play_button, quit_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(mouse_pos):
                        sounds.stop_music()
                        menu_running = False  # Exit pause menu to continue the game
                    if quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

    def game_over_menu(self):
        """Display game over menu with main menu and quit options."""
        sounds.game_over()
        bg = BACKGROUND
        menu_running = True
        while menu_running:
            self.screen.blit(bg, (50, 50))
            mouse_pos = pygame.mouse.get_pos()

            game_over_text = self.get_font(36).render(f"GAME OVER", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, 100))

            main_menu_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(50 + WINDOW_WIDTH // 2, 250),
                text_input="Main Menu",
                font=self.get_font(25),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            quit_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(50 + WINDOW_WIDTH // 2, 400),
                text_input="QUIT",
                font=self.get_font(25),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            self.screen.blit(game_over_text, game_over_rect)

            for button in [main_menu_button, quit_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if main_menu_button.checkForInput(mouse_pos):

                        return True
                    if quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

        return True

    def you_win_menu(self):
        """Display win menu with restart and quit options."""
        sounds.victory()
        bg = BACKGROUND
        menu_running = True
        while menu_running:
            self.screen.blit(bg, (50, 50))
            mouse_pos = pygame.mouse.get_pos()

            won_text = self.get_font(36).render(f"YOU WIN!", True, (0, 255, 0))
            won_rect = won_text.get_rect(center=(self.screen_width // 2, 100))

            restart_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(50 + WINDOW_WIDTH // 2, 250),
                text_input="Main Menu",
                font=self.get_font(25),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            quit_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(50 + WINDOW_WIDTH // 2, 400),
                text_input="QUIT",
                font=self.get_font(25),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            self.screen.blit(won_text, won_rect)

            # Update and draw buttons
            for button in [restart_button, quit_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.checkForInput(mouse_pos):
                        return True
                    if quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

        return True
