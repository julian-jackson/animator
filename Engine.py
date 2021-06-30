import pygame, math

pygame.init()

class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def preview_render(self, objects):
        surface = pygame.Surface((self.width, self.height))
        surface.fill((0, 0, 0))

        for item in objects:
            pygame.draw.rect(surface, (255,255,0), (item["x"], item["y"], item["width"], item["height"]))

        return surface

    def render(self, animation_length, frame, objects):
        surface = pygame.Surface((self.width, self.height))
        surface.fill((0, 0, 0))
        frame_x_change = []
        frame_y_change = []

        for j, item in enumerate(objects):
            frame_x_change.append((item["magnitude"] * math.cos(math.radians(item["angle"]))) / animation_length)
            frame_y_change.append((item["magnitude"] * math.sin(math.radians(item["angle"]))) / animation_length)

        for x in range(animation_length):
            for i, item in enumerate(objects):
                delta_x = 0
                delta_y = 0
                for y in range(frame):
                    delta_x += frame_x_change[i]
                    delta_y += frame_y_change[i]

                pygame.draw.rect(surface, (255,255,0), (item["x"] + delta_x, item["y"] + delta_y, item["width"], item["height"]))
            return surface
