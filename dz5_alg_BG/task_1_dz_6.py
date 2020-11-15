"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import sys
from memory_profiler import profile


@profile
def func():
    a = list(range(10000))

    min_num = a[0]
    min_num2 = a[1]

    if min_num > min_num2:
        min_num, min_num2 = min_num2, min_num

    for i in range(len(a)):
        if a[i] < min_num:
            min_num2 = min_num
            min_num = a[i]
        elif a[i] < min_num2:
            min_num2 = a[i]

    print("Два наименьших элемента:", min_num, min_num2)
    print(f"Два наименьших элемента: {min_num}, {min_num2}")


func()

b = sys.platform
c = sys.version
print(f'разрядность вашей ОС: {b}')
print(f'версия Python: {c}')

"""
выделено памяти: 29.5 MiB
на создание списка 0.3 MiB


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     29.5 MiB     29.5 MiB           1   @profile
    21                                         def func():
    22     29.8 MiB      0.3 MiB           1       a = list(range(10000))
    23                                         
    24     29.8 MiB      0.0 MiB           1       min_num = a[0]
    25     29.8 MiB      0.0 MiB           1       min_num2 = a[1]
    26                                         
    27     29.8 MiB      0.0 MiB           1       if min_num > min_num2:
    28                                                 min_num, min_num2 = min_num2, min_num
    29                                         
    30     29.8 MiB      0.0 MiB       10001       for i in range(len(a)):
    31     29.8 MiB      0.0 MiB       10000           if a[i] < min_num:
    32                                                     min_num2 = min_num
    33                                                     min_num = a[i]
    34     29.8 MiB      0.0 MiB       10000           elif a[i] < min_num2:
    35     29.8 MiB      0.0 MiB           1               min_num2 = a[i]
    36                                         
    37     29.8 MiB      0.0 MiB           1       print("Два наименьших элемента:", min_num, min_num2)
    38     29.8 MiB      0.0 MiB           1       print(f"Два наименьших элемента: {min_num}, {min_num2}")


разрядность вашей ОС: darwin
версия Python: 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)]

"""
