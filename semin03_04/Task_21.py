# 21.	Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.



a = ['geehhk brains','geek brains','geek brains','geek brains']

word = 'geek brains'


def  two_overlap(a, word):
    # print(a,word, sep='\n')
    count = 0
    index=0
    for i in a:        
        if word == i:
           count += 1            
        
        if count==2: 
            return f' позиция: {index}'
        index+=1
print( two_overlap(a,word))





