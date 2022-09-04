x = int(input('Введите новмер четверти: '))
if x == 1:
    print('Координаты х(0;inf), y(0,inf)')
elif x == 2:
    print('Координаты х(-inf;0), y(0,inf)')
elif x == 3:
    print('Координаты х(-inf;0), y(-inf,0)')
elif x == 4:
    print('Координаты х(0;inf), y(-inf,0)')
else: print('Такой четверти нет')