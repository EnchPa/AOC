# Zahlen finden die an ein (nicht Punkt-) Zeichen angrenzen, auch Diagonal über die Zeilen hinweg,
# alle diese zusammen addieren
import re

numbers = 0
special_chars = "*#'?=)(/&%$§!^°{}[]+-*/<>!,'\";:?_#@&$%^\\|~"

def process_lines(lines):
    number = 0
    for i, line in enumerate(lines):
        previous_line = lines[i - 1] if i > 0 else None
        next_line = lines[i + 1] if i < len(lines) - 1 else None


        numbers = []
        for match in re.finditer(r'(\d+)', line):
            my_little_bool = False
            start, end = match.span()
            symbols_front = line[start - 1] if start > 0 else None
            symbols_back = line[end] if end < len(line) else None
            if (symbols_front and symbols_front in special_chars) or (
                    symbols_back and symbols_back in special_chars):
                number1 = int(line[start:end])
                number += number1
                print(f"start: {start}, end: {end}, nummer: {number1}, total: {number} symbols_front: {symbols_front}, symbols_back: {symbols_back}")
                my_little_bool = True
            if previous_line and not my_little_bool:
                start_index = max(start - 1, 0)
                end_index = min(end + 1, len(previous_line))
                for char in previous_line[start_index:end_index]:
                    if char in special_chars:
                        number2 = int(line[start:end])
                        number += number2
                        print(f"start: {start}, end: {end}, nummer: {number2}, total: {number}")
                        my_little_bool = True
            if next_line and not my_little_bool:
                start_index = max(start - 1, 0)
                end_index = min(end + 1, len(next_line))
                for char in next_line[start_index:end_index]:
                    if char in special_chars:
                        number3 = int(line[start:end])
                        number += number3
                        print(f"start: {start}, end: {end}, nummer: {number3}, total: {number}")
    return number


if __name__ == "__main__":
    filepath = '../../dateien/aoc3_1.txt'
    with open(filepath, 'r') as file:
        lines = file.readlines()
        numbers += process_lines(lines)
    print(f"Total sum: {numbers}")
