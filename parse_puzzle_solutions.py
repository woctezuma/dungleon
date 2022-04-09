from glob import glob

from src.data_utils import (
    get_solution_image_folder,
    get_fname_for_character_names,
)
from src.image_utils import show_image
from src.load_utils import load_txt, load_img
from src.puzzle_utils import extract_puzzle_elements
from src.sprite_utils import (
    load_sprites_as_img_list,
    get_rescale_factor,
    load_sprites_as_img,
)


def main():
    character_names = load_txt(fname=get_fname_for_character_names())

    sprites_as_img = load_sprites_as_img(as_gray=True, scale=get_rescale_factor())
    print(sprites_as_img.shape)

    sprites = load_sprites_as_img_list(
        as_gray=True, trim_sprites=True, scale=get_rescale_factor()
    )
    for name, e in zip(character_names, sprites):
        print(f"{name} -> {e.shape}")

    solution_fnames = glob(f"{get_solution_image_folder()}*.jpg")
    puzzle_img = load_img(fname=solution_fnames[0], as_gray=True)

    show_image(puzzle_img)

    puzzle_elements = extract_puzzle_elements(puzzle_img, trim_sprites=True)
    for e in puzzle_elements:
        print(e.shape)

    return True


if __name__ == "__main__":
    main()
