import numpy as np
import skimage
from PIL import Image


def extract_square_blocks(img):
    if len(img.shape) > 2:
        (h, w, num_channels) = img.shape
        block_shape = (h, h, num_channels)
    else:
        (h, w) = img.shape
        block_shape = (h, h)

    blocks = skimage.util.view_as_blocks(img, block_shape).squeeze()

    return blocks


def binarize(img):
    threshold = skimage.filters.threshold_otsu(img)
    binary_img = img < threshold

    return binary_img


def compute_bbox(img):
    binary_img = binarize(img)
    bbox = Image.fromarray(binary_img).getbbox()

    return bbox


def auto_crop(img):
    bbox = compute_bbox(img)
    pil_img = Image.fromarray(img).crop(bbox)

    return np.array(pil_img)
