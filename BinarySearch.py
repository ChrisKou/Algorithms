import sys
import random
import math

target_number = random.randint(1, 1000)
target_number_index = target_number.__index__()
minimum_number = 1
maximum_number = 1000

while True:
    guess = math.floor((minimum_number + maximum_number)/2)
    if guess == target_number:
        print(f"Search complete. The number is {target_number} at index {target_number_index}.")
        sys.exit(1)
    elif guess < target_number:
        print(f"The number {guess} is too low.")
        minimum_number = guess + 1
    elif guess > target_number:
        print(f"The number {guess} is too high.")
        maximum_number = guess - 1
