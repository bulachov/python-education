import math
import random
# 1 Задача для подсчета суммы элементов любого числа
# a = input('1# введите число для : ')
# sum_a = sum(int(i) for i in a if i.isdigit())
# print(sum_a)
# 2 вход число N и выдает набор произведений чисел от 1 до N
# b = int(input('2# введите число для N!: '))
# result_list = list(math.factorial(i) for i in range(1, b + 1))
# print(result_list)
# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# c = int(input('3# введите число n для $(1+1/n)^n$ : '))
# result_list3 = list((1+1/i)**i for i in range(1, c + 1))
# print(f'sum for 3# = {round(sum(result_list3), 3)}')
# 4 задайте список от -n : n и найдите произведение чисел из файла в строке которого 1 число
# d = int(input('4# n для -n - n : '))
# list_d = list(int(i) for i in range(-d, d+1))
# print(list_d)
# f = open('file_1.txt', 'r')
# result_d = 1
# for line in f:
#     line = int(line[:])
#     result_d *= list_d[(line % (d*2+1))]
# print(result_d)
# 5 реализовать перемешивание списка
f = open('file_1.txt', 'r')
list_for_shake = list(int(line[:]) for line in f)
print(list_for_shake)
for i in range(len(list_for_shake)-1):
    list_for_shake[i], list_for_shake[random.randint(i, len(list_for_shake)-1)] = list_for_shake[random.randint(i, len(list_for_shake)-1)], list_for_shake[i]
print(list_for_shake)