# Dungleon

This repository contains Python code to study the hidden rules of Dungleon.

[![Dungleon][img-cover]][game]

## Characters

[![Sprites][img-sprites]][img-sprites-original]

As official emojis:
:bow_and_arrow: :bat: :moneybag: :yellow_circle: :dragon_face: :frog: :japanese_goblin: :crown: 🧙‍♀️ :imp: :japanese_ogre: :skull: :spider: :bust_in_silhouette: 🤡 :trophy: :man_farmer: :person_fencing: 🧙‍♂️ :zombie:

## Requirements

- Install the latest version of [Python 3.X][python-download].
- Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1) To download puzzles solutions for previous days, run:

```bash
python download_puzzle_solutions.py 
```

2) To parse puzzles solutions with template matching, run:

```bash
python download_puzzle_solutions.py 
```

After this step, you should have generated a file identical to [`data/solutions.md`][solutions-markdown].

![Template matching][template-matching]

## References

- The [official website][game]
- An [archive of solutions][solutions]
- [Rules][wiki-rules] found by the community of players
- A study of [the best starter guesses][dungleon-starter-guesses]

[python-download]: <https://www.python.org/downloads/>
[game]: <https://www.dungleon.com/>
[solutions]: <https://public.amplenote.com/v9pKb8k54NRetqnjUodLsFKF>
[img-cover]: <https://github.com/woctezuma/dungleon/wiki/img/cover.png>
[img-sprites]: <https://github.com/woctezuma/dungleon/wiki/img/sprites/big.png>
[img-sprites-original]: <https://www.dungleon.com/images/elements/big/sprites.png>
[template-matching]: <https://github.com/woctezuma/dungleon/wiki/img/template_matching.png>
[solutions-markdown]: <data/solutions.md>
[wiki-rules]: <https://github.com/woctezuma/dungleon/wiki/Rules>
[dungleon-starter-guesses]: <https://github.com/woctezuma/dungleon-bot>
