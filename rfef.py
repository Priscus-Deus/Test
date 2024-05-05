from ast import While
from math import gcd
import random
import sys



def jacobi_symbol(a, n):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a % 2 == 0: 
        if (n % 8 == 5 or n % 8 == 3):
            return (-1)*jacobi_symbol(a // 2, n) 
        else:
            return jacobi_symbol(a // 2, n)
        
    if a >= n:
        return jacobi_symbol(a % n, n)
    
    if a % 2 != 0 and n % 2 != 0: 
        return jacobi_symbol(n, a) * ((-1)**(((a - 1) // 2) * ((n - 1) // 2)))



def solovay_strassen_test(bits, t=5): 
  
    n = random.getrandbits(bits) 

    #n = 10585
    
    if n % 2 == 0:
        return print(f"{n} - четное"),0 
    
    if n <= 1:
        return print("<= 1"),0
    
    for _ in range(t):
        a = random.randint(2, n-1)
        
        if gcd(a, n) != 1:
            return print(f"{n} - составное"),0
        
        r = jacobi_symbol(a, n)
        s = pow(a, (n - 1) // 2, n)

        if r % n != s: 
             return print(f"{n} - составное"),0
        
    return f"Число {n} простое с вероятностью {round(1-pow(0.5, t), 2)}", 1



if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    
    while True:

        a, n = solovay_strassen_test(1024)  
        if n == 1:
            print(a)
            break
