import sys

frequency = 0
frequencies_reached = {0}
frequency_changes = []

def change_frequency(frequency_change):
    global frequency
    frequency += frequency_change
    if frequency in frequencies_reached:
        print(frequency)
        sys.exit()
    frequencies_reached.add(frequency)

with open('data.txt') as f:
    for line in f:
        frequency_change = int(line)
        change_frequency(frequency_change)
        frequency_changes.append(frequency_change)

while True:
    for frequency_change in frequency_changes:
        change_frequency(frequency_change)