x = int(input('Введите число х: '))
y = int(input('Введите число y: '))
z = int(input('Введите число z: '))
if not (x or y or z) == (not x) and (not y) and (not z):
    print(True)
else:print(False)   