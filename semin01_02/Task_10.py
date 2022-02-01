#10.	Найти расстояние между двумя точками пространства
# 
#  С помощью данной формулы можно рассчитать расстояние
#  между двумя точками в пространстве: AB = √ (x b — x a) 2 + (y b — y a) 2 + (z b — z a) 2 
#   
import math
def distantion_3d(x1,y1,z1,x2,y2,z2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)+ math.pow(z2-z1,2))
print(distantion_3d(1, 2, 1, 3, 3, 4))