![image](https://user-images.githubusercontent.com/63996033/230408406-de7901b4-9ada-438f-9112-2553c988d9a9.png)

[encoded.txt]()

This is likely a frquency related challenge where the flag is dependent on the number of times that character has appeared in the encoded.txt.

Solution:
```py
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

>>>  +|>b5BhawA`l^T87to&;6j-/"%?'v!f:gRS{FrEQU3NcY_m0De}#sz=<@[dCW,H2LO(Kk X\IV1$.J)Mqnp~ZGP4yi*]x9
```

[solve.py]()

Flag: `RS{FrEQU3NcY_m0De}`
