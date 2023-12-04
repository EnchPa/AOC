# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
import re

all_colors = ["red", "green", "blue"]


# Function returns the game number of the games which do not go over the limit of 12 red, 13 green and 14 blue
def find_games(line):
    # Find game number
    if line.find("Game") != -1:
        matches = re.findall(r'(\d+)', line)
        game_number = matches[0]
        # Check if game number is a digit
        if not game_number.isdigit() or int(game_number) > 100:
            print("error: game number is not a digit or bigger than 100")

    my_bool = True
    red_match = line.find("red")
    while red_match != -1 and my_bool:
        red_number = line[red_match - 3:red_match]
        if int(red_number) > 12:
            my_bool = False
        else:
            red_match = line.find("red", red_match + 1)

    blue_match = line.find("blue")
    while blue_match != -1 and my_bool:
        blue_number = line[blue_match - 3:blue_match]
        if int(blue_number) > 14:
            my_bool = False
        else:
            blue_match = line.find("blue", blue_match + 1)
    green_match = line.find("green")
    while green_match != -1 and my_bool:
        green_number = line[green_match - 3:green_match]
        if int(green_number) > 13:
            my_bool = False
        else:
            green_match = line.find("green", green_match + 1)

    if my_bool:
        return game_number
    else:
        return 0


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
