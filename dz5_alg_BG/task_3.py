"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
import timeit

list_with_range = [el for el in range(1000)]
deque_with_range = deque()
deque_with_range.extend(list_with_range)


def list_append(num):
    my_list = []
    for i in range(num):
        my_list.append(i)


def deque_append(num):
    my_list = deque()
    for i in range(num):
        my_list.append(i)


def list_appendleft(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def deque_appendleft(num):
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)


def list_extend(lst_range):
    my_list = []
    my_list.extend(lst_range)


def deque_extend(lst_range):
    my_list = deque()
    my_list.extend(lst_range)


def list_extendleft(lst_range):
    my_list = []
    for el in lst_range:
        my_list.insert(0, el)


def deque_extendleft(lst_range):
    my_list = deque()
    my_list.extendleft(lst_range)


def list_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def deque_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def list_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop(0)


def deque_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.popleft()


def list_reverse(lst_range):
    a = lst_range.reverse()


def deque_reverse(lst_range):
    a = lst_range.reverse()


name_list = 'list_append deque_append list_appendleft deque_appendleft list_extend deque_extend list_extendleft deque_extendleft list_pop deque_pop list_popleft deque_popleft list_reverse deque_reverse'.split()
num_time = 10000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print()
    if id <= 3:
        print(
            f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    else:
        if id % 2 == 0:
            print(
                f"{func_name}(list_with_range) -\t{timeit.timeit(stmt=func_name + f'({list_with_range})', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(
                f"{func_name}(deque_with_range) -\t{timeit.timeit(stmt=func_name + f'({deque_with_range})', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
