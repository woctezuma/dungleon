import shutil

import requests


def get_file_ext(url):
    return url.split(".")[-1]


def download_file(url, fname):
    # Reference:https://stackoverflow.com/a/39217788/376454

    with requests.get(url, stream=True) as r:
        with open(fname, "wb") as f:
            shutil.copyfileobj(r.raw, f)

    return fname


def download_archived_puzzle_solutions(urls, output_folder):
    num_files = len(urls)

    for i, url in enumerate(urls, start=1):
        day_no = f"{i:03}"
        file_ext = get_file_ext(url)
        output_fname = f"{output_folder}{day_no}.{file_ext}"

        print(f"[{i:03}/{num_files:03}] Downloading {url} to {output_fname}")
        download_file(url, output_fname)

    return
