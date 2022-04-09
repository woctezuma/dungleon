from glob import glob

from src.data_utils import get_puzzle_name_pattern
from src.image_utils import show_image
from src.load_utils import load_img
from src.puzzle_utils import extract_puzzle_elements


def main(puzzle_index=0):
    puzzle_fnames = glob(get_puzzle_name_pattern())
    puzzle_fname = puzzle_fnames[puzzle_index]

    # Whole puzzle
    puzzle_img = load_img(puzzle_fname, as_gray=True)

    # Puzzle elements
    puzzle_elements = extract_puzzle_elements(puzzle_img, trim_sprites=True, scale=1.0)

    # Display information
    for i, e in enumerate(puzzle_elements, start=1):
        print(f"Puzzle element n°{i} -> {e.shape}")

    print(f"Puzzle {puzzle_fname} -> {puzzle_img.shape}")
    show_image(puzzle_img)

    return True


if __name__ == "__main__":
    main()
