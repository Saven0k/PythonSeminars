#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.#

#Пример:
#
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21


x1 = int(input("Введите значение числа x первой точки: "))
y1 = int(input("Введите значение числа y первой точки: "))
x2 = int(input("Введите значение числа x второй точки: "))
y2 = int(input("Введите значение числа y второй точки: "))

def Distance_2D(x1 , y1 , x2 , y2):
    result = round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5 , 3)
    print(result)
Distance_2D(x1, y1, x2, y2)