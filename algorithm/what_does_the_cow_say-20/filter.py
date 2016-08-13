import sys

inp = ''.join(sys.stdin.readlines())

# filter out bad chars
inp = ''.join([c for c in inp if c.isalpha()])

# cut to length
inp = inp[:39]

print inp

