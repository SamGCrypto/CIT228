import pygame
class Setting:
    def __init__(self):
        self.screen_width =1200
        self.screen_height = 800
        self.bg_color=(230,230,230)


        #ship related things
        self.ship_spd =1.5
        self.ship_limit = 3

        self.bullet_spd = 1.5
        self.bullet_width =3
        self.bullet_height =15
        self.bullet_color=(60,60,60)
        self.bullet_allowed = 4

        #alien stuff
        self.alien_spd = 0.5
        self.fleet_drpSpd =10
        self.fleet_dir = 1