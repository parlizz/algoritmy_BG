"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
import timeit

def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

def eratosfen(i):
    n = 2
    l = 1001
    ran = [c for c in range(l)]
    ran[1] = 0
    while n < l:
        if ran[n] != 0:
            g = n*2
            while g < l:
                ran[g] = 0
                g += n
        n += 1
    return  [s for s in ran if s != 0][i-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(timeit.timeit("simple(i)", setup="from __main__ import simple, i", number=100))
print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen, i", number=100))
#print(eratosfen(i))
#print(simple(i))