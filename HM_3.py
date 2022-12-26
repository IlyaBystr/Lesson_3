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


# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# arr = list(map(float, input("Введите элементы массива через пробел: ").split()))
# Array = [round(i % 1, 2) for i in arr if i % 1 != 0]
# print(max(Array) - min(Array))


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# y = int(input("Введите число: \n"))
# x = ""
# while y != 0:
#     x = str(y % 2) + x
#     y //= 2
# print(x)

# 5. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
