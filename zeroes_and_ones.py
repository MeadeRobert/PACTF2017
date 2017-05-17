

def roll_right(size, bits, value):
    for i in range(0, abs(bits)):
        if bits > 0:
            value = (value % 2 << (size - 1)) + (value >> 1)
        else:
            value = (value >> (size - 1)) + (value << 1) % pow(2, size)
    return value


def expression(x):
    value = roll_right(5, -3, 0b01011 and x or 0b10100)
    print value
    return value == 0b01101


print bin(roll_right(6, -2, 0b011101))

for x in range(0, pow(2, 5)):
    print expression(x)
