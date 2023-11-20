
def fibonacci(n):
    '''
    Напишите функцию для расчёта чисел Фибоначчи
    Числа Фибоначчи - элементы числовой последовательности, в которой первые два числа равны 0 и 1, а каждое последующее
    число равно сумме двух предыдущих чисел (0, 1, 1, 2, 3, 5, 8, 13 и т.д)
    '''
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


input = {1:{2:{3:{4:{5:10}}}},6:5}
def dict_sum(input, first_sum = 0):
    '''
    Цель задания — научиться использовать словарь в Python
    Дан словарь произвольной вложенности вида:
    input = {1:{2:{3:{4:{5:{…}}}}}}
    Разработайте функцию, вычисляющую сумму всех значений этого словаря.
    '''
    for key, value in input.items():
        if isinstance(value, int):
            first_sum += value
        else:
            first_sum += dict_sum(value)

    return first_sum

print(dict_sum(input))