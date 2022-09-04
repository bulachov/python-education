day_value = int(input('please press number your day : '))
if day_value % 7 == 0 or day_value % 7 == 6:
    print('this day is weekend')
else:
    print('go work')
