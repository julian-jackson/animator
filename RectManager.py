import pygame, ui

pygame.init()

class Manager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active_x = 0
        self.active_y = 0
        self.editing = False

        self.x_label = ui.InputBox(x=445, y=535, default_text=str(f"X: {self.active_x}"))
        self.y_label = ui.InputBox(x=445, y=580, default_text=str(f"Y: {self.active_y}"))

    def render(self, objects, win, event):
        event_handler = []
        surface = pygame.Surface((self.width, self.height))
        surface.fill((0, 0, 0))
        
        y_offset = 0

        for item in objects:
            object_button = ui.Button(x=10, y=80 + y_offset, font_size=50, item_id=item["id"], active_font=(220, 220, 220), passive_colour=(75, 75, 75), active_colour=(38, 38, 38), icon="+")
            object_label = ui.TextBox(x=45, y=80 + y_offset, font_size=30, font_colour=(30, 30, 30), text=item["id"])

            event_handler.append(object_button.draw(win))
            event_handler.append(object_label.draw(win))

            # for rect in objects:
            #     if rect["id"] in event_handler:
            #         self.active_x = rect["x"]
            #         self.active_y = rect["y"]

            y_offset += 50

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    textbox_handler = []
                    textbox_handler.append(self.x_label.keydown_update(event))
                    textbox_handler.append(self.y_label.keydown_update(event))

            self.x_label.draw(win)
            self.y_label.draw(win)
                