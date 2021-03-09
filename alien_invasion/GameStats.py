import pygame

class GameStats:

    def __init__(self, ai_game):
        self.setting = ai_game.setting
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.setting.ship_limit