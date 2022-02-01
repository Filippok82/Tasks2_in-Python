# 7.	Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def log_task(x,y,z):
    return not(x or y or z) == (not x and y and z)  

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
             print (log_task(x,y,z))  