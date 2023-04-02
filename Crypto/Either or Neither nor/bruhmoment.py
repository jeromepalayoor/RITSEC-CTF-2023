enc = [         91,         241,         101,         166,          85,192,87,188,110,164,99,152,98,252,34,152,117,164,99,162,107]
key = [ord('M')^91,ord('e')^241,ord('t')^101,ord('a')^166]
flag = ''
for i, char in enumerate(enc):
    flag += chr(char ^ key[i%4])
print(flag)