def get_key_by_value(dict, target):
    for key, value in dict.items():
        if target == value:
            return key

def get_key_by_index(dict : dict, index: int):
    for i, key in enumerate(dict.keys()):
        if i == index:
            return key





