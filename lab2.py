from lab1 import solovay_strassen_test
from random import *




def ghost(t, q):



    n = (2 ** (t-1) // q) + (2 ** (t - 1) * rand()) // q

    if n % 2 == 1:
        n += 1

    u = 0

    p = (n + u ) * q + 1

    if p > 2 ** t: 

        return ghost(t, p)


    if 2 ** (p - 1) % p == 1 and 2 ** (n + u) % p != 1:
        return p
    
    u += 2