# 32.	Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.



num = [6,5,6,8,9,2,3,9,5,9]


# def unique_list(num):   # с помощью встроенной функции set
    
#     res_number= set(num) # переписываем список  в множество
#     res_num = []      # создаем новый список
#     for num in res_number:  # проходи по множеству через цикл
#         res_num.append(num)   # добавляем в новый список уникальные

#     return res_num

# print(unique_list(num))


#_________________________________________________________________


# def unique_list2(num):
#     new_list = [] 
#     for i in num: 
# 	    if i not in new_list: 
# 	        new_list.append(i) 

#     return new_list

# print(unique_list2(num))



#_____________________________________________________________


from collections import Counter # предназначен для удобных и быстрых подсчетов количества появлений 
                                # неизменяемых элементов в последовательностях.

def unique_list3(num):
    new_list=[]
    new_list = Counter(num) # хранятся в виде значений словаря например- {9: 3, 6: 2, 5: 2, 8: 1, 2: 1, 3: 1}
    # new_list = Counter(num).keys() # возвращает новый список-представление всех ключей dict_keys, содержащихся в словаре dict.
    return new_list
print(unique_list3(num))

