import pgzrun
import random
import math

# ----- MAIN SETTINGS -----
WIDTH = 800
HEIGHT = 600

# ----- GAME STATE -----
game_state = "menu"  # could be: menu, gameplay or game_over

# ----- GAME SOUND SETTINGS -----
sound_enabled = True
current_music = None
music.set_volume(0.5)

# ----- MENU ACTORS -----
title = Actor('game-title')
title.pos = 400, 100

btn_play = Actor('ui_play')
btn_play.pos = 400, 250

btn_musicOn = Actor('ui_music_and_sounds')
btn_musicOn.pos = 400, 330

btn_exit = Actor('ui_exit')
btn_exit.pos = 400, 400

# ----- GAMEPLAY ACTORS -----
alien = Actor('character_green_idle')

# ----- MUSIC CONTROLLER -----
def play_music(track_name):
    global current_music
    if not sound_enabled:
        music.stop()
        current_music = None
        return
    if current_music != track_name:
        music.stop()
        music.play(track_name)
        music.set_volume(0.5)
        current_music = track_name

# ----- MOUSE EVENTS -----
def on_mouse_down(pos):
    global game_state, sound_enabled

    if game_state == 'menu':
        if btn_play.collidepoint(pos):
            print("Começando o jogo...")
            game_state = 'gameplay'

        elif btn_musicOn.collidepoint(pos):
            sound_enabled = not sound_enabled
            print('Music ON' if sound_enabled else 'Music OFF')
            # Atualiza música baseada no estado atual do jogo
            if game_state == 'menu':
                play_music('music_menu')
            elif game_state == 'gameplay':
                play_music('music_level1')
            elif game_state == 'game_over':
                play_music('music_ending')

        elif btn_exit.collidepoint(pos):
            print('Fechando o jogo ---- XD')
            exit()

# ----- KEYBOARD EVENTS -----
def on_key_down(key):
    global game_state
    if game_state == 'gameplay' and key == keys.ESCAPE:
        print("Voltando ao menu...")
        game_state = 'menu'

# ----- DRAW's -----
def draw_menu():
    screen.clear()
    title.draw()
    btn_play.draw()
    btn_musicOn.draw()
    btn_exit.draw()

def draw_gameplay():
    screen.clear()
    

def draw():
    draw_menu()
    
# ----- UPDATE LOOP -----
def update():
    if game_state == 'menu':
        play_music('music_menu')
        draw_menu()
    elif game_state == 'gameplay':
        play_music('music_level1')
        draw_gameplay()
    elif game_state == 'game_over':
        play_music('music_ending')

pgzrun.go()