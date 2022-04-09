from pathlib import Path


def get_data_folder():
    folder_name = "data/"
    Path(folder_name).mkdir(exist_ok=True)
    return folder_name


def get_solution_image_folder():
    folder_name = get_data_folder() + "solutions/"
    Path(folder_name).mkdir(exist_ok=True)
    return folder_name


def get_fname_for_character_sprites():
    return get_data_folder() + "characters.png"


def get_fname_for_character_markdown():
    return get_data_folder() + "characters.md"


def get_fname_for_character_names():
    return get_data_folder() + "characters.txt"


def get_fname_for_character_emojis():
    return get_data_folder() + "emojis.txt"


def get_fname_for_solution_markdown():
    return get_data_folder() + "solutions.md"


def get_fname_for_solution_urls():
    return get_data_folder() + "solutions.txt"
