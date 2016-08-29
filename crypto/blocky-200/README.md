# Blocky Writeup

We are provided with [blocky.py](https://github.com/bobacadodl/ctfx-problems/blob/master/crypto/blocky-200/blocky.py) and the encrypted flag.


Upon examination of the code, this is a block cipher with a block size of 5. 

We know that flag starts with 'ctf(', so we can generate 256 possibilities for the Initialization Vector.

We then reverse the encryption algorithm in z3, and try decrypting the 2nd block with all the IV possibilties. 
Only 1 results in a seemingly legitimate ascii printable decryption, so we know the correct IV
Then simply decrypt each block with that initialization vector

See [blocky_sol.py](https://github.com/bobacadodl/ctfx-problems/blob/master/crypto/blocky-200/blocky_sol.py) for code
