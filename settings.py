class Settings:
    """A class to store all settings for Alient Invasion"""
    def __init__(self):
        """Initialize the games's settings."""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = .50

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = .25
        self.fleet_drop_speed = 5
        # Fleet_direction of 1 represents right; -1 is left
        self.fleet_direction = 1