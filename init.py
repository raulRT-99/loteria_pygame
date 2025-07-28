import pygame
import os
import constants as cons
from ui import Interfaz

pygame.init()

def resize(image,scale):
    new_image = pygame.transform.scale(image,(image.get_width()//scale,image.get_height()//scale))
    return new_image

def resize_custom(image, width, hieght):
    new_image = pygame.transform.scale(image,(width,hieght))
    return new_image

#---LOAD IMAGES
bg_menu = resize_custom(pygame.image.load('assets/fondo.jpg'), cons.WIDTH, cons.HEIGHT)

shown_cards = {str(i+1):resize_custom(pygame.image.load(f'assets/cards/carta ({i+1}).jpg'), 145,205) for i in range(cons.TOTAL_CARDS)}
player_cards = {str(i+1):resize_custom(pygame.image.load(f'assets/cards/carta ({i+1}).jpg'), 65,91) for i in range(cons.TOTAL_CARDS)}
enemy_cards = {str(i+1):resize_custom(pygame.image.load(f'assets/cards/carta ({i+1}).jpg'), 33,46) for i in range(cons.TOTAL_CARDS)}
anverso = resize_custom(pygame.image.load('assets/cards/anverso.png'), 145, 205)
tables_directory = 'assets/tables'
content = os.listdir(tables_directory)
tables = {str(i[0:-4]):resize_custom(pygame.image.load(f'assets/tables/{i}'), cons.WIDTH, cons.HEIGHT) for i in content}
cuenta_player = resize(pygame.image.load('assets/cuenta.png'),8)
cuenta_enemie = resize(pygame.image.load('assets/cuenta.png'),13)

new_card = []
win = 0
run = True
start = False
pause = False
game_over = False

players = 3
table_color = 'Azul'
time_cards = 1500

#---TEXT MENU
main_menu_texts = ['Iniciar', 'Opciones', 'Salir']
options_menu_texts = ['Numero de jugadores', 'Color de la mesa', 'Tiempo entre cartas', 'Regresar']
options_players_texts = [str(i) for i in cons.NUM_PLAYERS]
options_table_color_texts = [i for i in cons.TABLE.keys()]
options_time_texts = [str(i/1000) + " seg." for i in cons.TIME_GET_CARD]
options_difficulty_texts = ["Oponentes: "+i for i in cons.DIFFICULTY.keys()]

pause_texts = ['Continuar','Menu prinicpal','Salir']
game_over_texts = ['Menu principal', 'Salir']

clock = pygame.time.Clock()

main_menu_ui=options_player_ui=options_table_ui=options_time_ui=pause_ui=game_over_ui=None
menus = []
sub_menus = []
shown_menu = []
screen = pygame.display.set_mode((cons.WIDTH, cons.HEIGHT))

def main_screen():
    main_menu_ui = Interfaz(cons.WIDTH // 2, cons.HEIGHT // 3, main_menu_texts, cons.WHITE, screen,
                            'menu')
    options_ui = Interfaz(30, cons.HEIGHT//5,options_menu_texts, cons.BLACK, screen, 'options')
    options_player_ui = Interfaz(155, cons.HEIGHT//4 + 10,options_players_texts, cons.BLACK, screen, 'choice')
    options_table_ui = Interfaz(455, cons.HEIGHT//4 + 10,options_table_color_texts, cons.BLACK, screen, 'choice')
    options_time_ui = Interfaz(755, cons.HEIGHT//4 + 10,options_time_texts, cons.BLACK, screen, 'choice')
    options_difficulty_ui = Interfaz(1055, cons.HEIGHT // 4 + 10, options_difficulty_texts, cons.BLACK, screen, 'choice')
    menus.clear()
    menus.append(main_menu_ui)
    sub_menus.clear()
    sub_menus.extend([options_ui,options_player_ui,options_table_ui,options_time_ui,options_difficulty_ui])
    for menu in menus:
        menu.create()
    for menu in sub_menus:
        menu.create()
    shown_menu.clear()
    shown_menu.append(menus)
    shown_menu.append(sub_menus)
    bg_main = bg_menu
    return bg_main

texts_selected = [None,None,None,None]
default = [True, True, True, True]
game_config = {}
def game_screen():
    pause_ui = Interfaz(cons.WIDTH//2, cons.HEIGHT//2,pause_texts, cons.WHITE, screen, 'menu')
    game_over_ui = Interfaz(cons.WIDTH//2, cons.HEIGHT//2,game_over_texts, cons.WHITE, screen, 'menu')
    pause_ui.create()
    game_over_ui.create()
    shown_menu.clear()
    shown_menu.extend([pause_ui, game_over_ui])
    bg_game = tables[game_config['table']]
    return bg_game

background = main_screen()
selected_menu = 0
for config in cons.DEFAULT_VALUES.keys():
    game_config[config] = cons.DEFAULT_VALUES[config][1]

def winner_msg(winner):
    winner_ui = Interfaz(cons.WIDTH//2, cons.HEIGHT//2,[f'Jugador {winner}:  !!!LOTERIA!!!'], cons.GOLD, screen, 'win')
    winner_ui.create()
    shown_menu.append(winner_ui)

def set_config():
    global texts_selected, game_config
    for x,text in enumerate(texts_selected):
        if text:
            if x == 0:
                game_config['players'] = int(text)
            elif x == 1:
                for color in cons.TABLE.keys():
                    if color == text:
                        game_config['table'] = cons.TABLE[color]
                        break
            elif x ==2:
                number = int(float(text[0:2].strip())*1000)
                if number in cons.TIME_GET_CARD:
                    game_config['time'] = number
            else:
                if text[11:] in cons.DIFFICULTY.keys():
                    game_config['difficulty'] = cons.DIFFICULTY[text[11:]]
