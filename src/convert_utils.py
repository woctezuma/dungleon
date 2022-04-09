import math


def convert_sprite_abscissa_to_index(sprite_abscissa, block_width):
    sprite_index = math.floor(sprite_abscissa / block_width)
    return sprite_index


def convert_parsed_sprite(sprite_index, symbols):
    return symbols[sprite_index]


def convert_parsed_puzzle(parsed_puzzle, symbols):
    return [convert_parsed_sprite(index, symbols) for index in parsed_puzzle]


def convert_all_parsed_puzzles(all_parsed_puzzles, symbols):
    return [convert_parsed_puzzle(puzzle, symbols) for puzzle in all_parsed_puzzles]
