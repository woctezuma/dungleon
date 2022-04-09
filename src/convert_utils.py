import math


def convert_sprite_abscissa_to_index(sprite_abscissa, block_width):
    sprite_index = math.floor(sprite_abscissa / block_width)
    return sprite_index
