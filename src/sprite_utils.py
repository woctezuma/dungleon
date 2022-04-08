from skimage.transform import rescale

from src.data_utils import get_fname_for_character_sprites
from src.image_utils import extract_square_blocks, auto_crop
from src.load_utils import load_img


def get_rescale_factor():
    trimmed_knight_puzzle_width = 86
    trimmed_knight_sprite_width = 52
    return trimmed_knight_puzzle_width / trimmed_knight_sprite_width


def load_sprites_as_img(as_gray=True, scale=1.0):
    fname = get_fname_for_character_sprites()
    img = load_img(fname, as_gray=as_gray)

    if scale != 1:
        print("Scaling the image by a factor {scale:.2f}")
        img = rescale(img, scale)

    return img


def load_sprites_as_img_list(as_gray=True, trim_sprites=True, scale=1.0):
    img = load_sprites_as_img(as_gray=as_gray)
    sprites = extract_square_blocks(img)

    trimmed_sprites = []
    for block in sprites:

        if trim_sprites:
            small_element = auto_crop(block)
        else:
            small_element = block

        if scale != 1:
            small_element = rescale(small_element, scale)

        trimmed_sprites.append(small_element)

    return trimmed_sprites
