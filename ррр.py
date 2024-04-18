def aaa(a, b, **kwargs):
    print(a)
    print(b)
    for i in kwargs:
        print(i, "=", kwargs[i])


aaa(1, 2, c=1, f=3, j=5)
