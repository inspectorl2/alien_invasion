class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 0.5
        self.bullet_width = 2
        self.bullet_height = 12
        self.bullet_color = 220, 20, 60
        self.bullet_allowed = 10
