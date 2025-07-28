
from init import *
from cards import Card
from card_board import CardBoard
import random as ran
from game_deck import Deck
from character import Character

enemies_characters= []
player_character = None
#---CREATE OBJETCS
def create_boards():
    global deck_cards, tablero1_cards, tableroN_cards, tablero1, boardgame1, enemy_boardgames, enemies_characters, player_character

    enemies_characters.clear()
    deck_cards = []
    deck_cards.clear()
    tablero1_cards = []
    tablero1_cards.clear()
    tableroN_cards = []
    tableroN_cards.clear()
    for x in range(cons.TOTAL_CARDS):
        deck_cards.append(Card(shown_cards[str(x+1)],x+1))
    for x in range(cons.TOTAL_CARDS):
        tablero1_cards.append(Card(player_cards[str(x+1)], x+1))

    ran.shuffle(tablero1_cards)
    tablero1 = []
    tablero1.clear()
    for i in range(16):
        tablero1.append(tablero1_cards.pop(ran.randint(0,len(tablero1_cards)-1)))
    boardgame1 = None
    boardgame1 = CardBoard(1, tablero1, game_config['players'])
    boardgame1.create()
    player_character = None
    player_character = Character(boardgame1, 1, cuenta_player)

    enemy_boardgames = []
    enemy_boardgames.clear()
    for p in range(game_config['players']-1):
        tableroN = []
        for x in range(cons.TOTAL_CARDS):
            tableroN.append(Card(enemy_cards[str(x+1)], x+1))
        ran.shuffle(tableroN)
        for i in range(16):
            tableroN.append(tableroN.pop(ran.randint(0,len(tableroN)-1)))
        boardgame = CardBoard(p+2, tableroN, game_config['players'])
        boardgame.create()
        enemy_boardgames.append(boardgame)

    for x, enemie_board in enumerate(enemy_boardgames, 2):
        enemie_character = Character(enemie_board, x, cuenta_enemie, game_config['time'], game_config['difficulty'])
        enemies_characters.append(enemie_character)


anverso_cards = []
anverso_total = [44,34,24,14]
#---CREATE DECK
def create_deck():
    global game_deck, anverso_cards, shown_deck_card, last_shown_card
    shown_deck_card = None
    last_shown_card = pygame.time.get_ticks()
    anverso_cards.clear()
    game_deck = []
    game_deck.clear()
    for x in range(cons.TOTAL_CARDS):
        game_deck.append(Card(shown_cards[str(x+1)],x+1))
    game_deck = Deck(game_deck)
    game_deck.shuffle_deck()
    for i in range(5):
        anverso_card = Card(anverso, 0)
        x = cons.WIDTH // 2 - anverso_card.image.get_width() + i*3
        y = cons.HEIGHT // 2 - anverso_card.image.get_height() - 25 +i*3
        anverso_card.repositionate(x,y)
        anverso_cards.append(anverso_card)

first_card = True
shown_deck_card = None
last_shown_card = pygame.time.get_ticks()
in_game = False
def main_menu_events():
    global selected_menu, run, default, start, in_game, new_card, pause, game_over

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #---MAIN MENU
        if selected_menu == 0 and event.type == pygame.MOUSEBUTTONDOWN:
            for idx, button in enumerate(shown_menu[selected_menu][0].buttons):
                if button.collidepoint(event.pos):
                    if shown_menu[selected_menu][0].texts[idx] == 'Iniciar':
                        start = True
                        create_boards()
                        create_deck()
                        in_game = True
                        pause = False
                        game_over = False
                        new_card = [True for i in range(len(enemies_characters)+1)]
                    elif shown_menu[selected_menu][0].texts[idx] == 'Opciones':
                        selected_menu = 1
                    elif shown_menu[selected_menu][0].texts[idx] == 'Salir':
                        run = False
        #---OPTIONS MENU
        elif selected_menu == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            #--NUMBER OF PLAYERS
            for idx, button in enumerate(shown_menu[selected_menu][1].buttons):
                if button.collidepoint(event.pos):
                    selected_text = shown_menu[selected_menu][1].texts[idx]
                    if selected_text in str(cons.NUM_PLAYERS):
                        texts_selected[0] = selected_text
                        default[0] = False
            #--TABLE COLOR
            for idx, button in enumerate(shown_menu[selected_menu][2].buttons):
                if button.collidepoint(event.pos):
                    selected_text = shown_menu[selected_menu][2].texts[idx]
                    if selected_text in str(cons.TABLE.keys()):
                        texts_selected[1] = selected_text
                        default[1] = False
            #--TIME BETWEEN CARDS
            for idx, button in enumerate(shown_menu[selected_menu][3].buttons):
                if button.collidepoint(event.pos):
                    selected_text = shown_menu[selected_menu][3].texts[idx]
                    if selected_text in [str(pos/1000) + " seg." for pos in cons.TIME_GET_CARD]:
                        texts_selected[2] = selected_text
                        default[2] = False
            #--DIFFICULTY
            for idx, button in enumerate(shown_menu[selected_menu][4].buttons):
                if button.collidepoint(event.pos):
                    selected_text = shown_menu[selected_menu][4].texts[idx]
                    if selected_text[11:] in cons.DIFFICULTY.keys():
                        texts_selected[3] = selected_text
                        default[3] = False
            #--GO BACK MENU
            for idx, button in enumerate(shown_menu[selected_menu][0].buttons):
                if button.collidepoint(event.pos):
                    if shown_menu[selected_menu][0].texts[idx] == 'Regresar':
                        selected_menu = 0

            set_config()

def pause_events():
    global run, start, in_game, pause, game_over, background, selected_menu, win
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx, button in enumerate(shown_menu[0].buttons):
                if button.collidepoint(event.pos):
                    if shown_menu[0].texts[idx] == 'Continuar':
                        pause = False
                        break
                    elif shown_menu[0].texts[idx] == 'Menu prinicpal':
                        start = False
                        in_game = False
                        pause = False
                        game_over = False
                        background = main_screen()
                        selected_menu = 0
                        win = 0
                        break
                    elif shown_menu[0].texts[idx] == 'Salir':
                        run = False
                        break

def game_over_events():
    global run, start, in_game, pause, game_over, background, selected_menu, win
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx, button in enumerate(shown_menu[1].buttons):
                if button.collidepoint(event.pos):
                    if shown_menu[1].texts[idx] == 'Menu principal':
                        start = False
                        in_game = False
                        pause = False
                        game_over = False
                        background = main_screen()
                        selected_menu = 0
                        win = 0
                        break
                    elif shown_menu[1].texts[idx] == 'Salir':
                        run = False
                        break

while run:
    clock.tick(cons.FPS)
    screen.blit(background,(0,0))
    current_time = pygame.time.get_ticks()
    if in_game:
        background = game_screen()
        in_game = False

    if not start:
        for menu in shown_menu[selected_menu]:
            menu.draw(texts_selected, default)
        main_menu_events()
        last_shown_card = pygame.time.get_ticks()
    else:
        #---START GAME
        if not pause and not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for row in boardgame1.matrix:
                            for tarjeta in row:
                                if tarjeta.rect.collidepoint(event.pos) and not new_card[0]:
                                    new_card[0] = player_character.mark_board(shown_deck_card, last_shown_card, tarjeta)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = True

            if len(game_deck.cards) > 0:
                for x in anverso_cards:
                    x.draw(screen)
                    pygame.draw.rect(screen, (30, 30, 100), x.rect, 1)
                    if len(game_deck.cards) in anverso_total:
                        anverso_cards.remove(x)
                        anverso_total.pop(0)
                if first_card and current_time>= last_shown_card+3000:
                    shown_deck_card = game_deck.get_card()
                    last_shown_card = current_time
                    first_card = False
                elif not first_card and current_time - last_shown_card >= game_config['time']:
                    last_shown_card = current_time
                    shown_deck_card = game_deck.get_card()
                    new_card = [False for i in range(len(enemies_characters)+1)]
            else:
                game_over = True

            game_deck.draw_card(shown_deck_card, screen)

            for tarjeta in boardgame1.matrix:
                for i in tarjeta:
                    i.draw(screen)
            for board in enemy_boardgames:
                for tarjeta in board.matrix:
                    for i in tarjeta:
                        i.draw(screen)

            player_character.draw_cuentas(screen)
            #---AI
            for x, enemie in enumerate(enemies_characters,1):
                if not new_card[x]:
                    new_card[x] = enemie.mark_board(shown_deck_card, last_shown_card)
                enemie.draw_cuentas(screen)

            if player_character.win:
                win = player_character.player
            else:
                for enemie in enemies_characters:
                    if enemie.win:
                        win = enemie.player

            if win>0:
                game_over = True
                winner_msg(win)
        #---PAUSE GAME
        elif not game_over and pause:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = False

            for x in anverso_cards:
                x.draw(screen)
                pygame.draw.rect(screen, (30, 30, 100), x.rect, 1)
            game_deck.draw_card(shown_deck_card, screen)

            for tarjeta in boardgame1.matrix:
                for i in tarjeta:
                    i.draw(screen)
            for board in enemy_boardgames:
                for tarjeta in board.matrix:
                    for i in tarjeta:
                        i.draw(screen)

            player_character.draw_cuentas(screen)
            #---AI
            for enemie in enemies_characters:
                enemie.draw_cuentas(screen)

            shown_menu[0].draw(texts_selected, default, True)
            pause_events()
        #---GAME OVER
        elif game_over and not pause:
            for x in anverso_cards:
                x.draw(screen)
                pygame.draw.rect(screen, (30, 30, 100), x.rect, 1)
            game_deck.draw_card(shown_deck_card, screen)

            for tarjeta in boardgame1.matrix:
                for i in tarjeta:
                    i.draw(screen)
            for board in enemy_boardgames:
                for tarjeta in board.matrix:
                    for i in tarjeta:
                        i.draw(screen)

            player_character.draw_cuentas(screen)
            # ---AI
            for enemie in enemies_characters:
                enemie.draw_cuentas(screen)

            shown_menu[1].draw(texts_selected, default, True)
            if win >0:
                shown_menu[2].draw(texts_selected, default)
            game_over_events()


    pygame.display.update()









