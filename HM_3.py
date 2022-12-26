# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

number = int(input('Введите размер списка '))
arr = []
sum = 0
for i in range(number):
     arr_number = int(input(f'Введите число {i+1} '))
     arr.append(arr_number)
     if i % 2 == 0:
         sum += arr[i]


print(arr)
print(f'Сумма нечетных чисел равна {sum}')