# Задача 21 Нужно проверить, все ли числа в последовательности уникальны.

numbers=[1, 2, 3, 5, 1, 5, 3, 10]
unique_num=[]
 
def unique_list(numbers):
    for i in numbers:
        if numbers.count(i)==1:

            unique_num.append(i)
    return unique_num

print(unique_list(numbers))