import pygame

class TextBox:
    def __init__(self, x = 0, y= 0, font_size = 64, font_colour = (0, 0, 0), text="Placeholder"):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.font_colour = font_colour
    def draw(self, win):
        my_surface = pygame.font.Font(None, self.font_size).render(self.text, True, self.font_colour)
        win.blit(my_surface, (self.x, self.y))

class Background:
    def __init__(self, colour=(255, 255, 255)):
        self.colour = colour

    def draw(self, win):
        win.fill(self.colour) 

class Panel:
    def __init__(self, x=0, y=0, width=64, height=64, colour=(200, 200, 200)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))     

class InputBox:
    def __init__(self, x=0, y=0, width=100, height=50, passive_colour=(150,150,150), active_colour=(46, 140, 255), default_text="", start_active=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.passive_colour = passive_colour
        self.active_colour =  active_colour
        
        self.box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = default_text
        self.active = start_active

        self.entered = False
        self.char_limit = round(self.width / 18)

        self.colour = self.passive_colour
        self.font = pygame.font.Font(None, 48)

    def keydown_update(self, event):
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_ESCAPE:
                self.active = False
            elif event.key == pygame.K_e and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                self.text = ""
            else:
                if len(self.text) < self.char_limit and event.key != pygame.K_RETURN:
                    self.text += event.unicode 
        
            if event.key == pygame.K_RETURN:
                self.entered = True
            else:
                self.entered = False

            return [self.entered, self.text]

    def draw(self, win):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()

        if click[0]:
            if self.box.collidepoint(mouse):
                self.active = True
            else:
                self.active = False

        if self.active:
            self.colour = self.active_colour
        else:
            self.colour = self.passive_colour

        pygame.draw.rect(win, self.colour, self.box, 4, 5)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        win.blit(text_surface, (self.x + 7, self.y + 7))

class Button:
    def __init__(self, x=0, y=0, width=64, height=64, passive_colour=(255, 255, 255), active_colour=(0, 0, 0), font_size=32, active_font=(255, 255, 255), passive_font=(0, 0, 0), border_width=10, icon_type="Text", icon="Demo", item_id="default"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.passive_colour = passive_colour
        self.active_colour = active_colour
        self.colour = passive_colour
        self.border_width = border_width

        self.font_size = font_size
        self.active_font = active_font
        self.passive_font = passive_font
        self.font_colour = passive_font
        self.font = pygame.font.Font(None, self.font_size)

        self.icon_type = icon_type
        self.icon = icon
        self.item_id = item_id
        self.active = False

        text_surface = self.font.render(self.icon, True, self.font_colour)
        text_surface_rect = pygame.Surface(text_surface.get_size())
        self.rect = pygame.Rect(self.x, self.y, text_surface_rect.get_width(), text_surface_rect.get_height())

    def draw(self, win):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse):
            self.active = True
        else:
            self.active = False

        if click[0] and self.rect.collidepoint(mouse):
            return self.item_id

        if self.active:
            self.colour = self.active_colour
            self.font_colour = self.active_font
        else:
            self.colour = self.passive_colour
            self.font_colour = self.passive_font

        text_surface = self.font.render(self.icon, True, self.font_colour)

        text_surface_rect = pygame.Surface(text_surface.get_size())
        text_surface_rect.fill(self.colour)
        text_surface_rect.blit(text_surface, (0, 0))
        win.blit(text_surface_rect, (self.x, self.y))