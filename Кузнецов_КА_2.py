from pandas import *


def decimal_to_binary(decimal_number):
    whole_part = (int(decimal_number))
    fractional_part = decimal_number - whole_part

    fractional_binary = ''
    while str(fractional_part)[0] != '1':
        fractional_part *= 2
        fractional_binary += str(fractional_part)[0]


    return bin(whole_part)[2:] + ',' + fractional_binary

x1= int(input("Введите левую границу интервала -> "))
x2 = int(input("Введите правую границу интервала -> "))

armstrong = []
razlozhenie = []


for i in range(x1, x2 + 1):
    suma = 0
    a = i
    while i > 0:
        digit = i % 10
        suma = suma + digit ** len(str(a))
        i = i // 10

    if a == suma:
        armstrong.append(a)
        raz = []
        while a > 0:
            raz.append(str(a % 10))
            a //= 10
        raz.reverse()
        a = f"^{len(str(suma))} + ".join(raz)
        a += f'^{len(str(suma))} = {suma}'
        razlozhenie.append(a)



print(armstrong)
print(razlozhenie)

if len(armstrong) > 10:
    interval = 11
else:
    interval = len(armstrong) + 1

df = DataFrame({"№ пп": range(1, interval), "Число Армстронга из интервала (х1; х2)" : armstrong[0:10], "Расчёт числа Армстронга" : razlozhenie[0:10]})

df.to_excel('laba.xlsx', index=False)

a = 1
while a != 0:
    print('Нажмите 1, чтобы вызвать первую функцию')
    print('Нажмите 2, чтобы вызвать вторую функцию')
    print("Нажмите 0, чтобы завершить работу программы")
    a = int(input("Ожидание ответа -> "))


    if a == 0:
        break

    elif a == 1:

        decimal = [float(i) for i in input('Введите числа, разделяя их точкой с запятой -> ').split(';')]

        binary = [decimal_to_binary(i) for i in decimal]

        df2 = DataFrame({"№ пп": range(1, len(decimal) + 1), "Десятичное число": decimal,
                        "Двоичное число": binary})

        df2.to_excel('laba2.xlsx', index=False)
        print(decimal)

        print(binary)

    else:

        heximal = [hex(i)[2:] for i in armstrong]

        df = DataFrame({"№ пп": range(1, interval), "Число Армстронга из интервала (х1; х2)": armstrong[0:10],
                        "Расчёт числа Армстронга": razlozhenie[0:10], "Шестнадцатеричное представление" : heximal[:10]})

        df.to_csv('laba3.csv', index=False)





#print(decimal_to_binary(a))



