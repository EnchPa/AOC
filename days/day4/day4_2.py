# get winning numbers per line
# The first match makes the card worth one point and each match after the first doubles the point value of that card.
# that formula: 2^(number of matches - 1)
import re
import numpy as np

reg = r"(\d+)"


def cardpoints(lines):
    complete = 0
    extra_tickets = 0
    for line in lines:
        line_array = []
        treffer = 0
        for i in re.findall(reg, line):
            line_array.append(i)
        for element in line_array[1:11]:
            if element in line_array[11::]:
                treffer += 1

        if treffer > 0:
                total = treffer + treffer * extra_tickets
        else:
            total = 0
        complete += total

        extra_tickets = treffer
        print(f" complete: {complete}, extra_tickets: {extra_tickets}, treffer: {treffer}")
    return complete


def start(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    total = cardpoints(lines)
    print(f"Total sum: {total}")


if __name__ == "__main__":
    filepath = '../../dateien/aoc4_1.txt'
    start(filepath)
