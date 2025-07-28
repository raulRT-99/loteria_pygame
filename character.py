import random as ran
import pygame
import constants as cons


class Cuenta:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Character:
    def __init__(self, card_board, player, image, time_config=0, difficulty = 1):
        self.card_board = card_board
        self.image = image
        self.cuentas = []
        self.total = 0
        self.player = player
        self.win = False
        self.difficulty = difficulty
        self.time_config = time_config
        self.difficulty_time = 300 + self.difficulty
        self.difficulty_miss = self.difficulty/550

    def mark_board(self, card, shown_card_time, selectd_card=None):
        if card:
            if self.player == 1 and selectd_card:
                if selectd_card.id == card.id:
                    cuenta = Cuenta(self.image)
                    cuenta.rect.center = (selectd_card.rect.centerx, selectd_card.rect.centery)
                    self.cuentas.append(cuenta)
                    self.total += 1
                    if self.total >= cons.WIN_BOARD:
                        self.win = True
                    return True
            else:
                current_time = pygame.time.get_ticks()
                missed_oportunity = ran.random()
                try_mark = missed_oportunity > self.difficulty_miss
                if current_time - (shown_card_time+self.difficulty_time) >= 1 and try_mark:
                    missed_oportunity = ran.random()
                    try_mark = missed_oportunity > self.difficulty_miss
                    for row in self.card_board.matrix:
                        for tarjeta in row:
                            if tarjeta.id == card.id and try_mark:
                                cuenta = Cuenta(self.image)
                                cuenta.rect.center = (tarjeta.rect.centerx+8, tarjeta.rect.centery-8)
                                self.cuentas.append(cuenta)
                                self.total += 1
                                if self.total >= cons.WIN_BOARD:
                                    self.win = True
                                return True
            return False

    def draw_cuentas(self, screen):
        for cuenta in self.cuentas:
            cuenta.draw(screen)
