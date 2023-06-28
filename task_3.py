""" Напишите программу, которая запрашивает у пользователя три числа и выполняет следующие проверки:
Если первое число больше 100, выбросить исключение NumberOutOfRangeException с сообщением "Первое число вне допустимого диапазона".
Если второе число меньше 0, выбросить исключение NumberOutOfRangeException с сообщением "Второе число вне допустимого диапазона".
Если сумма первого и второго чисел меньше 10, выбросить исключение NumberSumException с сообщением "Сумма первого и второго чисел слишком мала".
Если третье число равно 0, выбросить исключение DivisionByZeroException с сообщением "Деление на ноль недопустимо".
В противном случае, программа должна выводить сообщение "Проверка пройдена успешно".
- необходимо создать 3 класса собвстенных исключений """


class NumberOutOfRangeException(Exception):
    pass

class NumberSumException(Exception):
    pass

class DivisionByZeroException(Exception):
    pass

def check_numbers(num1, num2, num3):
    if num1 > 100:
        raise NumberOutOfRangeException("Первое число вне допустимого диапазона")
    elif num2 < 0:
        raise NumberOutOfRangeException("Второе число вне допустимого диапазона")
    elif num1 + num2 < 10:
        raise NumberSumException("Сумма первого и второго чисел слишком мала")
    elif num3 == 0:
        raise DivisionByZeroException("Деление на ноль недопустимо")
    else:
        print("Проверка пройдена успешно")

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num3 = int(input("Введите третье число: "))
    check_numbers(num1, num2, num3)
except ValueError:
    print("Некорректный ввод")
except NumberOutOfRangeException as e:
    print(e)
except NumberSumException as e:
    print(e)
except DivisionByZeroException as e:
    print(e)
