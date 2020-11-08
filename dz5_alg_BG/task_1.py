"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import deque


def calc():
    company = int(input("Введите количество предприятий: "))
    company_lst = []
    for i in range(company):
        company_new = dict(
            name=input(f"Введите наименование предприятия {i + 1}: "),
            qp=deque(),
            q_sum=0.0
        )
        for qn in range(1, 5):
            company_new['qp'].append(
                float(
                    input(
                        f"Введите доход предприятия {i + 1} за {qn} квартал: ")
                )
            )
        company_new['q_sum'] = sum(company_new['qp'])
        company_lst.append(company_new)
        print("-" * 5)
    avg = sum([i.get('q_sum', 0.0) for i in company_lst]) / company
    print(f"Предприятия с общей прибылью выше среднего (среднее = {avg:.2f}):",
          ", ".join(
              [f"{i.get('name')} ({i.get('q_sum')})" for i in company_lst if
               i.get('q_sum', 0.0) > avg]))

    print(f"Предприятия с общей прибылью ниже среднего (среднее = {avg:.2f}):",
          ", ".join(
              [f"{i.get('name')} ({i.get('q_sum')})" for i in company_lst if
               i.get('q_sum', 0.0) < avg]))


calc()