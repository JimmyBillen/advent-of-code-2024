# fetching input file, from https://github.com/Rijgersberg/advent-of-code-2024/blob/main/aoc.py

from pathlib import Path
import requests

def get_input(day, as_list=True):
    """Retrieves the input data, if not locally stored fetches it from website.
    
    parameters
    ----------
    day:
        An integer representing the puzzle day (1-25) in Advent of Code.
    as_list:
        A bool, if True it returns input as a list, seperated at each newline. If false it strips the string.    
    """

    with open('sessioncookie.txt') as f:
        SESSION_COOKIE = f.read().strip()


    input_dir = Path('./input')
    input_dir.mkdir(exist_ok=True)

    filepath = input_dir / f'{day}.txt'

    if not filepath.is_file():
        print(f'Fetching input file for day {day} from AdventOfCode.com...')
        response = requests.get(f'https://adventofcode.com/2024/day/{day}/input',
                                cookies={'session': SESSION_COOKIE})
        if response.ok:
            with open(filepath, 'w') as ipt_file:
                ipt_file.write(response.text)
        else:
            raise ValueError(response.text)

    with open(filepath) as f:
        if as_list:
            return f.read().splitlines()
        else:
            return f.read().strip()
