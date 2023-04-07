![image](https://user-images.githubusercontent.com/63996033/230646432-12f13f5b-f04b-4ac3-8079-0a132fb97c44.png)

[bitmap.bmp](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Steganography/bitmap/bitmap.bmp)

Solution:
```
weird band of pixels at the bottom of the image

converted the hex values and got:
b3bdff b9a8b0 b7acb6 bab4a0 d8c2a6 b6ada0 baacab d8a0bc dfdfdf a9b6df bdd8c2 
a8b0b3 acb6b9 dfd8b7 dfdfdf bbb0b2 bcc2ba dfbcbd dfdfdf c2b1b6 a7bab7 dfdfdf 
aab0df b7c2ab dfa7ba dfdfdf afb6bc adbab7 acaad7 b6dfba b7dfb1 d6a7ba 9bd8c2 
f5a4bb 404ed4 27655a d809ca 63b29e 1d4c2e 047bac 522ff3 d368b6 ed5ce5 ffd8ff

also found second band in lower left half:
580000 20524f 205942 464627 000027

decode second band in little endian of 3 byte word lengths, and you get:
XOR BY 'FF'

using this, xor first message by FF and do the same little endian with 3 bytes:
BLOWFISH_KEY='_RITSEC_'    IV='BLOWFISH'    MODE=CBC    IN=HEX    OUT=HEX    CIPHER(USE IN HEX)='dD[

then using these configs, decrypt blowfish for the bytes after cipher(use in hex):
64 44 5b 0a 2b b1 bf a5 9a d8 35 f6 27 61 4d 9c d1 b3 e2 53 84 fb 0c d0 ad 49 97 2c 1a a3 12 00
```

Flag: `RS{CONSIDER_THESE_BITS_MAPPED}`
