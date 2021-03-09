import sys
from time import sleep
import pygame

from setting import Setting
from GameStats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.setting = Setting()
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        

        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()
        self.stats = GameStats(self)

        self.play_button = Button()
        self._create_fleet()
        self.game_active = True


    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_alien()
            
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key ==pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key ==pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        if len(self.bullet)< self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)
    
    def _update_bullet(self):
        self.bullet.update()
        for bullet in self.bullet.copy():
            if bullet.rect.bottom<=0:
                self.bullet.remove(bullet)
            self._check_alien_bullet_collisions()


    def _check_alien_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullet, self.alien, True, True)
        if not self.alien:
            self.bullet.empty()
            self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.setting.screen_width - (2*alien_width)
        number_of_aliens_x = available_space_x//(2*alien_width)
        
        ship_height =self.ship.rect.height
        available_space_y =(self.setting.screen_height-(3*alien_height)-ship_height)
        rowNum = available_space_y//(2*alien_height)
        for rowNum in range(rowNum):
            for aliens_num in range(number_of_aliens_x):
                self._create_aliens(aliens_num, rowNum)


    def _create_aliens(self, alien_nums, rowNum):
            alien = Alien(self)
            alien_width, alien_height =alien.rect.size
            alien.x = alien_width+2*alien_width*alien_nums
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2*alien.rect.height*rowNum
            self.alien.add(alien)

    def _update_alien(self):
        self._check_fleet_edges()
        self.alien.update()
        if pygame.sprite.spritecollideany(self.ship, self.alien):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.alien.sprites():
            if alien.check_edges():
                self._change_fleet_dir()
                break

    def _change_fleet_dir(self):
        for alien in self.alien.sprites():
            alien.rect.y += self.setting.fleet_drpSpd
        self.setting.fleet_dir *= -1

    def _ship_hit(self):
        if self.stats.ship_left >0:
            self.stats.ship_left -=1

            self.alien.empty()
            self.bullet.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.alien.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color) 
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

