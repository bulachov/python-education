path_number = input('введите номер четверти от 1 до 4 = ')
path_value = {'1': 'x > 0, y > 0',
              '2': 'x < 0, y > 0',
              '3': 'x < 0, y < 0',
              '4': 'x > 0, y < 0'}
print(f'{path_value[path_number]}')

