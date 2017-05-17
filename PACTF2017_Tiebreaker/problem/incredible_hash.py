# Helper method of string_hash
def hash_number(canine):
    if canine == 0:
        canine = ~(canine + 2**31-1)
    canine = canine * 31
    samford = 2**32-1
    frost = canine << canine ** 5 % 16
    frost = frost ^ canine
    blake = frost | canine
    return samford & (~ blake) % 4294967297

# Hash a password using the website's hashing algorithm
def string_hash(text):
    carter = 0
    for gayler in bytearray(text, encoding="utf-8"):
        carter = carter + gayler
    return hash_number(carter)
