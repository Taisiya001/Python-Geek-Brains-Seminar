#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = [1, 2, 3, 4, 5]
ProductNumber = 0
list_lenght = len(list)
for i in range(list_lenght):
    x = list_lenght-i
    ProductNumber = list[i]*list[x-1]
    print(ProductNumber, end= ' ')
    
    
