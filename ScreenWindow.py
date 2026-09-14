
import pygame
import project_style as style

# Sizes (800, 600) , (1920, 1080) , (1490, 914), (2560, 1440)

class ScreenWindow:
    def __init__(self):
        self.running = False
        self.size = (style.WIDTH, style.HEIGHT)
        self.width = self.size[0]
        self.height = self.size[1]

        self.pygame_version = pygame.version.ver

        self.screen = None
        self.mouse_dragging = False
        self.strip_height = style.tool_strip_height

        self.project_name = ""
        self.sheet_name = ""

        self.toolstrip_box = None
        self.tool_strip_colour = style.SKY_AZURE



    def start_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self.running = True

        # Initiate additional pygame objects
        self.font_big_italic = pygame.font.SysFont(None, 50, italic=True)
        self.font_bold = pygame.font.SysFont(None, 20, bold=True)


    def set_size(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)

    def draw_toolstrip(self):
        self.toolstrip_box = pygame.Rect(0, self.height-self.strip_height-10, self.width, self.strip_height+10)
        pygame.draw.rect(self.screen, self.tool_strip_colour, self.toolstrip_box)

        self.toolstrip_back = pygame.Rect(0, self.height - self.strip_height, self.width, self.strip_height)
        pygame.draw.rect(self.screen, style.DARK_GREY, self.toolstrip_back)

        # Draw window text
        main_text = self.font_big_italic.render("SeraphNote", True, (255 - 7, 255 - 7, 255 - 7))
        main_text_rect = main_text.get_rect()
        main_text_rect.center = (self.width-185, self.height-40)
        self.screen.blit(main_text, main_text_rect)

        slogan_text = self.font_bold.render("Connecting Facts to Thoughts", True, self.tool_strip_colour)
        slogan_text_rect = slogan_text.get_rect()
        slogan_text_rect.center = (self.width-155, self.height-14)
        self.screen.blit(slogan_text, slogan_text_rect)




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

            self.draw_screen()

            for event in pygame.event.get():
                # Detect if window is being closed
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.VIDEORESIZE:
                    # Check if changed to full screen
                    if pygame.display.get_surface().get_flags() & pygame.FULLSCREEN:
                        # Change screensize (get from resizable winodw)
                        #self.size = (event.w, event.h)
                        #self.size = pygame.display.get_window_size()
                        #self.width = self.size[0]
                        #self.height = self.size[1]
                        self.size = self.screen.get_size()
                        self.width, self.height = self.screen.get_size() #pygame.display.get_window_size()
                        self.draw_screen()
                        print(self.size)
                        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
                        #screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                        #self.size = self.screen.get_size()
                    else:
                        #self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
                        # Reset screen size to stylesheet default
                        # self.size = (style.WIDTH, style.HEIGHT)
                        # self.width = self.size[0]
                        # self.height = self.size[1]
                        self.size = self.screen.get_size()
                        self.width, self.height = self.screen.get_size()  # pygame.display.get_window_size()
                        self.draw_screen()
                        print(self.size)
                        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
                        #screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

                # Check if mouse actions
                self.check_mouse_input(event)

        # Close when loop broken
        pygame.quit()


    def draw_screen(self):
        pygame.display.set_caption(f"SeraphNote: {self.project_name} - {self.sheet_name}")
        self.screen.fill(style.CALM_AZURE)

        self.draw_toolstrip()


        # Refresh screen
        pygame.display.flip()