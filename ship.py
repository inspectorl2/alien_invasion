import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Каждый новый корабль появляется у нижнего края экрана
        self.center = float(self.rect.centerx)

    def update(self):
        """Обновляет позицию коробля c учетом флагов."""
        # Обновляет атрибут center, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center
        # elif self.moving_up:
        #    self.rect.centery -= 1
        # elif self.moving_down:
        #    self.rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
