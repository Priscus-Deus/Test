from math import gcd
import random

def euler_phi(n): 
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p 
            result = result // p
            result = result * (p - 1)
        p += 1
    if n > 1:
        result = result // n
        result = result * (n - 1)
    return result


def jacobi_symbol(a, n):
    """
    Символ якоби - нужно жостко разобраться, как он работаем, т.к. спиздил код с интернета, 
    но можно попытаться переписать алгоритм из книжки 
    """
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a % 2 == 0:
        return jacobi_symbol(a // 2, n) * ((-1) ** ((n ** 2 - 1) // 8))
    if a >= n:
        return jacobi_symbol(a % n, n)
    if a % 4 == 3 and n % 4 == 3:
        return -jacobi_symbol(n, a)
    else:
        return jacobi_symbol(n, a)


def solovay_strassen_test(n, t=1): 
    """
    Не забыть раскомментировать штуку ниже для ввода битов!!!
    Ну и по-хорошему return не через print делать, но мне пока лень
    что-то менять... 
    """
    # n = random.getrandbits(bits) 
    # print(n)
    
    if n % 2 == 0:
        return print(f"{n} - четное") 
    
    if n <= 1:
        return print("<= 1")
    
    for _ in range(t):
        a = random.randint(2, n-1)
        
        if gcd(a, n) != 1:
            return print(f"{n} - составное")
        
        r = jacobi_symbol(a, n)
        s = pow(a, (n - 1) // 2, n)

        if r % n != s: 
             return print(f"{n} - составное")
    # Возможно вероятность считается не верно, я не перепроверял себя     
    return print(f"Число {n} простое с вероятностью {round(1-pow(euler_phi(n) / n, t), 2)}")



solovay_strassen_test(23)