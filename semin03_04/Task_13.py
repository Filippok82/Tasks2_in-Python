# 13.	Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.


def count_overlap(text1, text2):
    print(text1,text2, sep='\n')
    count = 0
    i = 0
    while True:
        i = text1.find(text2, i+1)
        if i ==0:
            return count
        count += 1

        
print(count_overlap('geek brains geek brains geek brains geek brains  ', 'geek'))



