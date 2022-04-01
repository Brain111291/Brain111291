#import random
#x = random(1,4)
while True:
    print('Введи число 1 или 2')
    x = input()
    x = int(x)
    if x == 1:
        break
    if x == 2:
        break
if x == 1:
    print('x=1')
if x == 2:
    print('x=2')