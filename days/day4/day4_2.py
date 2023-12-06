# get winning numbers per line
# The first match makes the card worth one point and each match after the first doubles the point value of that card.
# that formula: 2^(number of matches - 1)
import re
from tqdm import tqdm

reg = r"(\d+)"


def cardpoints(lines):
    complete_amount_cards = 0
    extra_tickets = 0
    karten_array = []
    for x, line in tqdm(enumerate(lines)):
        line_array = []
        treffer = 0
        array_eintrag = 0
        for i in re.findall(reg, line):
            line_array.append(i)
        for element in line_array[1:11]:
            if element in line_array[11::]:
                treffer += 1
        # array Einträge über 0 zählen
        # wenn Einträge > 0:
        # total = Einträge + 1
        # einträge - 1
        for f, eintrag in enumerate(karten_array):
            #print(f"eintrag: {eintrag}")
            if eintrag > 0:
                array_eintrag += 1
                #print(f"eintrag: {eintrag}")
                karten_array[f] = eintrag - 1

        if treffer > 0:
            amount_cards = array_eintrag + 1
            ergebnis = treffer
            anzahl_eintraege = array_eintrag
            for i in range(anzahl_eintraege+1):
                karten_array.append(ergebnis)
        else:
            amount_cards = array_eintrag + 1
        complete_amount_cards += amount_cards



        print(f"complete_amount of cards: {complete_amount_cards}, Menge Karten line {x+1}: {amount_cards}, treffer: {treffer}, anzahl weitere Karten linie {x+1}: {ergebnis} durch: {treffer} treffer mal {array_eintrag} karten im array")
    #print(f" karten_array: {karten_array}")
    return complete_amount_cards


def start(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    total = cardpoints(lines)
    print(f"Total sum: {total}")


if __name__ == "__main__":
    filepath = '../../dateien/aoc4_1.txt'
    start(filepath)
