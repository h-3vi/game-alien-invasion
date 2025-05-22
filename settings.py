class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed_factor = 10
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed_factor = 1000
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (21,71,52)
        self.bullets_allowed = 100

        # Настройки пришельцев
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 20
        self.fleet_direction = 1  # 1 для движения вправо, -1 для движения влево

        # Темп ускорения игры
        self.speedup_scale = 1.5

        # Подсчет очков
        self.alien_points = 1000

        # Инициализация динамических настроек
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
