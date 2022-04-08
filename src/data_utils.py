from pathlib import Path


def get_data_folder():
    folder_name = "data/"
    Path(folder_name).mkdir(exist_ok=True)
    return folder_name


def get_solution_image_folder():
    folder_name = get_data_folder() + "solutions/"
    Path(folder_name).mkdir(exist_ok=True)
    return folder_name


def get_character_sprites():
    return get_data_folder() + "characters.png"


def get_character_names():
    return get_data_folder() + "characters.txt"


def get_character_emojis():
    return get_data_folder() + "emojis.txt"


def get_solution_urls():
    return get_data_folder() + "solutions.txt"