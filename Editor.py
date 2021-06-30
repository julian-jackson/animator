import pygame, ui, os, pickle
from Engine import Display
from RectManager import Manager

pygame.init()

default_width = 1280
default_height = 720

displayport_x = 350
displayport_y = 75

rect_manager_x = 25
rect_manager_y = 75

run = True
pickle_load = False

main_path = os.path.dirname(os.path.realpath(__file__))

win = pygame.display.set_mode((default_width, default_height))

preview_display = Display(width=900, height=450)
rect_manager = Manager(width=300, height=650)

objects = [
        {
            "id": "Rect1",
            "x": 50,
            "y": 200,
            "width": 25,
            "height": 35,
            "magnitude": 150,
            "angle": 270,
        },

        {
            "id": "Rect2",
            "x": 100,
            "y": 250,
            "width": 50,
            "height": 40,
            "magnitude": 100,
            "angle": 50,

        }
]

objects.append( 
    {

        "id": "Rect3",
        "x": 300,
        "y": 250,
        "width": 100,
        "height": 40,
        "magnitude": 100,
        "angle": 180,
    }
)

if pickle_load == True:
    # current_project_path = main_path + f"\projects\{current _project}"
    # with open(f'{current_project_path}\objects.pickle', 'rb') as f:
    #     objects = pickle.load(f)
    pass

animation_length = 1000
preview_running = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            width_scaler = event.w - default_width
            height_scaler = event.h  - default_height

        if event.type == pygame.KEYDOWN:
            textbox_handler = []

    win.fill((50, 50, 50))

    rect_manager.render(objects, win, event), (rect_manager_x, rect_manager_y)
    
    if preview_running == True:
        for frame in range(animation_length):
            win.blit(preview_display.render(animation_length, frame, objects), (displayport_x, displayport_y))
            pygame.display.update()
        frame = 0
        preview_running = False
    else:
        win.blit(preview_display.preview_render(objects), (displayport_x, displayport_y))
    
    pygame.display.update()
