
import pygame
import project_style as style

# Sizes (800, 600) , (1920, 1080) , (1490, 914), (2560, 1440)

class ScreenWindow:
    def __init__(self):
        self.running = False
        self.size = (style.WIDTH, style.HEIGHT)

        self.pygame_version = pygame.version.ver

        self.screen = None
        self.mouse_dragging = False

        self.project_name = ""
        self.sheet_name = ""

    def start_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self.running = True


    def set_size(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)


    def check_mouse_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pass
            if event.button == 2: # Middle mouse button
                pass
            if event.button == 3:  # Right mouse button
                pass

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                pass
            if event.button == 2: # Middle mouse button
                pass
            if event.button == 3:  # Right mouse button
                pass

        if event.type == pygame.MOUSEMOTION:
            if self.mouse_dragging:
                pass


    def display_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw_screen()

            for event in pygame.event.get():
                # Detect if window is being closed
                if event.type == pygame.QUIT:
                    self.running = False

                # Check if mouse actions
                self.check_mouse_input(event)

        # Close when loop broken
        pygame.quit()


    def draw_screen(self):
        pygame.display.set_caption(f"SeraphNote: {self.project_name} - {self.sheet_name}")
        self.screen.fill(style.CALM_AZURE)




        # Refresh screen
        pygame.display.flip()