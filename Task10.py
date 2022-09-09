#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
list = [1, 2, 3]
SumPosition = 0
list_lenght = len(list)
for i in range(list_lenght):
    if not i%2 == 0:
        SumPosition = SumPosition + list[i]
print("Summ", SumPosition)
