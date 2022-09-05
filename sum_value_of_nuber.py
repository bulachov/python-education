#Задача для подсчета суммы элементов числа

a = input('введите число')
sum_a = sum(int(i) for i in a if i.isdigit())
print(sum_a)
