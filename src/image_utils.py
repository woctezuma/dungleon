import numpy as np
import skimage
from PIL import Image

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


def show_image(img, max_value=255):
    img = img * max_value / img.max()
    Image.fromarray(img).show()

    return
