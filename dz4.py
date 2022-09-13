import random

# 1 вычислить число пи с указанной точностью после запятой
a = int(input('введите нужную точность 1#= '))
pi_target = 0
for i in range(1, 1000000):
    pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
print(str(pi_target)[:a + 2])

# 2 Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

b = int(input('введите число для анализа 2#= '))


def issimple(trget):
    z = 2
    while trget % z != 0:
        z += 1
    return trget == z


def analys_targ(x, res='') -> str:
    if -1 < x < 1:
        raise ValueError("Not quadratic equation")
    else:
        count = 2
        while count <= x:
            if x % count == 0 and issimple(count):
                res = res + ' ' + str(count)
            count += 1
        return res

list_b = analys_targ(b)[1:].split()
print(list_b)

# 3 Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся
# элементов исходной последовательности.

c = int(input('введите число длины последовательности 3# = '))
list_c = list(random.randint(1, 10) for _ in range(1, c + 1))
print(list_c)
c_1 = set(list_c).copy()
print(list(set(list_c).intersection(c_1)))


# 4 Задана натуральная степень k=2.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k=2.

def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res


def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res


f = open('dz40.txt', 'w')
f.write(nmnogochlen1())
print(nmnogochlen1())
f.close()

f = open('dz41.txt', 'w')
f.write(nmnogochlen2())
print(nmnogochlen2())
f.close()

# 5 Даны два файла, в каждом из которых
# находится запись многочлена.
# Задача - сформировать файл,
# содержащий сумму многочленов.

f = open('dz40.txt', 'r')
list_5 = str(f.readline()).split('x')
c1 = b1 = a1 = 0
if len(list_5) == 3:
    c1 = list_5[2][1:]
if len(list_5) >= 2:
    b1 = list_5[1][3:-1]
a1 = list_5[0][:-1]
f.close()

f = open('dz41.txt', 'r')
list_51 = str(f.readline()).split('x')
c2 = b2 = a2 = 0
if len(list_51) == 3:
    c2 = list_51[2][1:]
if len(list_51) >= 2:
    b2 = list_51[1][3:-1]
a2 = list_51[0][:-1]
f.close()

f = open('dz42.txt', 'w')
f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
f.close()
