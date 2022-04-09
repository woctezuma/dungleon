import numpy as np
from skimage.feature import match_template
import math
from src.display_utils import display_match


def match_puzzle_element(sprites, puzzle_element, block_width=None, verbose=False):
    if block_width is None:
        # NB: these blocks are squares anyway.
        block_width = sprites.shape[0]

    # Reference: https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_template.html

    result = match_template(sprites, puzzle_element)
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1]

    if verbose:
        print(f"Match (ordinate, abscissa): (y, x) = ({y}, {x})")
        display_match(image=sprites, template=puzzle_element, x=x, y=y)

    sprite_index = convert_sprite_abscissa_to_index(x, block_width=block_width)

    if verbose:
        print(f"Matched sprite index = {sprite_index}")

    return sprite_index


def convert_sprite_abscissa_to_index(sprite_abscissa, block_width):
    sprite_index = math.floor(sprite_abscissa / block_width)
    return sprite_index
