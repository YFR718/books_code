import random
import sys
import time

from settings import Settings
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from buttom import Buttom
from scoreboard import Scoreboard
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.stats = GameStats(self)
        self.scodeboard = Scoreboard(self)
        self.play_button = Buttom(self,"Play")
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()



    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_alien()
                self._create_fleet()
            self.scodeboard.prep_score() #???
            #self.scodeboard.check_high_score()
            self._update_screen()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scodeboard.prep_score()
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.scodeboard.prep_score()
            self.scodeboard.prep_ships()


    def _check_keydown(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction(alien)

    def _check_fleet_direction(self,alien):
        alien.fleet_direction *= -1


    def _check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=screen_rect.bottom:
                self.aliens.remove(alien)
                if self.settings.level>=3:
                    self._ship_hit()
                    self.settings.level = 1


    def _fire_bullet(self):
        if self.settings.bullet_nums > 0:
            self.settings.bullet_nums -= 1
            new_bullt = Bullet(self)
            self.bullets.add(new_bullt)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.scodeboard.show_score()
        #self.scodeboard.check_high_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # crash to move
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            self.stats.score += 1
            self.scodeboard.check_high_score()
            if self.stats.score %10 == 0:
                self.settings.level+=1
        # create alien when no alien
        # if not self.aliens:
        #     # self.bullets.empty()
        #     self._create_fleet()

    def _update_alien(self):
        self._check_fleet_edges()
        self.aliens.update() # ??
        # for alien in self.aliens:
        #     alien.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_alien_bottom()

    def _create_fleet(self):
        if random.random()<0.001:
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.rect.x = random.random()*self.settings.screen_width
            alien.rect.y = alien_height*random.random()
            self.aliens.add(alien)
    def _ship_hit(self):
        if self.stats.ship_left>0:
            self.stats.ship_left -= 1
            # self.aliens.empty()
            # self.bullets.empty()
            self.ship.center_ship()
            self.scodeboard.prep_ships()
            time.sleep(3)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)




if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
