import numpy as np
import skimage.filters
from PIL import Image
from skimage.transform import rescale


def binarize(img, factor=1.0):
    threshold = skimage.filters.threshold_otsu(img)
    binary_img = img < threshold * factor

    return binary_img


def compute_bbox(img, factor=1.0):
    binary_img = binarize(img, factor=factor)
    bbox = Image.fromarray(binary_img).getbbox()

    return bbox


def auto_crop(img, factor=1.0):
    bbox = compute_bbox(img, factor=factor)
    pil_img = Image.fromarray(img).crop(bbox)

    return np.array(pil_img)


def auto_crop_img_list(img_list):
    cropped_img_list = []

    for img in img_list:
        cropped_img = auto_crop(img)
        cropped_img_list.append(cropped_img)

    return cropped_img_list


def rescale_img_list(img_list, scale):
    rescaled_img_list = []

    for img in img_list:
        rescaled_img = rescale(img, scale)
        rescaled_img_list.append(rescaled_img)

    return rescaled_img_list


def show_image(img, max_value=255):
    img = np.array(img)
    img = img * max_value / img.max()
    Image.fromarray(img).show()

    return
