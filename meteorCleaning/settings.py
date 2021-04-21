import pygame

class Settings:
    """A class to store all settings for Meteor Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 1000
        self.background_image = pygame.image.load("images/galaxy.jpg")
        self.bg_color=(255,255,255)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.boom = pygame.mixer.Sound("boom.mp3")

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        self.pew = pygame.mixer.Sound("pew.mp3")
        # Meteor settings
        self.meteor_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        self.speedup_scale = 1.1

        self.score_scale = 1.5


        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.meteor_speed = 1.0

        self.fleet_direction = 1

        self.meteor_pts = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.meteor_speed *= self.speedup_scale

        self.meteor_pts = int(self.meteor_pts*self.score_scale)
        
