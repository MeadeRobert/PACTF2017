enc = "KGZFK\\qZFG]qA\\qZFOZ"

for k in range(0, 256):
    print ''.join([chr(ord(c) ^ k) for c in enc])

    
