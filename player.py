import pygame
class Player_object():
    def __init__(self,screen):
        self.screen = screen
        self.player = pygame.image.load('images/spaceship.png')
        self.player_scaled = pygame.transform.scale(self.player, (150, 100))
        self.rect = self.player_scaled.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.top = 220
        self.rect.left = 40
        self.moving_top = False
        self.moving_bottom = False
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        self.screen.blit(self.player_scaled, self.rect)

    def update(self):
        if self.moving_top and self.rect.top >= 30:
            self.rect.top -= 5
        if self.moving_bottom and self.rect.top <= 420:
            self.rect.top += 5
        if self.moving_left and self.rect.left >= 30:
            self.rect.left -= 5
        if self.moving_right and self.rect.left <= 550:
            self.rect.left += 5