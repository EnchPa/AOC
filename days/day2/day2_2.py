# What is the minimum number of red/green/blue cubes necessary
import re

all_colors = ["red", "green", "blue"]


# Function returns the minimum cubes of each color
def find_games(line):
    my_bool = True
    red_match = line.find("red")
    highest_red_number = 0
    while red_match != -1 and my_bool:
        red_number = line[red_match - 3:red_match]
        if int(red_number) > highest_red_number:
            highest_red_number = int(red_number)
        else:
            red_match = line.find("red", red_match + 1)
    blue_match = line.find("blue")
    highest_blue_number = 0
    while blue_match != -1 and my_bool:
        blue_number = line[blue_match - 3:blue_match]
        if int(blue_number) > highest_blue_number:
            highest_blue_number = int(blue_number)
        else:
            blue_match = line.find("blue", blue_match + 1)
    green_match = line.find("green")
    highest_green_number = 0
    while green_match != -1 and my_bool:
        green_number = line[green_match - 3:green_match]
        if int(green_number) > highest_green_number:
            highest_green_number = int(green_number)
        else:
            green_match = line.find("green", green_match + 1)

    total_sum = highest_red_number * highest_blue_number * highest_green_number
    return total_sum


def process_file(filepath):
    total = 0
    with open(filepath, 'r') as file:
        for line in file:
            number_str = find_games(line)
            total += int(number_str)
    return total


# Datei verarbeiten
total_sum = process_file('C:/Users/larsg/Desktop/AOC/dateien/aoc2_1.txt')
print(f"Total sum: {total_sum}")
