import random

s = "Good Luck!"
l = []

for i in range(len(s)-1):
	l += [ord(s[i+1])+ord(s[i]),ord(',')]
l += [ord(s[-1]), ord(',')]

e = [(x^97)%256 for x in l]

random.seed()
r = random.getrandbits(32)
m = r - (((r * 0x51eb851f) >> 4) - (r >> 31)) * 50 + 1
for _ in range(m+1):
	e = [m^x for x in e]

print([chr(x) for x in e])
