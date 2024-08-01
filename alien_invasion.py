import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
# from alien import Alien
import game_functions as gf


def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.
                                      screen_height))
    pygame.display.set_caption("Alien invasion")

    # Запуск основного цикла игры
    ship = Ship(ai_settings, screen)
    # alien = Alien(ai_settings, screen)
    aliens = Group()

    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, aliens)
    # Создание группы для хранения пуль.
    bullets = Group()

    while True:
        # Отслеживание событий клавиатуры и мыши
        screen.fill(ai_settings.bg_color)
        # ship.blitme()
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
