# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите любое трехзначное число: "))


first_digit = number // 100
second_digit = number // 10 % 10
firth_digit = number % 10
if 99 < number < 1000:
    print(first_digit + second_digit + firth_digit)
else:
    print("Вы ввели неверное число")
