# 22.	Найти сумму чисел списка стоящих на нечетной позиции

numbers = 1, 5, 3, 9, 7, 4


# def sum_num(numbers):
    
#     return sum(numbers[1::2]) # суммирует каждый второй элемент начиная с первого

# print(sum_num(numbers))


def sum_num(numbers):
    total = 0
    for index, element in enumerate(numbers):
            if index % 2 == 1:
                total += element
    return total
print(sum_num(numbers))





