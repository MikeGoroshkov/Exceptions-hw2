""" Напишите программу, которая запрашивает у пользователя число и проверяет, 
является ли оно положительным. Если число отрицательное или равно нулю, 
программа должна выбрасывать исключение InvalidNumberException с сообщением 
"Некорректное число". В противном случае, программа должна выводить сообщение
 "Число корректно". """

class InvalidNumberException(Exception):
    pass

def check_positive_number(num):
    if num <= 0:
        raise InvalidNumberException("Некорректное число")
    else:
        print("Число корректно")

try:
    num = int(input("Введите число: "))
    check_positive_number(num)
except ValueError:
    print("Некорректный ввод")
except InvalidNumberException as e:
    print(e)


