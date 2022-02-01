# 23.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]


numbers = [1, 5, 3, 9, 7, 4]


# def pow_two_num(numbers):
#     result = 0
#     result1 = 0
#     result2 =0

#     for i in numbers:
#         result = numbers[0]*numbers[-1]
#         result1 = numbers[1]*numbers[-2]
#         result2= numbers[2]*numbers[-3]
#     return (result, result1, result2)


# print(pow_two_num(numbers))


def pow_two_num(numbers):
    res = []
    while len(numbers) > 1:
        res.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: res.append(numbers[0]**2)       
    return res

print(pow_two_num(numbers))