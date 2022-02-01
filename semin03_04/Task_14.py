# 14.	Подсчитать сумму цифр в вещественном числе.
n = input('Введите вещественное число: ')


def sum_element(n):
    b = str(n)   # перевод числа в строку
    res = 0
    for i in b:
        if i != ',':  # если i , не равно запятой  
            res += int(i) # к res прибавляется i и перевод строки в число
    return res


print(sum_element(n))
