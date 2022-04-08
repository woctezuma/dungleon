import math

from src.image_utils import auto_crop


def extract_puzzle_elements(img, trim_sprites=True, verbose=True):
    element_width = 128
    element_offset = 15

    image_width = img.shape[1]
    element_stride = element_width + element_offset
    num_elements = math.ceil(image_width / element_stride)

    puzzle_elements = []

    for i in range(num_elements):
        w_start = element_stride * i
        w_end = w_start + element_width

        small_element = img[:, w_start:w_end]

        if trim_sprites:
            small_element = auto_crop(small_element)

        puzzle_elements.append(small_element)

    if verbose:
        print(f"#elements = {len(puzzle_elements)}")

    return puzzle_elements
