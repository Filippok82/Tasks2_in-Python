# 20.	Определить, присутствует ли в заданном списке строк, некоторое число



with open('task20.txt', 'w') as a:    # Запись строк в список

    a.write('aa\n')
    a.write('52\n')
    a.write('hh\n')
    a.write('25\n')
    a.write('2\n')
    a.write('36\n')
    a.write('nok\n')



n = int(input('Введите число:'))

def coll_elemen(n,path):
    c= open(path, 'r')  # открываем для чтения список из файла называем список с
    b=str()             # объявляем переменную b строка
    for i in c:
        b +=(str(i))   #  перебираем список с и перводим в строку
    
    if b.find(str(n)) != -1: # ищем n  в строке с если нее такого символа find возвращает -1
        return True
    else:
        return False
    

print(coll_elemen(n, 'task20.txt'))



