from src.block_utils import extract_tiled_elements
from src.image_utils import auto_crop_img_list, auto_crop, rescale_img_list


def extract_puzzle_elements(img, trim_sprites=True, scale=1.0, verbose=True):
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
        print("Trimming individual puzzle elements.")
        puzzle_elements = auto_crop_img_list(puzzle_elements)

    if scale != 1:
        # NB: this is optional. Preferably, rescale sprites rather than puzzle elements,
        #     as this would scale better to a large number of archived puzzle solutions.
        print(f"Scaling individual puzzle elements by a factor {scale:.2f}")
        puzzle_elements = rescale_img_list(puzzle_elements, scale)

    return puzzle_elements
