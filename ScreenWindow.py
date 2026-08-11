
import pygame
import project_style as style

# Sizes (800, 600) , (1920, 1080) , (1490, 914), (2560, 1440)

class ScreenWindow:
    def __init__(self):
        self.running = False
        self.size = (style.WIDTH, style.HEIGHT)

        self.pygame_version = pygame.version.ver

        self.screen = None

    def start_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self.running = True


    def set_size(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)

    def display_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw_screen()

        # Close when loop broken
        pygame.quit()

    def draw_screen(self):
        self.screen.fill(style.CALM_AZURE)
        pygame.display.flip()