import shutil

import requests
import pathlib


def get_file_ext(url):
    return url.split(".")[-1]


def download_file(url, fname):
    # Reference:https://stackoverflow.com/a/39217788/376454

    with requests.get(url, stream=True) as r:
        with open(fname, "wb") as f:
            shutil.copyfileobj(r.raw, f)

    return fname


def download_files(urls, output_folder):
    num_files = len(urls)
    assert num_files < 1000

    for i, url in enumerate(urls, start=1):
        file_no = f"{i:03}"
        file_ext = get_file_ext(url)
        output_fname = f"{output_folder}{file_no}.{file_ext}"

        if pathlib.Path(output_fname).exists():
            continue

        print(f"[{i:03}/{num_files:03}] Downloading {url} to {output_fname}")
        download_file(url, output_fname)

    return
