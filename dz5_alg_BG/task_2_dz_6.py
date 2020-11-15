"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки)
оптимизации и
доказать (наглядно, кодом) их эффективность
"""
from memory_profiler import profile


@profile
def simple(i):
    """Наивный алгоритм"""
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


@profile
def eratosfen(i):
    """Решето Эратосфена"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1


    return [p for p in sieve if p != 0][i-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(eratosfen(i))

"""
выделено памяти 29.5 MiB
оптимизация не требуется, так как инкримент находится в рамках нормы

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    10     29.5 MiB     29.5 MiB           1   @profile
    11                                         def simple(i):
    13     29.5 MiB      0.0 MiB           1       count = 1
    14     29.5 MiB      0.0 MiB           1       n = 2
    15     29.5 MiB      0.0 MiB          10       while count <= i:
    16     29.5 MiB      0.0 MiB          10           t = 1
    17     29.5 MiB      0.0 MiB          10           is_simple = True
    18     29.5 MiB      0.0 MiB          44           while t <= n:
    19     29.5 MiB      0.0 MiB          39               if n % t == 0 and t != 1 and t != n:
    20     29.5 MiB      0.0 MiB           5                   is_simple = False
    21     29.5 MiB      0.0 MiB           5                   break
    22     29.5 MiB      0.0 MiB          34               t += 1
    23     29.5 MiB      0.0 MiB          10           if is_simple:
    24     29.5 MiB      0.0 MiB           5               if count == i:
    25     29.5 MiB      0.0 MiB           1                   break
    26     29.5 MiB      0.0 MiB           4               count += 1
    27     29.5 MiB      0.0 MiB           9           n += 1
    28     29.5 MiB      0.0 MiB           1       return n

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     29.5 MiB     29.5 MiB           1   @profile
    32                                         def eratosfen(i):
    34     29.5 MiB      0.0 MiB           1       n = 2
    35     29.5 MiB      0.0 MiB           1       l = 10000
    36     29.9 MiB      0.4 MiB       10003       sieve = [x for x in range(l)]
    37     29.9 MiB      0.0 MiB           1       sieve[1] = 0
    38     29.9 MiB      0.0 MiB        9999       while n < l:
    39     29.9 MiB      0.0 MiB        9998           if sieve[n] != 0:
    40     29.9 MiB      0.0 MiB        1229               m = n*2
    41     29.9 MiB      0.0 MiB       24298               while m < l:
    42     29.9 MiB      0.0 MiB       23069                   sieve[m] = 0
    43     29.9 MiB      0.0 MiB       23069                   m += n
    44     29.9 MiB      0.0 MiB        9998           n += 1
    45                                         
    46                                         
    47     29.9 MiB      0.0 MiB       10003       return [p for p in sieve if p != 0][i-1]
"""