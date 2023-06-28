""" Напишите программу, которая запрашивает у пользователя два числа и 
выполняет их деление. Если второе число равно нулю, программа должна 
выбрасывать исключение DivisionByZeroException с сообщением "Деление на ноль недопустимо". 
В противном случае, программа должна выводить результат деления. """


class DivisionByZeroException(Exception):
    pass

def divide_numbers(num1, num2):
    if num2 == 0:
        raise DivisionByZeroException("Деление на ноль недопустимо")
    else:
        print(f"Результат деления: {num1 / num2}")

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    divide_numbers(num1, num2)
except ValueError:
    print("Некорректный ввод")
except DivisionByZeroException as e:
    print(e)
