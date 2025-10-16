import pygame, sys
from settings import Settings
from ship import Ship

class Alieninvasion():
    ### Overall class to manage game assets and behavior
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        ### watch keyboard & mouse movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ### Checks for events 
                sys.exit()
            elif event.type == pygame.KEYDOWN: ### checks for keyboard events such as a key being pressed
                if event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False 
                

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    ai = Alieninvasion()
    ai.run_game()