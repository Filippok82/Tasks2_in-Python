# Задача 12 Напишите программу, которая принимает имя файла и выводит его расширение. 
# Если расширение у файла определить невозможно, выбросите исключение.

import os

# name,extention=os.path.splitext('task34.txt')

# print(name)
# print(extention)

name, extention=os.path.splitext('Документ 3.docx')

print(name)
print(extention)
