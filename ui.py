import pygame
from settings import *
from button import Button
from assets.images import *

class UI:
    def __init__(self):
        self.screen_width = WINDOW_WIDTH
        self.screen_height = WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Centipede")

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def start_menu(self, bg):

        menu_running = True
        while menu_running:
            self.screen.blit(bg, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            menu_text = self.get_font(45).render("MAIN MENU", True, (255, 255, 255))
            menu_rect = menu_text.get_rect(center=(self.screen_width // 2, 100))

            choose_text = self.get_font(35).render("Choose a level", True, (255, 255, 255))
            choose_rect = choose_text.get_rect(center=(self.screen_width // 2, 150))

            play_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(self.screen_width // 2, 250),
                text_input="PLAY",
                font=self.get_font(50),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            # Quit button
            quit_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(self.screen_width // 2, 500),
                text_input="QUIT",
                font=self.get_font(30),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            self.screen.blit(menu_text, menu_rect)
            self.screen.blit(choose_text, choose_rect)

            for button in [play_button, quit_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(mouse_pos):
                        menu_running = False  # Exit pause menu to continue the game
                    if quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

    def pause_menu(self, bg):
        """Display pause menu with continue and quit options."""
        menu_running = True
        while menu_running:
            self.screen.blit(bg, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            pause_text = self.get_font(100).render("PAUSED", True, (255, 255, 255))
            pause_rect = pause_text.get_rect(center=(self.screen_width // 2, 100))

            continue_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(self.screen_width // 2, 250),
                text_input="CONTINUE",
                font=self.get_font(50),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            quit_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(self.screen_width // 2, 400),
                text_input="QUIT",
                font=self.get_font(50),
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

    def game_over_menu(self, bg):
        """Display game over menu with main menu and quit options."""
        menu_running = True
        while menu_running:
            self.screen.blit(bg, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            game_over_text = self.get_font(100).render("YOU LOST", True, (255, 255, 255))
            game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, 100))

            main_menu_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(self.screen_width // 2, 250),
                text_input="MAIN MENU",
                font=self.get_font(50),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            quit_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(self.screen_width // 2, 400),
                text_input="QUIT",
                font=self.get_font(50),
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

    def you_win_menu(self, bg):
        """Display win menu with restart and quit options."""
        menu_running = True
        while menu_running:
            self.screen.blit(bg, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            won_text = self.get_font(80).render("YOU WIN!", True, (255, 255, 255))
            won_rect = won_text.get_rect(center=(self.screen_width // 2, 100))

            restart_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(self.screen_width // 2, 250),
                text_input="RESTART",
                font=self.get_font(50),
                base_color=(255, 255, 255),
                hovering_color="White"
            )

            quit_button = Button(
                image=pygame.image.load('assets/images/quit_button.png'),
                pos=(self.screen_width // 2, 400),
                text_input="QUIT",
                font=self.get_font(50),
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
