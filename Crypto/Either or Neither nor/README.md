![image](https://user-images.githubusercontent.com/63996033/229368689-f80c5c4e-b884-47cd-8c23-1bddd8a3c396.png)

[Link](https://metaproblems.com/6ebee70f0d78d94a4750f9cb70031965/chal.py)

`chall.py:`
```py
#! /usr/bin/env python

flag = "XXXXXXXXXXXXXXXXXXXXX"
enc_flag = [91,241,101,166,85,192,87,188,110,164,99,152,98,252,34,152,117,164,99,162,107]

key = [0, 0, 0, 0]
KEY_LEN = 4

# Encrypt the flag
for idx, c in enumerate(flag):
    enc_flag = ord(c) ^ key[idx % len(key)]

```

Since we know that the first 4 characters of the flag is `Meta`, we can reverse engineer the key since a^b=c => a^c=b

```py
enc = [         91,         241,         101,         166,          85,192,87,188,110,164,99,152,98,252,34,152,117,164,99,162,107]
key = [ord('M')^91,ord('e')^241,ord('t')^101,ord('a')^166]
flag = ''
for i, char in enumerate(enc):
    flag += chr(char ^ key[i%4])
print(flag)

>>> MetaCTF{x0r_th3_c0re}
```

[Solve script](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Crypto/Either%20or%20Neither%20nor/solve.py)

Flag: `MetaCTF{x0r_th3_c0re}`
