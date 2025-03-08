import numpy as np 
test_number=np.random.rand(2,5)
number = np.random.randint(1,50)

"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

count = 0
# Запускаем цикл, чтобы угадать число
while True:
    count += 1
    my_number = int(input('Введите натуральное число ')) 
    
    if my_number == number:
        print('Вы угадали число: {} с {} раза(а)'.format(number,count))
        break
        
    elif my_number > number:
        print('Искомое число меньше')
        
    elif my_number < number:
        print('Искомое число больше')