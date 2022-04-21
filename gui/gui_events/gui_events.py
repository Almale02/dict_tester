import time

import pygame.display

from local_data.program_state_data import testing_scene
from gui.gui_elements import gui_elements
from local_data import local_database
from helper_functions import functions as helper_functions



def testing_submit_button(arg):


    if testing_scene.correct_eng_word == gui_elements.testing_scene["submit_txt"].txt_obj.txt:

        testing_scene.correct += 1

        testing_scene.remaining = len(local_database.data[testing_scene.choosed_lesson]) - (testing_scene.correct + testing_scene.incorrect)


        if not testing_scene.remaining <= 0:
            testing_scene.correct_eng_word = list(local_database.data[testing_scene.choosed_lesson].values())[testing_scene.correct + testing_scene.incorrect]
            testing_scene.correct_hun_word = helper_functions.get_key_by_value(local_database.data[testing_scene.choosed_lesson], testing_scene.correct_eng_word)
            gui_elements.testing_scene["hun_word"].txt_obj.txt = testing_scene.correct_hun_word
        gui_elements.testing_scene["answer_data"].txt_obj.txt = testing_scene.get_data_str()



    else:

        testing_scene.incorrect += 1

        testing_scene.remaining = len(local_database.data[testing_scene.choosed_lesson]) - (testing_scene.correct + testing_scene.incorrect)

        gui_elements.testing_scene["english_word"].txt_obj.txt = testing_scene.correct_eng_word
        gui_elements.testing_scene["non_update"]()
        pygame.display.flip()
        pygame.display.update()

        if not testing_scene.remaining <= 0:
            time.sleep(3)
            gui_elements.testing_scene["english_word"].txt_obj.txt = "!!!"


            testing_scene.correct_eng_word = list(local_database.data[testing_scene.choosed_lesson].values())[testing_scene.correct + testing_scene.incorrect]
            testing_scene.correct_hun_word = helper_functions.get_key_by_value(local_database.data[testing_scene.choosed_lesson], testing_scene.correct_eng_word)
            gui_elements.testing_scene["hun_word"].txt_obj.txt = testing_scene.correct_hun_word


        gui_elements.testing_scene["answer_data"].txt_obj.txt = testing_scene.get_data_str()

def lesson_submit_drop_down_box(arg):
    testing_scene.choosed_lesson = arg[0]
    testing_scene.correct_hun_word = helper_functions.get_key_by_index(local_database.data[arg[0]], 0)
    gui_elements.testing_scene["hun_word"].txt_obj.txt = testing_scene.correct_hun_word
    testing_scene.correct_eng_word  = local_database.data[arg[0]][testing_scene.correct_hun_word]

    testing_scene.new_test()










