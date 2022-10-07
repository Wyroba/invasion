class Settings:
    """A class to store all settings for Alient Invasion"""
    def __init__(self):
        """Initialize the games's settings."""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = .25

        # Bullet settings
        self.bullet_speed = .75
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3