import pygame

import constants as cons
import random as ran

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle_deck(self):
        ran.shuffle(self.cards)

    def get_card(self):
        card = self.cards.pop(ran.randint(0,len(self.cards)-1))
        return card

    def draw_card(self, card, screen):
        if card:
            x = cons.WIDTH//2 + card.image.get_width()
            y = cons.HEIGHT//2 - card.image.get_height() -25
            card.repositionate(x,y)
            card.draw(screen)
            pygame.draw.rect(screen, (30,30,100), card.rect, 3)