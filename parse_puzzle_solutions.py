from glob import glob

from src.convert_utils import convert_all_parsed_puzzles
from src.data_utils import get_puzzle_name_pattern, get_fname_for_character_markdown
from src.display_utils import display_all_parsed_puzzles
from src.load_utils import load_img, load_txt
from src.match_utils import match_puzzle_element, match_all_puzzles
from src.puzzle_utils import extract_puzzle_elements
from src.sprite_utils import get_rescale_factor, load_sprites_as_img


def main(puzzle_index=0, element_index=0, debug=False):
    # Sprites as a single image
    sprites = load_sprites_as_img(scale=get_rescale_factor())

    # Puzzle elements
    puzzle_fnames = glob(get_puzzle_name_pattern())
    puzzle_fname = puzzle_fnames[puzzle_index]
    puzzle_elements = extract_puzzle_elements(load_img(puzzle_fname))

    puzzle_element = puzzle_elements[element_index]

    # Template matching
    if debug:
        sprite_index = match_puzzle_element(sprites, puzzle_element, verbose=True)

    # Template matching for every puzzle
    all_puzzles = (
        extract_puzzle_elements(load_img(fname), verbose=False)
        for fname in puzzle_fnames
    )
    all_parsed_sprites = match_all_puzzles(sprites, all_puzzles)

    # Conversion of sprite indices to character names, emojis, markdown, etc.
    symbols = load_txt(fname=get_fname_for_character_markdown())
    converted_sprites = convert_all_parsed_puzzles(all_parsed_sprites, symbols=symbols)

    display_all_parsed_puzzles(converted_sprites)

    return True


if __name__ == "__main__":
    main()
