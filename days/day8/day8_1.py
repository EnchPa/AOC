# start af MQF and go to FMJ in aoc8_1.txt
# take the LLLRLR... String and move accordingly,
# start af MQF and first take the left string combination, so Move to DDG
# In DDG take the left String combination, so move to QTS and so on


# make 3 arrays, one for both sides and one for the start line
# take 1. array and 0th element and look at the string and search for the 0th element of the correct array
# look for the found element in the 1. array und look at the string again. repeat until you find the correct element
# if the string ends, start again at the beginning of the string
def find_steps(lines):







def start(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    steps_taken = find_steps(lines)
    print(f"Total steps taken: {steps_taken}")


if __name__ == "__main__":
    filepath = '../../dateien/aoc8_1.txt'
    start(filepath)

