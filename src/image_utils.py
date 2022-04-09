import numpy as np
import skimage
from PIL import Image
from skimage.transform import rescale


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
    img = img * max_value / img.max()
    Image.fromarray(img).show()

    return
