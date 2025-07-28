
import constants as cons

class CardBoard():
    def __init__(self, player, cards, num_players):
        self.cards = cards
        self.player = player
        self.right = True if self.player%2==0 else False
        self.num_players = num_players
        self.matrix = [[None for _ in range(cons.BOARD)] for _ in range(cons.BOARD)]
        count = 0
        for i in range(cons.BOARD):
            for j in range(cons.BOARD):
                self.matrix[i][j] = self.cards[count]
                count += 1

    def create(self):
        def get_coords_and_angle(num_players, player):
            if player == 1:
                # Parámetros para jugador 1
                return (60, 91, cons.WIDTH // 2 - 100, cons.HEIGHT // 2 + 15, 0)
            elif num_players <= 3:
                coordY = ((cons.HEIGHT - 100) // 4) + 100
                if player == 2:
                    return (46, 30, cons.WIDTH-190, coordY, 90)
                elif player == 3:
                    return (46, 30, 40, coordY, 270)
            else:
                # Más de 3 jugadores
                if player in (2, 3):
                    coordY = ((cons.HEIGHT - 100) // 6) + 50
                else:
                    coordY = ((cons.HEIGHT - 100) // 2) + 100

                if player == 2:
                    return (46, 31, cons.WIDTH -190, coordY, 90)
                elif player == 3:
                    return (46, 31, 40, coordY, 270)
                elif player == 4:
                    return (46, 31, cons.WIDTH -190, coordY, 90)
                elif player == 5:
                    return (46, 31, 40, coordY, 270)

            # Valor por defecto (opcional)
            return (0, 0, 0, 0, 0)

        step_x, step_y, base_x, base_y, angle = get_coords_and_angle(self.num_players, self.player)

        for i in range(cons.BOARD):
            for j in range(cons.BOARD):
                # Aplicar rotación sólo si no es 0 (jugador 1 no rota)
                if angle != 0:
                    self.matrix[i][j].rotate(angle)
                self.matrix[i][j].repositionate(j * step_x + base_x, i * step_y + base_y)



