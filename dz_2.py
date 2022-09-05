import math
# 1 Задача для подсчета суммы элементов любого числа
a = input('1# введите число для : ')
sum_a = sum(int(i) for i in a if i.isdigit())
print(sum_a)
# 2 вход число N и выдает набор произведений чисел от 1 до N
b = int(input('2# введите число для N!: '))
result_list = list(math.factorial(i) for i in range(1, b + 1))
print(result_list)
# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
c = int(input('3# введите число n для $(1+1/n)^n$ : '))
result_list3 = list((1+1/i)**i for i in range(1, c + 1))
print(f'sum for 3# = {round(sum(result_list3), 3)}')
