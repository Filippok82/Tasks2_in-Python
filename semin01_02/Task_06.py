# 6.Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

a=int(input('Введите число от 1 до 7:'))

def number_day(a):
    if a==6 or a==7:
        return 'Выходной'
    else:
        return 'Будни'
print(number_day(a))