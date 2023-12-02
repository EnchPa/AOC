# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




with open('../dateien/aoc1.txt', 'r') as file:
    datei = file.readlines()

numbers = 0
for line in (datei):
    end_length = len(line)-2
    start_length = 0
    start = line[start_length]
    end = line[end_length]
    while start in "abcdefghijklmnopqrstuvwxyz":
        start_length += 1
        start = line[start_length]
    while end in "abcdefghijklmnopqrstuvwxyz":
        end_length -= 1
        end = line[end_length]

    #print(f"start: {line[start_length]}, ende: {line[end_length]}")
    number = str(start) + str(end)
    #print(f"number: {number}")
    numbers = numbers + int(number)

print(numbers)











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
