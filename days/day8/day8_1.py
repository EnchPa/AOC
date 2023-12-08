# start af MQF and go to FMJ in aoc8_1.txt
# take the LLLRLR... String and move accordingly,
# start af MQF and first take the left string combination, so Move to DDG
# In DDG take the left String combination, so move to QTS and so on


# make 3 arrays, one for both sides and one for the start line
# take 1. array and 0th element and look at the string and search for the 0th element of the correct array
# look for the found element in the 1. array und look at the string again. repeat until you find the correct element
# if the string ends, start again at the beginning of the string
def find_steps(array1, array2, array3, line_array):
    steps_taken = 0 # Anzahl Gesamtschritte
    array1_line = array1.index("AAA") # index von AAA in array1
    current_element_left = array1[array1_line] # hier AAA
    index_line_array = steps_taken # index für line_array, hier 0
    while True:
        if current_element_left == "ZZZ":
            break
        if line_array[index_line_array] == "L": # Wenn Element in LR String L ist
            current_element_tuple = array2[array1_line] # dann nimm das Element aus array2
        elif line_array[index_line_array] == "R":
            current_element_tuple = array3[array1_line]
        steps_taken += 1
        if index_line_array >= len(line_array) - 1:
            index_line_array = 0
        else:
            index_line_array += 1
        current_element_left = current_element_tuple
        array1_line = array1.index(current_element_tuple)
    return steps_taken


def create_arrays(lines):
    array1 = []
    array2 = []
    array3 = []
    line_array = []
    line = lines[0]
    print(f"line: {line}")
    for element in line:
        line_array.append(element)
    line_array.pop(-1)
    print(f"line_array: {line_array}")
    for line in lines[2:]:
        teile = line.split("=")
        hauptteil = teile[0].strip()
        unterpaare = teile[1].strip().replace("(", "").replace(")", "").split(", ")
        array1.append(hauptteil)
        array2.append(unterpaare[0])
        array3.append(unterpaare[1])
    print(f"array1: {array1}")
    print(f"array2: {array2}")
    print(f"array3: {array3}")

    return array1, array2, array3, line_array


def start(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    array1, array2, array3, line_array = create_arrays(lines)
    steps_taken = find_steps(array1, array2, array3, line_array)
    print(f"Total steps taken: {steps_taken}")


if __name__ == "__main__":
    filepath = '../../dateien/aoc8_1.txt'
    start(filepath)
