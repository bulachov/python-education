a = [int(i) for i in input('введите координаты первой точки пример "12,6" a=').split(',')]
b = [int(i) for i in input('введите координаты первой точки пример "7,2" b=').split(',')]
len_line = ((a[0]-b[0])**2+(a[1]-b[1])**2)**(0.5)
print(round(len_line, 3))