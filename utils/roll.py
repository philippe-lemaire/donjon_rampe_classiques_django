import random


def roll(die_size):
    if isinstance(die_size, str):
        die = int(die_size[1:])
    else:
        die = int(die_size)

    return random.randint(1, die)
