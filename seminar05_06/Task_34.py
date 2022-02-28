# 34.	Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.


# # _______________________Создание файла  task34.txt_________пригодится______________

# # __________________определение степени _________________________
# k=3
# step=[]
# def degree_selection34(k):

#     for i in range(1,k+1):
#         step.append(i)
#     return step

# print(degree_selection34(k))

# #_________________определение коэффициентов_______________________________________

# from random import randint

# numbers=[]
# def select_coefficient34(k):
#     for i in range(0,k+1):
#         numbers.append(randint(1, 100))
#     return numbers
# print(select_coefficient34(k))

# #______________________формирование многочлена____________________________________________________________

# def polinom34(step_k,numbers):
#     return f'{numbers[0]}*x^{step[2]}+{numbers[1]}*x^{step[1]}+{numbers[2]}*x+{numbers[3]} = 0'

# print(polinom34(step, numbers))


# with open('task34.txt', 'w') as file_data:
#      file_data.write(polinom34(step,numbers))


# #______________________________________________________________________________________


# data1 = open('task34_1.txt', 'r')
# data2 = open('task34_2.txt', 'r')
# pol1 = data1.readline().replace(' ', '')
# pol2 = data2.readline().replace(' ', '')
# data1.close()
# data2.close()
# print(pol1)
# print(pol2)
# x = int(input('введите x: '))
# result = sum(f'{pol1}+{pol2}')

# res_file = open('task34_3.txt', 'w', encoding="UTF-8")
# res_file.write(f'при x = {x} \n{pol1}+{pol2} = {result}')
# res_file.close()


# решение с функцией eval ____________________________________


data1 = open('task34_1.txt', 'r')
data2= open('task34_2.txt', 'r')

pol1 = data1.readline().replace(' ', '')
pol2 = data2.readline().replace(' ', '')
data1.close()
data2.close()
print(pol1)
print(pol2)
x = int(input('введите x: '))
result = eval(f'{pol1}+{pol2}')

res_file = open('task34_3.txt', 'w',encoding="UTF-8")
res_file.write(f'при x = {x} \n{pol1}+{pol2} = {result}')
res_file.close()
