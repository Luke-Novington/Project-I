import pygame, sys

class Alieninvasion():
    ### Overall class to manage game assets and behavior
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            ### watch keyboard & mouse movements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    ai = Alieninvasion()
    ai.run_game()