# Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
#если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).
#Выведите yes или no соответственно.

a = 3
b = 2
c = 4

'''
if c < a * b and (c % a == 0) or (c % b == 0):

    print('yes')

else:

    print('no')

'''
def can_break_chocolate(a, b, c):
    if c <= a * b:
        if c % a == 0 or c % b == 0:
            return "yes"
        else:
            return "no"
    else:
        return "no"
result = can_break_chocolate(a, b, c)
print(result)    