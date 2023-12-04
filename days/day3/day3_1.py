# Zahlen finden die an ein (nicht Punkt-) Zeichen angrenzen, auch Diagonal über die Zeilen hinweg,
# alle diese zusammen addieren
import re

with open('../../dateien/aoc1_1.txt', 'r') as file:
    lines = file.readlines()

numbers = 0
def process_file(lines):
    for line in lines:
        matches = re.findall(r'(/d+)', line)
        for match in matches:
            symbols_front = line[match:match-1]
            symbols_back = line[match+1:match+2]
            if symbols_front in "*#'?=)(/&%$§!^°{[]}"

