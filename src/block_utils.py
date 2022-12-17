import math

import skimage.util


def extract_square_blocks(img):
    if len(img.shape) > 2:
        (h, w, num_channels) = img.shape
        block_shape = (h, h, num_channels)
    else:
        (h, w) = img.shape
        block_shape = (h, h)

    blocks = skimage.util.view_as_blocks(img, block_shape).squeeze()

    return blocks


def extract_tiled_elements(img, element_width, element_offset):
    image_width = img.shape[1]
    element_stride = element_width + element_offset
    num_elements = math.ceil(image_width / element_stride)

    blocks = []

    for i in range(num_elements):
        w_start = element_stride * i
        w_end = w_start + element_width

        element = img[:, w_start:w_end]

        blocks.append(element)

    return blocks
