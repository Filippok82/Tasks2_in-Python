# 4.	Показать первую цифру дробной части числа

# num = input('Введите дробное число: ')
# def first_num(num):
#     return num[0]
# print(first_num(num))


def first_num():
   return int(float(input('Введите число с дробной частью: '))*10 % 10)

print (first_num())

