# 12.	Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.

from random import randint
n = randint(3, 10)
print(n)
def index_meaning(n):
    return {x: 3 * x + 1 for x in range(n)}

print (index_meaning(n))
