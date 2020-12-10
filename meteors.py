import pygame
class Meteor():
    def __init__(self,screen):
        self.screen = screen
        self.meteor = pygame.image.load('images/meteor.png')
        self.meteor_scaled = pygame.transform.scale(self.meteor, (150, 50))
        self.rect = self.meteor_scaled.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = 1100
        self.rect.bottom = 100
        self.step = 0

    def update_position(self,update,position_update,screen_out=0):
        if screen_out > 0:
            self.rect.bottom = 50 + position_update
        else:
            self.rect.bottom = update + 150

    def blitme(self):
        self.screen.blit(self.meteor_scaled, self.rect)