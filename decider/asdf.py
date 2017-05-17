s = "SPQMSQTMSQQMPXYMSPVMSSVMSQWMSQQMPWYMPVPMPWYMPRXMPRQMPWQMSQWMSSSMSQXMSPPMSRSMPYUMPYSMSPRMSSTMSRXMPPYM"
o = ord('M')^ord(',')
q = [int(x) for x in "".join([chr(o^ord(x)) for x in s])[:-1].split(',')]
n = q
for i in range(len(n)-2, -1, -1):
	n[i] = n[i] - n[i+1]
print(n)
print("".join([chr(x) for x in n]))

