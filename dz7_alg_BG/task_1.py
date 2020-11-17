"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
import timeit


def bubble_sort(original):
    n = 1
    while n < len(original):
        for i in range(len(original) - n):
            if original[i] < original[i + 1]:
                original[i], original[i + 1] = original[i + 1], original[i]
        n += 1
    return original


def bubble_sort_new(original):
    n = 1
    k = 0
    while n < len(original):
        for i in range(len(original) - n):
            if original[i] < original[i + 1]:
                original[i], original[i + 1] = original[i + 1], original[i]
                k = 1
        if k == 0:
            break
        n += 1
    return original


original = [random.randint(-100, 100) for i in range(1000)]

print(timeit.timeit("bubble_sort(original[:])",
                    setup="from __main__ import bubble_sort, original",
                    number=100))
print(timeit.timeit("bubble_sort_new(original[:])",
                    setup="from __main__ import bubble_sort_new, original",
                    number=100))

"""
rezult:
8.221140104
8.347679404
оптимизация не дала особого сокращения времени, а наоборот увеличилась
"""
