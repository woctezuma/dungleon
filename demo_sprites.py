import mediapy as media

from src.data_utils import (
    get_fname_for_character_names,
    get_fname_for_character_emojis,
    get_fname_for_character_markdown,
)
from src.load_utils import load_txt
from src.sprite_utils import load_sprites_as_img_list, load_sprites_as_img


def main():
    # Descriptions
    names = load_txt(fname=get_fname_for_character_names())
    emojis = load_txt(fname=get_fname_for_character_emojis())
    markdown = load_txt(fname=get_fname_for_character_markdown())

    # Sprites as a single image
    sprites_as_img = load_sprites_as_img(as_gray=True, scale=1.0)

    # Individual sprites
    sprites = load_sprites_as_img_list(as_gray=True, trim_sprites=True, scale=1.0)

    # Display information
    for name, emoji, mark, e in zip(names, emojis, markdown, sprites):
        print(f"- {mark}\t{emoji:5}\t{name} -> {e.shape}")

    print(f"Sprites -> {sprites_as_img.shape}")
    media.show_image(sprites_as_img)

    return True


if __name__ == "__main__":
    main()
