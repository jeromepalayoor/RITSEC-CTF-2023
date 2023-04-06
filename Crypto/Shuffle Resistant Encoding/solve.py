freq = {}

with open('encoded.txt', 'r') as f:
    enc = f.read().strip()

for c in enc:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

a = [' ']*100

for c, f in freq.items():
    a[f] = c

print(''.join(a))
