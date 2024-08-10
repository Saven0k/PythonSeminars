#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#Какаое значение мы бы не ввели будет True

x = int(input("Введите значение числа x: "))
y = int(input("Введите значение числа y: "))
z = int(input("Введите значение числа z: "))
def True_or_False(x , y , z):
    if not(x or y or z) == ((not x) and (not y) and (not z)):
        print(True)
    else:
        print(False)

True_or_False(x , y , z)