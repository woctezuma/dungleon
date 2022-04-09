from skimage.transform import rescale

from src.block_utils import extract_square_blocks
from src.data_utils import get_fname_for_character_sprites
from src.image_utils import auto_crop_img_list, rescale_img_list
from src.load_utils import load_img


def get_rescale_factor():
    trimmed_knight_puzzle_width = 86
    trimmed_knight_sprite_width = 52
    return trimmed_knight_puzzle_width / trimmed_knight_sprite_width


def load_sprites_as_img(as_gray=True, scale=1.0):
    fname = get_fname_for_character_sprites()
    img = load_img(fname, as_gray=as_gray)

    if scale != 1:
        print("Scaling aggregated sprites by a factor {scale:.2f}")
        img = rescale(img, scale)

    return img


def load_sprites_as_img_list(as_gray=True, trim_sprites=True, scale=1.0):
    img = load_sprites_as_img(as_gray=as_gray)
    sprites = extract_square_blocks(img)

    if trim_sprites:
        sprites = auto_crop_img_list(sprites)

    if scale != 1:
        # NB: do not rescale() before extract_square_blocks(), or block shape might not divide the image shape!
        print("Scaling individual sprites by a factor {scale:.2f}")
        sprites = rescale_img_list(sprites, scale)

    return sprites
