# 38.	Напишите программу, удаляющую из текста все слова содержащие "абв".

# from functools import reduce
# str='рапааисим фбварара абвгдх ваабвгр'
# print(str)
# str=str.split('абв')
# str = reduce(lambda x,y: x+y ,[i for i in str])
# print(str)


#________________________________________________________________

text='рапааисим фбварара абвгдх ваабвгр'
print(text)
tex=text.split()
print(tex)
# for word in tex[:]:
#     if 'абв' in word:
#         tex.remove(word)
[tex.remove(word) for word in tex[:] if 'абв'in word]
print(tex)


        