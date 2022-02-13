# 17.	Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

with open('task17.txt', 'w') as a:
    a.write('1\n')
    a.write('2\n')
    a.write('8\n')
    a.write('10\n')
    

a = open('task17.txt','r')

n = int(input('Введите число n: '))

def elements(n):
    b = [i for i in range(-n, n + 1)]
    return b
print(elements(n))

s = elements(n)
def composition(a,b):
    result=1
    for i in a:
        result=result*b[int(i)]
    return result
    a.close()
print (composition(a,s))






