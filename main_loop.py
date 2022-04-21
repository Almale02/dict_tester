import sys
import time

import pygame

from gui.gui_elements import gui_elements
from gui.gui_events import gui_events
from local_data import local_database as local_database

gui_elements.listeners["submit_button"] = gui_events.testing_submit_button
gui_elements.listeners["lesosn_chooser_drop_down_box"] = gui_events.lesson_submit_drop_down_box
gui_elements.init_testing_scene()

def on_start():
    gui_elements.testing_scene["lesson_chooser"].cases = [*local_database.data.keys()]



pygame.init()

on_start()


while True:
    for e in pygame.event.get():
        gui_elements.testing_scene["event_update"](e)



        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    gui_elements.testing_scene["non_update"]()

    #gui_elements.testing_scene["lesson_chooser"].non_event_update()

    pygame.display.flip()
    pygame.display.update()

    gui_elements.win.fill((0, 0, 0))
    time.sleep(1 / 60)



