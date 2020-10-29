"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""
def revers_numb(numb, y=0):
    if numb == 0:
        return y
    else:
        y = (y * 10) + (numb % 10)
        numb = numb // 10
        return revers_numb(numb, y)
try:
    a = int(input("Введите натуральное число: "))
    print(f"Количество четных и нечетных цифр в числе равно: {revers_numb(a)}")
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")