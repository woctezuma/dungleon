from src.data_utils import get_solution_urls, get_solution_image_folder
from src.download_utils import download_files
from src.load_utils import load_txt


def main():
    urls = load_txt(fname=get_solution_urls())
    download_files(urls, output_folder=get_solution_image_folder())

    return True


if __name__ == "__main__":
    main()
