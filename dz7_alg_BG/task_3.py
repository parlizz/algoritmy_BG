"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import copy
import timeit
from random import randint
from statistics import median


def mediana_sort(in_list):
    temp = in_list
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


m = int(input('Введите m: '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив:\n{orig_list}\n')

print(f'Медиана - {median(orig_list)}')
print(f'Медиана (без сортировки) - {mediana_sort(orig_list)}')


print(timeit.timeit("median(orig_list[:])",
                    setup="from __main__ import orig_list, median",
                    number=10000))
print(timeit.timeit("mediana_sort(orig_list[:])",
                    setup="from __main__ import orig_list, mediana_sort",
                    number=10000))
