import pygame

FPS = 30


class Game:
    def __init__(self) -> None:
        super().__init__()
        self._running = False
        pygame.init()
        self.size = (640, 480)

        self.screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()
        pass

    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value) -> None:
        self._running = value

    def update(self):
        self.screen.fill((120, 120, 120))
        pass

    def start(self):
        self.running = True
        try:
            while self.running:
                self.clock.tick(FPS)
                self.process_events()
                self.update()

                pygame.display.flip()
        finally:
            pygame.quit()
        pass

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


if __name__ == '__main__':
    game = Game()
    game.start()
