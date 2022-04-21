import  local_data.local_database as local_database
correct = 0
incorrect = 0
remaining = None

correct_hun_word = None
correct_eng_word = None





choosed_lesson = "test_lesson1"
def get_data_str():
    return f"Correct : {correct}, Incorrect : {incorrect}, Remaining : {remaining}"

def new_test():
    global correct,incorrect,remaining

    correct = 0
    incorrect = 0
    remaining = len(local_database.data[choosed_lesson])

