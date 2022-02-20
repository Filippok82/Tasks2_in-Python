# 42.	Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных файлах



def output_txt(path):
    data = open(path, 'r')

    text=str()            
    for i in data:
        text +=(str(i))
    return(text)
print(output_txt('task42_1.txt'))         
        
        
        
text=output_txt('task42_1.txt')        
def encode_rle(text):       
    count = 1
    text1=str()
    text2=str()
    for i in range(0,(len(text)-1)):
               
        if text[i] == text[i+1]:
            count += 1
            text1=str(count)+text[i]
        elif text[i]!=text[i+1]:            
            text1=str(count)+text[i]
            count = 1
            text2+=text1 
    return text2

print(encode_rle(text))



text2 = encode_rle(text)


with open('task42_2.txt','w') as data2:
    data2.write(text2)
    



#___________________________оббратно
# def decoding_rle(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(my_text2)
# print(str_decode)



