# »: Ввести с клавиатуры координаты двух точек (A и B) на плоскости (вещественные числа). 
#Вычислить длину отрезка AB 
import math
a1=float(input("Введите a1: "))
a2=float(input("Введите a2: "))
b1=float(input("Введите b1: "))
b2=float(input("вВедите b2: "))
AB=math.sqrt((a2-a1)**2+(b2-b1)**2)
print(AB)