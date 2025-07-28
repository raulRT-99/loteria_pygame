import pygame
import constants as cons

class Interfaz():
    def __init__(self,x,y, texts, color, screen, type):
        self.texts = texts
        self.screen =screen
        self.font = pygame.font.Font('assets/Persona Aura.otf', 25)
        self.color = color
        self.buttons = []
        self.render_texts = []
        self.buttons_created = []
        self.x = x
        self.y = y
        self.type = type #menu--options--choice--win

    def render(self):
        for text in self.texts:
            text_render = self.font.render(text, True, self.color if text != 'Regresar' else (220,220,220))
            self.render_texts.append(text_render)

    def create_buttons(self):
        for x, text in enumerate(self.texts):
            button_width = 250 if self.type != 'choice' else 200
            button_height = 40
            spacing = 20 if self.type != 'options' else 50
            if self.type != 'options':
                pos_x = self.x - button_width//2
                pos_y = self.y + x*(button_height + spacing)
                if self.type == 'win':
                    self.font = pygame.font.Font('assets/Persona Aura.otf', 100)
                    button_width = 350
                    button_height = 60
                    pos_x = self.x - button_width // 2
                    pos_y = self.y + x * button_height - 150
            else:
                pos_y = self.y
                pos_x = self.x + x * (button_width + spacing)
            button = pygame.Rect(pos_x, pos_y, button_width if 'Oponentes' not in text else button_width+30, button_height)
            self.buttons.append(button)

    def create(self):
        self.render()
        self.create_buttons()

    #---DRAW SELECTED BUTTON OR DEFAULT BUTTON
    def draw(self, texts_selected, default_values, pause=False):
        for x, button in enumerate(self.buttons):
            pygame.draw.rect(self.screen, cons.BUTTON_COLOR[self.type], button)
            self.screen.blit(self.render_texts[x], (button.x + 15, button.y + 10))
            if pause or self.type == 'win':
                pygame.draw.rect(self.screen, cons.GOLD, button, 3)
            #--NUMBER OF PLAYERS
            if not default_values[0] and self.type == 'choice' and texts_selected[0] == self.texts[x]:
                pygame.draw.rect(self.screen, cons.RED, button, 3)
            elif default_values[0] and self.type == 'choice':
                if cons.DEFAULT_VALUES['players'][0] == self.texts[x]:
                    pygame.draw.rect(self.screen, cons.RED, button, 3)
            #--TABLE COLOR
            if not default_values[1] and self.type == 'choice' and texts_selected[1] == self.texts[x]:
                pygame.draw.rect(self.screen, cons.RED, button, 3)
            elif default_values[1] and self.type == 'choice':
                if cons.DEFAULT_VALUES['table'][0] == self.texts[x]:
                    pygame.draw.rect(self.screen, cons.RED, button, 3)
            #--TIME BETWEEN CARDS
            if not default_values[2] and self.type == 'choice' and texts_selected[2] == self.texts[x]:
                pygame.draw.rect(self.screen, cons.RED, button, 3)
            elif default_values[2] and self.type == 'choice':
                if cons.DEFAULT_VALUES['time'][0] == self.texts[x]:
                    pygame.draw.rect(self.screen, cons.RED, button, 3)
            #--DIFFICULTY
            if not default_values[3] and self.type == 'choice' and texts_selected[3] == self.texts[x]:
                pygame.draw.rect(self.screen, cons.RED, button, 3)
            elif default_values[3] and self.type == 'choice':
                if cons.DEFAULT_VALUES['difficulty'][0] == self.texts[x][11:]:
                    pygame.draw.rect(self.screen, cons.RED, button, 3)
