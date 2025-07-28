import pygame

class Card():
    def __init__(self,image, id):
        self.original_image = image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        self.id = id

    def repositionate(self,x,y):
        self.rect.center = (x,y)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.original_image, angle)

    def draw(self,screen):
        screen.blit(self.image, self.rect)