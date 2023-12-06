# Find the numbers of possible ways to beat the record
# for 1 milisec of charge the boat travels +1mm/s
# release the button and the boat travels the remaining distance with the current speed
from numpy.compat import long
from tqdm import tqdm
import numpy as np

def find_travel_time(time, distance):
    solutions = 0
    for i in tqdm(range(time)):
        speed = i
        distance_travelled = speed * (time-i)
        if distance_travelled > distance:
            solutions += 1
    return solutions


def find_travel_time_optimized(time, distance):
    speeds = np.int64(np.arange(time))
    times = np.int64(time - np.arange(time))
    distances_travelled = speeds * times  # Berechnet die zurückgelegten Entfernungen für alle Geschwindigkeiten
    solutions = np.sum(distances_travelled > distance)  # Zählt, wie oft die zurückgelegte Entfernung die Distanz übertrifft
    return solutions


#number1 = find_travel_time(34, 204)
#number2 = find_travel_time(90, 1713)
#number3 = find_travel_time(89, 1210)
#number4 = find_travel_time(86, 1780)
#number_aufgabe_6_2 = find_travel_time(34908986, 204171312101780)
number2_aufgabe_6_2 = find_travel_time_optimized(34908986, 204171312101780)

#print(f"number: {number1}, number2: {number2}, number3: {number3}, number4: {number4}")
#final_number = number1 * number2 * number3 * number4
#print(f"final_number: {final_number}")
#print(f"number_aufgabe_6_2: {number_aufgabe_6_2}")
print(f"number2_aufgabe_6_2: {number2_aufgabe_6_2}")