class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """ Initialize the games static settings """
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Ship settings
        self.ship_limit = 3
        #Alien Settings.
        self.fleet_drop_speed = 10
        # How quickly the game speeds up.
        self.speedup_scale = 2
        self.initialize_dynamic_settings()        

    def initialize_dynamic_settings(self):
        """ Initialize settings that chnage throughout the game """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """ Increase speed settings """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

    
        
