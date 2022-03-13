# Задача 7 Нужно вывести первые n строк треугольника Паскаля.
#  В этом треугольнике на вершине и по бокам стоят единицы, 
# а каждое число внутри равно сумме двух расположенных над ним чисел.

n=int(input('Введите значение n: '))

def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

pascal_triangle(n)


