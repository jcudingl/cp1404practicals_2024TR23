import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_IN_A_LINE = 6


while True:
    try:
        number_of_quick_pick = int(input("How many quick picks? "))
        if number_of_quick_pick > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input, please enter a number.")

for row in range(number_of_quick_pick):
    line = []
    while len(line) < NUMBER_IN_A_LINE:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in line:
            line.append(number)
    quick_pick = sorted(line)
    print("".join(f"{number:2} " for number in quick_pick))
