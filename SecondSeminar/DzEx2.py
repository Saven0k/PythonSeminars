#2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#*Пример:*

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#Запрещено использовать функцию factorial из библиотеки math

N = int(input("Enter  number:  "))

lst = []

Fact = 1

for number in range(1 , N+1):
    Fact = Fact * number
    lst.append(Fact)

print(lst)

'''
1 1*15
2 1*1*2
3 1*1*2*3
4 1*1*2*3*4
5 1*1*2*3*4*5
'''