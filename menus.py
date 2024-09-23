import pygame
from button import Button
from settings import *

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def load_and_scale_background(image_path, window_width, window_height):
    bg = pygame.image.load(image_path)
    return pygame.transform.scale(bg, (window_width, window_height))


def show_menu(screen, bg):
    menu_running = True

    while menu_running:
        screen.blit(bg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(45).render("MAIN MENU", True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(WINDOW_WIDTH // 2, 100))

        choose_text = get_font(35).render("Choose a level", True, (255, 255, 255))
        choose_rect = choose_text.get_rect(center=(WINDOW_WIDTH // 2, 150))

        # Create level buttons in two rows of five
        level_buttons = []
        for i in range(10):
            row = i // 5
            col = i % 5
            x = (WINDOW_WIDTH // 2 - 300) + col * 150
            y = 250 + row * 120
            level_buttons.append(Button(
                image=pygame.image.load('assets/images/level_button.png'),
                pos=(x, y),
                text_input=f"{i+1}",
                font=get_font(30),
                base_color=(255, 255, 255),
                hovering_color="White"
            ))

        # Quit button
        quit_button = Button(
            image=pygame.image.load('assets/images/quit_button.png'),
            pos=(WINDOW_WIDTH // 2, 500),
            text_input="QUIT",
            font=get_font(30),
            base_color=(255, 255, 255),
            hovering_color="White"
        )

        screen.blit(menu_text, menu_rect)
        screen.blit(choose_text, choose_rect)

        # Update and draw level buttons
        for button in level_buttons:
            button.changeColor(mouse_pos)
            button.update(screen)

        # Update and draw quit button
        quit_button.changeColor(mouse_pos)
        quit_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(level_buttons):
                    if button.checkForInput(mouse_pos):
                        level = f"level_{i+1}.json"
                        return level
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()


def pause_menu(screen, bg):
    menu_running = True

    while menu_running:
        screen.blit(bg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        pause_text = get_font(100).render("PAUSED", True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, 100))

        continue_button = Button(
            image=pygame.image.load('assets/images/quit_button.png'),
            pos=(WINDOW_WIDTH // 2, 250),
            text_input="CONTINUE",
            font=get_font(50),
            base_color=(255, 255, 255),
            hovering_color="White"
        )

        quit_button = Button(
            image=pygame.image.load('assets/images/quit_button.png'),
            pos=(WINDOW_WIDTH // 2, 400),
            text_input="QUIT",
            font=get_font(50),
            base_color=(255, 255, 255),
            hovering_color="White"
        )

        screen.blit(pause_text, pause_rect)

        # Update and draw buttons
        for button in [continue_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

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

    return True


def game_over_menu(screen, bg):

    menu_running = True

    while menu_running:
        screen.blit(bg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        game_over_text = get_font(100).render("YOU LOST", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, 100))

        main_menu_button = Button(
            image=pygame.image.load('assets/images/quit_button.png'),
            pos=(WINDOW_WIDTH // 2, 250),
            text_input="MAIN MENU",
            font=get_font(50),
            base_color=(255, 255, 255),
            hovering_color="White"
        )

        quit_button = Button(
            image=pygame.image.load('assets/images/quit_button.png'),
            pos=(WINDOW_WIDTH // 2, 400),
            text_input="QUIT",
            font=get_font(50),
            base_color=(255, 255, 255),
            hovering_color="White"
        )

        screen.blit(game_over_text, game_over_rect)

        for button in [main_menu_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.checkForInput(mouse_pos):
                    main()  # Restart the game loop
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()


def you_win_menu(screen, bg):
    menu_running = True

    while menu_running:
        screen.blit(bg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        won_text = get_font(80).render("YOU WIN!", True, (255, 255, 255))
        won_rect = won_text.get_rect(center=(WINDOW_WIDTH // 2, 100))

        restart_button = Button(
            image=pygame.image.load('assets/images/quit_button.png'),
            pos=(WINDOW_WIDTH // 2, 250),
            text_input="RESTART",
            font=get_font(50),
            base_color=(255, 255, 255),
            hovering_color="White"
        )

        quit_button = Button(
            image=pygame.image.load('assets/images/quit_button.png'),
            pos=(WINDOW_WIDTH // 2, 400),
            text_input="QUIT",
            font=get_font(50),
            base_color=(255, 255, 255),
            hovering_color="White"
        )

        screen.blit(won_text, won_rect)

        # Update and draw buttons
        for button in [restart_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.checkForInput(mouse_pos):
                    main()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()
    return False
