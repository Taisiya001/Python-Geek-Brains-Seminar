x = int(input('Введите коррдинату х первой точки: '))
y = int(input('Введите координату y второй точки: '))
if x > 0 and y > 0:
    print('Точка находится в первой четверти')
elif x <0 and y > 0:
    print('Точка находится во второй четверти')
elif x > 0 and y < 0:
    print('Точка находится в третье четверти')
elif x > 0 and y < 0:
    print('Точка находится вчетвертой четверти')
elif x == 0 and y == 0:
    print('Введите другие значения, отличные от нуля')