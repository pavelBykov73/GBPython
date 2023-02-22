"""
Урок 8. Работа с файлами
Решение задачи № 2
Требуется реализовать функцию longest_words(file),
которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
Протестируем функцию на файле «article.txt» со следующим содержимым:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела
"""

from datetime import datetime
import os


def print_long_word_1(file):
    """
    печать самых длинных слов в файле
    Метод 1. Через список, map & filter
    :param file: имя файла
    :return:
    """
    try:
        with open(file, "r", encoding="utf-8") as fp:
            # with open(file, "r") as fp:
            start_time = datetime.now()
            len_max_word = 0
            lst_lines = fp.readlines()
            out_list = []
            for i in lst_lines:
                for j in i.split():
                    out_list.append(j)
            len_max_word = max(map(lambda x: len(x), out_list))
            out_list = list(filter(lambda x: len(x) >= len_max_word, out_list))
            end_time = datetime.now()
            print(out_list)
            print(f"Количество слов = {len(out_list)}, длина = {len_max_word}")
            print(f"Время выполнения 1: {end_time - start_time}")
    except OSError:
        print(f"Файл {file} не найден или не возможно открыть")


def print_long_word_2(file):
    """
    печать самых длинных слов в файле
    Метод 2. Чтение файла целиком в список, обработка с накоплением длинных слов в отдельном списке
    :param file: имя файла
    :return:
    """
    out_list = []
    try:
        with open(file, "r", encoding="utf-8") as fp:
            # with open(file, "r") as fp:
            start_time = datetime.now()
            lst_lines = fp.readlines()
            len_max_word = 1
            for line in lst_lines:
                words = line.split()
                for word in words:
                    if len(word) == len_max_word:
                        out_list.append(word)
                    if len(word) > len_max_word:
                        out_list.clear()
                        out_list.append(word)
                        len_max_word = len(word)
            end_time = datetime.now()
            print(out_list)
            print(f"Количество слов = {len(out_list)}, длина = {len_max_word}")
            print(f"Время выполнения: {end_time - start_time}")
    except OSError:
        print(f"Файл {file} не найден или не возможно открыть")


def print_long_word_3(file):
    """
    печать самых длинных слов в файле
    Метод 3. Построчно с накоплением длинных слов в отдельном списке
    :param file: имя файла
    :return:
    """
    out_list = []
    try:
        with open(file, "r", encoding="utf-8") as fp:
            # with open(file, "r") as fp:
            start_time = datetime.now()
            len_max_word = 1
            end_of_file = False
            while not end_of_file:
                line = fp.readline()
                if line == '':
                    end_of_file = True
                else:
                    words = line.split()
                    for word in words:
                        if len(word) == len_max_word:
                            out_list.append(word)
                        if len(word) > len_max_word:
                            out_list.clear()
                            out_list.append(word)
                            len_max_word = len(word)
            end_time = datetime.now()
            print(out_list)
            print(f"Количество слов = {len(out_list)}, длина = {len_max_word}")
            print(f"Время выполнения: {end_time - start_time}")
    except OSError:
        print(f"Файл {file} не найден или не возможно открыть")


# input_file = input("Введите имя файла:")
input_file = "ti_monitor.txt"  # "ti_monitor.txt"  # "article.txt"
print("\nМетод 1:")
print_long_word_1(input_file)
print("\nМетод 2:")
print_long_word_2(input_file)
print("\nМетод 3:")
print_long_word_3(input_file)
