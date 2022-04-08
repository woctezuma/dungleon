def load_txt(fname, verbose=True):
    with open(fname, "r", encoding="utf8") as f:
        lines = f.readlines()

    data = [row.strip() for row in lines]

    if verbose:
        print(data)

    return data
