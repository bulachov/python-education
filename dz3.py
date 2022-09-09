# 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
from random import randint

a = int(input('Введите кол-во чисел в списке for 1# = '))
list_a = list((i-i+1)*randint(0, 10) for i in range(a))
print(list_a)
sum_a = sum(list_a[i] for i in range(1, a, 2))
print(sum_a)

# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

b = int(input('Введите кол-во чисел в списке for 2# = '))
list_b = list((i-i+1)*randint(0, 10) for i in range(b))
print(list_b)
proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
print(proiz_b)

# 3 Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
print('задача 3#')
c = [1.3, 1.4, 20.1, 100.9, 3.001]
print(c)
list_c = list(round(c[i]%1, 4) for i in range(len(c)))
result_3 = max(list_c)-min(list_c)
print(f'разница между нецелой частью = {result_3}')

# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
print('задача 4#')
a = int(input('введите число для перевода = '))
b = ''
while a != 0:
    b = str(a % 2) + b
    a = a // 2
print(b)

#5 Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

fib = int(input('5# введите число for fib = '))
res_5 = []
for i in range(fib+1):
    if i==0:
        res_5.append(i)
    elif i==1:
        res_5.append(i)
        res_5.insert(0, i)
    else:
        res_5.append(res_5[len(res_5)-1]+res_5[len(res_5)-2])
        res_5.insert(0, (-1)**(i-1)*res_5[len(res_5)-1])
print(res_5)