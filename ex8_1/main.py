"""
Урок 8. Работа с файлами
Решение задачи № 1
Напишите функцию read_last(lines, file),
которая будет открывать определенный файл file
и выводить на печать построчно последние строки в количестве lines
(на всякий случай проверим, что задано положительное целое число).
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


class Queue:
    """
    Класс очереди по типу FIFO
    """

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed

    def len(self):
        return len(self.queue)


def input_value(msg, type_lambda):
    """
    Ввод числа с консоли. В случае ошибки ввода выполняется повтор
    кроме ввода пустой строки
    :param msg: сообщение приглашения ввода
    :param type_lambda: лямбда функция преобразования типа данных
    :return: None - ввод отменен, либо число
    """
    input_correct = False
    while not input_correct:
        try:
            in_str = input(msg)
            if in_str == "":
                return None
            val = type_lambda(in_str)
            input_correct = True
        except ValueError:
            print("Неверный ввод!")
    return val


def read_last(lines: int, file):
    """
    Печать последних lines строк из файла через список для всех строк файла
    :param lines: количество выводимых строк
    :param file: имя файла
    :return:
    """
    if lines < 0:
        print("Число строк не может быть отрицательным")
        return
    try:
        with open(file, "r", encoding="utf-8") as fp:
            # with open(file, "r") as fp:
            start_time = datetime.now()
            lst_lines = fp.readlines()
            for line in lst_lines[-lines:]:
                print(line.strip())
            print(f"Время выполнения: {datetime.now() - start_time}")
    except OSError:
        print(f"Файл {file} не найден или не возможно открыть")


def read_last_2(lines, file):
    """
    Печать последних lines строк из файла с минимальным требованием к памяти
    Построчное чтение файла с начала с пропусканием считанных строк через fifo
    :param lines: количество выводимых строк
    :param file: имя файла
    :return:
    """
    if lines < 0:
        print("Число строк не может быть отрицательным")
        return

    try:
        with open(file, "r", encoding="utf-8") as fp:
            # with open(file, "r") as fp:
            start_time = datetime.now()
            fifo = Queue()
            end_of_file = False
            while not end_of_file:
                line = fp.readline().strip()
                if line == '':
                    end_of_file = True
                else:
                    fifo.push(line)
                    if fifo.len() > lines:
                        fifo.pop()
            while True:
                str_val = fifo.pop()
                if str_val is None:
                    break
                print(str_val.strip())
            print(f"Время выполнения_2: {datetime.now() - start_time}")
    except OSError:
        print(f"Файл {file} не найден или не возможно открыть")


def read_last_3(lines, file):
    """
    Печать последних lines строк из файла с частичным поблочным чтением файла с конца
    Минимальное время выполнения для длинных файлов
    TODO Перебор блоков файла, если строки длинные и в одном блоке может не оказаться требуемого количества строк
    :param lines: количество выводимых строк
    :param file: имя файла
    :return:
    """
    if lines < 0:
        print("Число строк не может быть отрицательным")
        return

    try:
        with open(file, "r", encoding="utf-8") as fp:
            # with open(file, "r") as fp:
            start_time = datetime.now()
            size = fp.seek(0, os.SEEK_END)
            print(f"size={size}")
            block_length = min(1024, size)
            fp.seek(size - block_length, os.SEEK_SET)
            fifo = Queue()
            end_of_file = False
            while not end_of_file:
                line = fp.readline().strip()
                if line == '':
                    end_of_file = True
                else:
                    fifo.push(line)
                    if fifo.len() > lines:
                        fifo.pop()
            while True:
                s = fifo.pop()
                if s is None:
                    break
                print(s.strip())
            print(f"Время выполнения_3: {datetime.now() - start_time}")
    except OSError:
        print(f"Файл {file} не найден или не возможно открыть")


# input_file = input("Введите имя файла:")
input_file = "ti_monitor.txt"  # "ti_monitor.txt"  # "article.txt"
lines_to_print = input_value("Число строк для печати (с конца файла):", lambda x: int(x))
# проверим каждый из 3 методов
print("\nМетод 1:")
read_last(lines_to_print, input_file)
print("\nМетод 2:")
read_last_2(lines_to_print, input_file)
print("\nМетод 3:")
read_last_3(lines_to_print, input_file)
