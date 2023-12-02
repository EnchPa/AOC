'''numbers = 0
with open('../dateien/input.txt', 'r') as file:
    lines = file.readlines()

non_digit_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
non_digit_numbers_short = {"one": "1", "two": "2", "six": "6"}
non_digit_numbers_medium = {"four": "4", "five": "5", "nine": "9"}
non_digit_numbers_long = {"three": "3", "seven": "7", "eight": "8"}

for line in lines:
    bool = False
    end_length = len(line) - 2
    start_length = 0
    line_numbers = []
    start = line[start_length]
    end = line[end_length]
    while start in "abcdefghijklmnopqrstuvwxyz" and bool == False:
        three_letter_element = line[start_length:start_length + 3]
        four_letter_element = line[start_length:start_length + 4]
        five_letter_element = line[start_length:start_length + 5]
        for element in non_digit_numbers_long:
            if str(element) in five_letter_element:
                print(f"5er_element: {element}")
                start = non_digit_numbers_long[element]
                print(f"start_element: {start}")
                bool = True
                break
        if bool == False:
            for element in non_digit_numbers_medium:
                if str(element) in four_letter_element:
                    start = non_digit_numbers_medium[element]
                    bool = True
                    break
        if bool == False:
            for element in non_digit_numbers_short:
                if str(element) in three_letter_element:
                    start = non_digit_numbers_short[element]
                    bool = True
                    break

        if not bool:
            start_length += 1
            start = line[start_length]
    counter = 0
    bool = False

    while end in "abcdefghijklmnopqrstuvwxyz" and bool == False:
        counter += 1
        if counter > 2:
            five_letter_element = line[end_length:end_length + 5]
            for element in non_digit_numbers:
                if str(element) in five_letter_element:
                    end = str(non_digit_numbers.index(element) + 1)
                    bool = True
                    break
            if not bool:
                end_length -= 1
                end = line[end_length]
    number = str(start) + str(end)
    print(f"number: {number}")
    numbers = numbers + int(number)
print(f"numbers: {numbers}")






"""


        if counter == 3:
            five_letter_element = line[end_length:end_length + 3]
            #print(f"letztes 3_element: {five_letter_element}")
            for element in non_digit_numbers:
                if str(element) in five_letter_element:
                    end = str(non_digit_numbers.index(element)+1)
                    #print(f"ende3: {end}")
                    bool = True
                    break
            if not bool:
                end_length -= 1
                end = line[end_length]



        if end in "abcdefghijklmnopqrstuvwxyz" and bool == False and counter == 4:
            five_letter_element = line[end_length+1:end_length + 5]
            #print(f"letztes 4_element: {five_letter_element}")
            for element in non_digit_numbers:
                if str(element) in five_letter_element:
                    end = str(non_digit_numbers.index(element)+1)
                    bool = True
                    break
            if not bool:
                end_length -= 1
                end = line[end_length]
        if end in "abcdefghijklmnopqrstuvwxyz" and bool == False and counter > 4:
            five_letter_element = line[end_length+2:end_length + 7]
            #print(f"letztes 5_element: {five_letter_element}")
            for element in non_digit_numbers:
                if str(element) in five_letter_element:
                    end = str(non_digit_numbers.index(element)+1)
                    bool = True
                    break
            if not bool:
                end_length -= 1
                end = line[end_length]
        elif counter < 3 and bool == False:
            end_length -= 1
            end = line[end_length]"""
'''

import re

# Wörterbuch für Zahlenwörter
number_words = {
    "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

# Funktion, um das erste und letzte Zahlwort oder Ziffer in einer Zeile zu finden
def find_numbers(line):
    # Regex, um Zahlenwörter oder einzelne Ziffern zu finden (case-insensitive)
    matches = re.findall(r'(?i)\b(one|two|three|four|five|six|seven|eight|nine|\d)\b', line)
    if matches:
        # Umwandlung des ersten und letzten Matches in Ziffern
        start = number_words.get(matches[0].lower(), matches[0])
        end = number_words.get(matches[-1].lower(), matches[-1])
        print(f"start: {start} end: {end}")
        # Wenn nur ein Match vorhanden ist, wird es verdoppelt
        return start + end if len(matches) > 1 else start * 2
    return "0"

# Datei lesen und Zahlen verarbeiten
def process_file(filepath):
    total = 0
    with open(filepath, 'r') as file:
        for line in file:
            number_str = find_numbers(line)
            total += int(number_str)
    return total

# Datei verarbeiten
total_sum = process_file('../dateien/aoc1_2.txt')
print(f"Total sum: {total_sum}")

