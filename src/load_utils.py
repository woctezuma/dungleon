import skimage.io


def load_txt(fname, verbose=True):
    with open(fname, "r", encoding="utf8") as f:
        lines = f.readlines()

    data = [row.strip() for row in lines]

    if verbose:
        print(data)

    return data


def load_img(fname, as_gray=True):
    return skimage.io.imread(fname, as_gray=as_gray)
