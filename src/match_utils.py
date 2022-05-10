import numpy as np
from skimage.feature import match_template

from src.convert_utils import convert_sprite_abscissa_to_index
from src.display_utils import display_match
from src.image_utils import auto_crop


def match_puzzle_element(
    sprites, puzzle_element, block_width=None, factor=0.87, verbose=False
):
    if block_width is None:
        # NB: these blocks are squares anyway.
        block_width = sprites.shape[0]

    # Reference: https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_template.html

    try:
        result = match_template(sprites, puzzle_element)
    except ValueError:
        print(f"Sprite ({sprites.shape}) larger than template ({puzzle_element.shape})")
        print(f"Using Otsu factor {factor} to remove the frame for this binary sprite.")
        puzzle_element = auto_crop(puzzle_element, factor=factor)
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


def match_puzzle(sprites, puzzle, verbose=False):
    parsed_puzzle = []

    for i, puzzle_element in enumerate(puzzle, start=1):
        print(f"\t- element n°{i}/{len(puzzle)}")
        parsed_element = match_puzzle_element(sprites, puzzle_element, verbose=verbose)
        parsed_puzzle.append(parsed_element)

    return parsed_puzzle


def match_all_puzzles(sprites, puzzles, verbose=False):
    all_parsed_puzzles = []

    for i, puzzle in enumerate(puzzles, start=1):
        print(f"Parsing puzzle n°{i}")
        parsed_puzzle = match_puzzle(sprites, puzzle, verbose=verbose)
        all_parsed_puzzles.append(parsed_puzzle)

    return all_parsed_puzzles
