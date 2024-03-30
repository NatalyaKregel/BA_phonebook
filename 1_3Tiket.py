# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
#и получали билет с номером.
#Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех.
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#Вам требуется написать программу, которая проверяет счастливость 
#билета с номером n и выводит на экран yes или no.

n = 385916

# Введите ваше решение ниже
'''
#n = input('Введите 6-значный номер билета: ')
if len(n) != 6:
    print(f'Число {n} не 6-ти значное')
else:
    res1 = 0
    res2 = 0
    for i in range(len(n)//2):
        res1 += int(n[i])
        res2 += int(n[len(n)//2 + i])
    if res1 == res2:
        print(f'{n} -> yes')
    else:
        print(f'{n} -> no')
'''


d = list(map(int, list(f'{n:06}')))
print(('no', 'yes')[sum(d[:3])==sum(d[3:])])