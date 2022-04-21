import pygame
from pyg_gui.gui_elements.text_out import Txt_out
from pyg_gui.gui_elements.button import Button
from pyg_gui.gui_elements.text_in import Txt_in
from pyg_gui.gui_elements.drop_down import Drop_down
from pyg_gui.helper_files.text_class import Text
from local_data.program_state_data import testing_scene as testing_scene_data




pygame.init()
win = pygame.display.set_mode((800, 800))



listeners = {
    "submit_button" : None,
    "lesosn_chooser_drop_down_box" : None
}

def non_update():
    testing_scene["answer_data"].txt_obj.txt = testing_scene_data.get_data_str()



    for i, element in enumerate(testing_scene.keys()):
        if not i <= 1:
            testing_scene[element].non_event_update()

def event_update(e):
    for i, element in enumerate(testing_scene.keys()):
        if not i <= 1:
            testing_scene[element].event_update(e)

testing_scene = None

def init_testing_scene():

    global testing_scene
    testing_scene = {
        "non_update" : non_update,
        "event_update" : event_update,
        "english_word" : Txt_out(win, (0,50), (800,35), (0,0,0), Text(30, "!!!", (255,255,255))),
        "hun_word" : Txt_out(win, (0, 90), (800, 35), (0, 0, 0), Text(30, "!!!", (255, 255, 255))),
        "submit_button" : Button(win, (800  // 2 - Text(30, "submit", (255, 255 ,255)).font_renderer.get_width() // 2 - 40, 130), (Text(30, "submit", (255, 255, 255)).font_renderer.get_width() + 90, 35), (0, 30, 100), Text(30, "submit", (255, 255, 255)),[listeners["submit_button"]], [(1,2,3)]),
        "submit_txt" : Txt_in(win, (0, 170), (800, 35), (0,0,0), Text(30, "!!!", (255,255,255))),
        "answer_data" : Txt_out(win, (0, 210), (800,35), (0,0,0), Text(30, "Correct : 0, Incorrect : 0, Remaining : 0", (255,255,255))),
        "lesson_chooser" :  Drop_down(win, (win.get_width() // 2 - 250  // 2, 255),(250,40),(0,0,40),["1","2","3","4","5","6"],Text(30,"choose boxasd",(100,0,100)),listeners["lesosn_chooser_drop_down_box"],3)



    }

