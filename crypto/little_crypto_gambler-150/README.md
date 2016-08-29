# Little Crypto Gambler Writeup

The pseudorandom numbers are generated using a Linear Congruential Generator, with the parameters m,a,c,s being randomly generated.

There are several fast ways to crack them based on only a few outputs. One way to do this can be found here: http://security.stackexchange.com/a/4306


Bet 1 ~7 times and calculate the LCG parameters, then calculate the next number and bet everything.

[Solution code](https://github.com/bobacadodl/ctfx-problems/blob/master/crypto/little_crypto_gambler-150/gamble_solution.py)
