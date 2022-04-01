# Это игра орел и решка 123
import random
myName = input('Здравствуй! Как тебя зовут?')
v = random.randint(1,2)
print(myName+',я подбрасываю монетку')
print('Попробуй угадать,что выпало')
print('Введи 1,если орел и 2,если решка')
n = input()
n = int(n)
if v == n:
    print('Молодец,'+myName+',ты выигал!')
if v != n:
    print('Сожалею,'+myName+',ты проиграл')
