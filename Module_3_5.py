# Самостоятельная работа по уроку "Рекурсия"
# ***************************************************************************************
# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number
# и подсчитывает произведение цифр этого числа.
#
# Пример результата выполнения программы:
#   Исходный код:
#   result = get_multiplied_digits(40203)
#   print(result)
#   Вывод на консоль:
#   24
#****************************************************************************************

def get_multiplied_digits(number):
    if len(str(number)) == 1:
        return number
    else:
        number1 = str(number)
        #int1 = int(number1[len(number1) - 1])
        # int1 = int(number1.pop())
        # int2 = int(number1[:len(number1) - 2])
        int1 = int(number1[0])
        int2 = int(number1[1:])
        return int1 * get_multiplied_digits(int2)

print(get_multiplied_digits(40203))
