import pygame
from pygame.sprite import Sprite
 
class Meteor(Sprite):
    """A class to represent a single meteor in the fleet."""

    def __init__(self, ai_game):
        """Initialize the meteor and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the meteor image and set its rect attribute.
        image = pygame.image.load('images/rock.png')
        self.image = pygame.transform.scale(image,(75,75))
        self.rect = self.image.get_rect()

        # Start each new meteor near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the meteor's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if meteor is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the meteor right or left."""
        self.x += (self.settings.meteor_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x
