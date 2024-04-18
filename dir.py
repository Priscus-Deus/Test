d1 = dict(zip([str(i) for i in range(1,11)], [i for i in 'abcdefghjk']))
for i in d1:
    print(i,d1[i])
print(**d1)