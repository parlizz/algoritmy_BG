"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile

length = 800


@profile
def recursion(length):
    def sum_series_numbers(n, elem=1):
        if n <= 0:
            return 0
        return elem + sum_series_numbers(n - 1, -elem / 2)

    print(
        f'Сумма последовательности из {length} элементов равна {sum_series_numbers(length)}')


@profile
def for_in(length):
    elem = 1
    amount = 0
    for i in range(length):
        amount += elem
        elem = -elem / 2
    print(f'Сумма последовательности из {length} элементов равна {amount}')


for_in(length)
recursion(length)
"""
Рекурсия более требовательна к выделенной памяти, так как при ее работе требуется выделения стека для храения вызываемых функций
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19     29.5 MiB     29.5 MiB           1   @profile
    20                                         def for_in(length):
    21     29.5 MiB      0.0 MiB           1       elem = 1
    22     29.5 MiB      0.0 MiB           1       amount = 0
    23     29.5 MiB      0.0 MiB         801       for i in range(length):
    24     29.5 MiB      0.0 MiB         800           amount += elem
    25     29.5 MiB      0.0 MiB         800           elem = -elem / 2
    26     29.5 MiB      0.0 MiB           1       print(f'Сумма последовательности из {length} элементов равна {amount}')

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     9     29.5 MiB     29.5 MiB           1   @profile
    10                                         def recursion(length):
    11     30.7 MiB      1.1 MiB         802       def sum_series_numbers(n, elem=1):
    12     30.7 MiB      0.1 MiB         801           if n <= 0:
    13     30.7 MiB      0.0 MiB           1               return 0
    14     30.7 MiB      0.0 MiB         800           return elem + sum_series_numbers(n - 1, -elem / 2)
    15     30.7 MiB      0.0 MiB           2       print(
    16     30.7 MiB      0.0 MiB           1           f'Сумма последовательности из {length} элементов равна {sum_series_numbers(length)}')
"""