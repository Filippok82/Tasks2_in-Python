# Задача 14 Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]
def even_elem(numbers):
    for i in numbers:
        if i == 237:
            break
        elif i % 2 == 0:
            print (i)
even_elem(numbers)


