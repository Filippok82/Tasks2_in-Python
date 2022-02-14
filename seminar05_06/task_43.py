# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

numbers=[1, 2, 3, 5, 1, 5, 3, 10]
unique_num=[]
 
def unique_list(numbers):
    for i in numbers:
        if numbers.count(i)==1:
            unique_num.append(i)
    return unique_num

print(unique_list(numbers))