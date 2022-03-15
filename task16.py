# Задача 16 Выведите список файлов в указанной директории.


from os import listdir
from os.path import isfile, join
file = [f for f in listdir('C:\Python\Pippy2') if isfile(join('C:\Python\Pippy2', f))]
print(file)


import os
# вывести текущую директорию
print("Текущая директория:", os.getcwd())