import skimage


def extract_square_blocks(img):
    if len(img.shape) > 2:
        (h, w, num_channels) = img.shape
        block_shape = (h, h, num_channels)
    else:
        (h, w) = img.shape
        block_shape = (h, h)

    blocks = skimage.util.view_as_blocks(img, block_shape).squeeze()

    return blocks
