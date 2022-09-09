#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list = [1.1, 1.2, 3.1, 5, 10.01]
list_1 = []
n = len(list)
list_fraction = 0
for i in range(n):
    list_fraction = list[i] - int(list[i])
    list_1.append(list_fraction)
    print(list_1)
print(max(list_1) - min(list_1))    