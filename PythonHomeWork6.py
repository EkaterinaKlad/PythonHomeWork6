
# # Задача 3 ДЗ 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# # *Пример:*

# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = [round((i-int(i)),2) for i in list]
# print(list)
# print(new_list)
# min = 1

# for i in new_list:
#     if (i <= min, i != 0):
#         min = i
    
# print(max(new_list))
# print(min)
# print(max(new_list) - min)



# Задача 1 ДЗ 3. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = list(map(int, input("Введите числа через пробел:\n").split()))
# print(list)
# sum = 0

# for i in range(1, len(list), 2):
#     list.append(sum)
#     sum = sum + list[i]
    
# print(f'Сумма элементов списка, стоящих на нечетных позициях, равна {sum}')



# Задача 32 ДЗ 4. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint

# list = [randint(0, 10) for i in range(10)]
# print(list)
# my_list = [i for i in list if list.count(i)==1]

# print(f"Список неповторяющихся элементов: {my_list}")



# # Задача 18 ДЗ 2. Реализуйте алгоритм перемешивания списка.

# from random import Random, randint

# N = int(input('Введите число '))
# numbers = [randint(-N,N+1) for i in range(N)]
# print(numbers)

# def smes(numbers):
#     list = numbers[:]
#     numbers_length = len(list)
#     for i in range(numbers_length):
#         index = randint(0, numbers_length - 1)
#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp
#     return list
# print(smes(numbers))

