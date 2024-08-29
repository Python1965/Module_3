# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# ***************************************************************************************
# Входные данные (применение функции):
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#
# Вопрос: "А есть ли универсальное решение для подсчёта
# суммы всех чисел  и длин всех строк?"
#
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то).
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Рекомендации:
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов,
# можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.
# ****************************************************************************************

def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure, dict):
        keys = data_structure.keys()
        for key in keys:
            sum += len(key)

        values = data_structure.values()
        for val in values:
            if isinstance(val, int) or isinstance(val, float):
                sum += val
            elif isinstance(val, str):
                sum += len(val)
            else:
                sum += calculate_structure_sum(val)
    else:
        for item in data_structure:
            if isinstance(item, int) or isinstance(item, float):
                sum += item
            elif isinstance(item, str):
                sum += len(item)
            elif isinstance(item, dict):
                sum += calculate_structure_sum(item)
            else:
                for item_ in item:
                    if isinstance(item_, int) or isinstance(item_, float):
                        sum += item_
                    elif isinstance(item_, str):
                        sum += len(item_)
                    else:
                        sum += calculate_structure_sum(item_)

    return sum



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)




