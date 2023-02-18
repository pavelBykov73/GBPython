"""
ОУрок 7. Функции высшего порядка
Решение задачи № 34
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
“Пам парам”, если с ритмом все не в порядке

Ввод:

пара-ра-рам рам-пам-папам па-ра-па-да

Вывод:
Парам пам-пам
"""


def rhythm_1(s: str):
    """
    Определение ритма методом 1
    :param s: строка по правилам задания (фразы отделяются пробелами
    :return: True если ритм есть (число гласных во всех фразах одинаково)
    """
    dict_chars = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', ' '}
    len_list = list(map(lambda x: len(x), "".join(filter(lambda x: x in dict_chars, input_string)).split()))
    print(len_list)
    return min(len_list) == max(len_list)


def rhythm_2(s: str):
    """
    Определение ритма методом 2
    :param s: строка по правилам задания (фразы отделяются пробелами
    :return: True если ритм есть (число гласных во всех фразах одинаково)
    """
    vowels = set("аеёиоуыэюя")
    phrases = input_string.split()
    len_list = list(map(lambda x: sum(letter in vowels for letter in x), phrases))
    print(len_list)
    return min(len_list) == max(len_list)


input_string = "пара-ра-рам рам-пам-папам па-ра-па-да".lower()  # input("Введите стих:")
if rhythm_2(input_string):
    print("Парам пам-пам")
else:
    print("Пам парам")