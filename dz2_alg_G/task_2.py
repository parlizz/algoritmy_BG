"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
def recurs(numb, x=0, y=0):
    if numb == 0:
        return x, y
    else:
        n = numb % 10
        numb = numb // 10
        if n % 2 == 0:
            x += 1
            return recurs(numb, x, y)
        else:
            y += 1
            return recurs(numb, x, y)
try:
    a = int(input("Введите натуральное число: "))
    print(f"Количество четных и нечетных цифр в числе равно: {recurs(a)}")
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")