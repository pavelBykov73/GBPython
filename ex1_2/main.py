# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Введите трехзначное число (от 100 до 999):")
try:
    number = abs(int(input()))
except ValueError:
    print("Неверный ввод!")
    exit(-1)

if 100 <= number <= 999:
    sum_of_digit = 0
    for i in range(3):
        sum_of_digit += number % 10
        number //= 10
    print(f"Сумма цифр числа = {sum_of_digit}")
else:
    print("Число должно быть от 100 до 999")
