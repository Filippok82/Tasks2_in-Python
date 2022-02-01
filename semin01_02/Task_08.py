# 8.Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 


x=float(input('Ввведите координату для x:'))
y=float(input('Ввведите координату для y:'))

def quarter_number(x,y):
    if x>0 and y>0:
        return ' первая четверть'
    elif x<0 and y>0:
        return 'вторая четверть'
    elif x<0 and y<0:
        return 'третья четверть'
    elif x>0 and y<0:
        return 'четвертая четверть'
print(quarter_number(x, y))
    