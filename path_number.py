x = int(input('введите параметр координаты х кроме 0 = '))
y = int(input('введите параметр координаты y кроме 0 = '))
if x > 0 and y > 0:
    print('1st path')
elif x < 0 and y > 0:
    print('second path')
elif x < 0 and y < 0:
    print('3th path')
elif x > 0 and y < 0:
    print('4th path')
else:
    print('придется повторить исключи 0')