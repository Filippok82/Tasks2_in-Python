# 30.	Вычислить число π c заданной точностью d
	# Пример: при d = 0.001,π = 3.141.10^(-1)≤d≤10^(-10) 

	# Число Пи, скажу вам братцы,
    # Легче так запоминать.
    # Три четырнадцать пятнадцать
	# Девять два, шесть пять, три пять.

# 3.1415926535



from math import pi

# n = pi
# n=float('{:.3f}'.format(n)) 
# print(n)

# Формула Бэйли — Боруэйна — Плаффа



n=100
pi = sum(1/16**k*(4/(8*k + 1) - 2/(8*k + 4) - 1/(8*k + 5) - 1/(8*k + 6)) for k in range(n))
print(f'{pi:.3f}')
