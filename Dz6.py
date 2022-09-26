#1 Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
list_numb = [1, 2, 3, 5, 1, 5, 3, 10]
list_result = [list_numb[i] for i in range(len(list_numb)) if list_numb[i] not in list_numb[list_numb[i]:]]
print(list_result)
list_result1 = list(filter(lambda x: x not in list_numb[x:], list_numb))
print(list_result1)
list_result2 = list(filter(lambda x: list_numb.count(x)==1, list_numb))
print(list_result2)
