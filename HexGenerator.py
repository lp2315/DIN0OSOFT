import random


# Randomly output a
# hex color string


def rnd_hexcode():
    x = random.randrange(0, 16777215, 1)
    x = str((hex(x))[2:])

    return str("#" + ('{:<06}'.format(x)))


# Testing

print(rnd_hexcode())
