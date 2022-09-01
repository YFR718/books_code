
class Settings:

    def __init__(self):
        # screen
        self.level = 1
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # ship
        self.ship_speed = 1.5
        self.ship_limit = 3
        # bullet
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_nums = 3000
        # alien
        self.alien_speed = 1
        self.fleet_drop_speed = 2

    def increase_speed(self):
        self.ship_speed *= (1.0*self.level-1) / self.level
        self.bullet_speed *= (1.0*self.level-1) / self.level
        self.alien_speed *= self.level/(1.0*self.level-1)
        self.fleet_drop_speed *= self.level/(1.0*self.level-1)


