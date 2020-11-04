"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib
from collections import Counter

inp_str = input('Введите строку из маленьких латинских букв: ')
s = set()

dl_str = len(inp_str)
for i in range(dl_str):
    if i == 0:
        dl_str = len(inp_str) - 1
    else:
        dl_str = len(inp_str)
    for k in range(dl_str, i, -1):
        print(inp_str[i:k])
        s.add(hashlib.sha1(inp_str[i:k].encode('utf-8')).hexdigest())
print(s)
print("Количество различных подстрок в строке '%s' равно %d" % (inp_str, len(s)))