#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


#quarter = int(input("Введите номер четверти: "))


def exercise_4(quaeter):
    if quaeter == 1:
        print("x > 0 and y > 0")
    elif quaeter == 2:
        print("x < 0 and y > 0")
    elif quaeter == 3:
        print("x < 0 and y < 0")
    elif quaeter == 4:
        print("x > 0 and y < 0")

exercise_4(quarter)