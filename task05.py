# Задача 5  Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.


my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sotr_dict={}
sort_dict=sorted(my_dict, key=my_dict.get, reverse=True)[:3]

print(sort_dict)