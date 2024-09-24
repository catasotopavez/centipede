import pygame

# Inicializar pygame mixer
pygame.mixer.init()

# Cargar sonidos
block_destroyed_sound = pygame.mixer.Sound('sounds/block_destroyed_sound.wav')
shoot_sound = pygame.mixer.Sound('sounds/shoot.mp3')
lose_music = pygame.mixer.Sound('assets/music/lose-music.mp3')
victory_music = pygame.mixer.Sound('assets/music/victory-music.mp3')

# Cargar música
menu_music = 'assets/music/menu-music.mp3'
gameplay_music = 'assets/music/gameplay-music.mp3'

# Cuando se destruya un hongo
def mushroom_destroyed():
    block_destroyed_sound.play()

# Cuando se active un powerup
def shooting():
    shoot_sound.play()

# Reproducir música de fondo
def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)  # -1 para que se repita indefinidamente

# Detener la música
def stop_music():
    pygame.mixer.music.stop()

# Cambiar música según el estado del juego
def start_game():
    play_music(gameplay_music)

def game_over():
    stop_music()
    lose_music.play()

def victory():
    stop_music()
    victory_music.play()

def menu():
    play_music(menu_music)
