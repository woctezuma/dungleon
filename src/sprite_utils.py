from src.data_utils import get_fname_for_character_sprites
from src.image_utils import extract_square_blocks, auto_crop
from src.load_utils import load_img


def load_sprites_as_img(as_gray=True):
    fname = get_fname_for_character_sprites()

    return load_img(fname, as_gray=as_gray)


def load_sprites_as_img_list(as_gray=True, trim_sprites=True):
    img = load_sprites_as_img(as_gray=as_gray)
    sprites = extract_square_blocks(img)

    trimmed_sprites = []
    for block in sprites:

        if trim_sprites:
            small_element = auto_crop(block)
        else:
            small_element = block

        trimmed_sprites.append(small_element)

    return trimmed_sprites
