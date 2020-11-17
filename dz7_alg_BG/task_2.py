"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
def list_sort(in_list):
    if len(in_list) > 1:
        mid = len(in_list) // 2
        lefthalf = in_list[:mid]
        righthalf = in_list[mid:]

        list_sort(lefthalf)
        list_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                in_list[k] = lefthalf[i]
                i += 1
            else:
                in_list[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            in_list[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            in_list[k] = righthalf[j]
            j += 1
            k += 1
n = int(input("Введите число элементов: "))
in_list = [random.random()*50 for i in range(n)]

print(f"Исходный - {in_list}")
list_sort(in_list)
print(f"Отсортированный - {in_list}")