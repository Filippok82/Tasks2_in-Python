#27.	Строка содержит набор чисел. Показать большее и меньшее число.Символ-разделитель - пробел

a='1 2 3 4 5 6'
def set_numbers(x):
    b = x.split(' ')
    c = [int(i) for i in b]
    a=max(c)
    d=min(c)
    return f'min={d} max={a}'
print(set_numbers(a))

