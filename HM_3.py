# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# number = int(input('Введите размер массива '))
# arr = []
# sum = 0
# for i in range(number):
#      arr_number = int(input(f'Введите элемент {i+1} '))
#      arr.append(arr_number)
#      if i % 2 == 0:
#          sum += arr[i]
# print(arr)
# print(f'Сумма нечетных чисел равна {sum}')

# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint
# number = int(input('Введите размер массива '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)