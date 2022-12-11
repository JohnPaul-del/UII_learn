"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Ввведите год рождения А.С.Пушкина:')
#
# day = input('Ввведите день рождения Пушкин?')
# while day != '6':
#     print("Не верно")
#     day = input('В какой день июня родился Пушкин?')
# print('Верно')

def year_birthday(year):
    if year == 1799:
        print('Right!')
        _day = int(input('Enter day of birthday: '))
        day_of_birthday(_day)
    else:
        print('Wrong')
        _year = int(input('Enter Year of birthday: '))
        year_birthday(_year)


def day_of_birthday(day):
    if day == 6:
        print('Right!')
    else:
        print('Wrong')
        _day = int(input('Enter day of birthday: '))
        day_of_birthday(_day)


year_birthday(1578)
