"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


el_1 = randint(100, 10000)
el_2 = randint(10000, 1000000)

print('Не оптимизированная функция recursive_reverse')
print(timeit("recursive_reverse(el_1)",
             setup='from __main__ import recursive_reverse, el_1', number=100))
print(timeit("recursive_reverse(el_2)",
             setup='from __main__ import recursive_reverse, el_2',
             number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_revers_n(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('Oптимизированная функция recursive_reverse')
print(timeit("recursive_reverse(el_1)",
             setup='from __main__ import recursive_reverse, el_1', number=100))
print(timeit("recursive_reverse(el_2)",
             setup='from __main__ import recursive_reverse, el_2',
             number=10000))
