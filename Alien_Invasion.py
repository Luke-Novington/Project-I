import pygame, sys
from settings import Settings
from ship import Ship

class Alieninvasion():
    ### Overall class to manage game assets and behavior
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_width, self.settings.screen_length)
        self.ship = Ship(self)

    def run_game(self):
        while True:
            ### watch keyboard & mouse movements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    ai = Alieninvasion()
    ai.run_game()