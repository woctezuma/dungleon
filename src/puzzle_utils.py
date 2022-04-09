from src.block_utils import extract_tiled_elements
from src.image_utils import auto_crop_img_list, auto_crop


def extract_puzzle_elements(img, trim_sprites=True, verbose=True):
    element_width = 128
    element_offset = 15

    if verbose:
        print(f"Original image shape: {img.shape}")

    img = auto_crop(img)

    if verbose:
        print(f"Auto-cropped image shape: {img.shape}")

    puzzle_elements = extract_tiled_elements(img, element_width, element_offset)

    if verbose:
        print(f"#elements = {len(puzzle_elements)}")

    if trim_sprites:
        puzzle_elements = auto_crop_img_list(puzzle_elements)

    return puzzle_elements
