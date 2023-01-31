# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#
# 4 4 -> 2 2
# 5 6 -> 2 3

# Можно решить уравнением или перебором

# Решаем систему уравнений
# x+y=s
# x*y=p
# из второго x=p/y
# подставляем в первое
# y+p/y=s
# Приводим к общему знаменателю
# y2+p=sy
# или
# y2-sy+p=0
# Реализация C++:
# int d=s*s-4*p;
# if(d<0)
#    cout<<"Так не бывает!";
# else
# {
#    int sd=sqrt(d);
#    y=(s+sd)/2;
#    x=s-y;
#    cout<<x<<' '<<y<<endl;
# }


from math import sqrt


def input_int_value(msg):
    input_correct = False
    while not input_correct:
        try:
            val = int(input(msg))
            input_correct = True
        except ValueError:
            print("Неверный ввод!")
            # exit(-1)
    return val


def find_result_v1(s, p):
    d = s * s - 4 * p
    if d < 0:
        return None, None
    else:
        sd = int(sqrt(d))
        y = int((s + sd) / 2)
        x = s - y
    return x, y


def find_result_v2(s, p):
    x = 0
    y = 0
    for x in range(1000):
        for y in range(1000):
            if s == x + y and p == x * y:
                return x, y
    return None, None


summ = input_int_value("Введите сумму чисел:")
product = input_int_value("Введите произведение чисел:")

x, y = find_result_v1(summ, product)
if x is None or y is None:
    print(f"Решения уравнением нет!")
else:
    print(f"Решение уравнением (может быть неточным, но наиболее близким): {x}, {y}")

x, y = find_result_v2(summ, product)
if x is None or y is None:
    print(f"Решения перебором нет!")
else:
    print(f"Решение перебором: {x}, {y}")
