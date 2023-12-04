# Zahlen finden die an ein (nicht Punkt-) Zeichen angrenzen, auch Diagonal über die Zeilen hinweg,
# alle diese zusammen addieren
import re

numbers = 0


def process_lines(line):
    number = 0
    numbers = []
    for match in re.finditer(r'(\d+)', line):
        start, end = match.span()
        symbols_front = line[start - 1] if start > 0 else None
        symbols_back = line[end] if end < len(line) else None
        if (symbols_front and symbols_front in "*#'?=)(/&%$§!^°{[]}") or (symbols_back and symbols_back in "*#'?=)(/&%$§!^°{[]}"):
            print(f"symbols_front: {symbols_front}, symbols_back: {symbols_back}")
            number = int(line[start:end])
            print(f"start: {start}, end: {end}, number: {number}")
            number += number
        else :

    return number


def process_file(filepath):
    total = 0
    with open(filepath, 'r') as file:
        for line in file:
            number_str = process_lines(line)
            total += number_str
    return total


if __name__ == "__main__":
    filepath = '../../dateien/aoc3_1.txt'
    numbers = process_file(filepath)
    print(f"Total sum: {numbers}")
