#Задача для подсчета суммы элементов числа
import string
a = input('введите число')
for s in string.punctuation:
    a = a.replace(s, '')
sum_a = 0
for i in range(len(a)):
    sum_a += int(a[i])
print(sum_a)