#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#Помогите Кате отгадать задуманные Петей числа.
#Пример:
#4 4 -> 2 2
#5 6 -> 2 3 '''
s = 12
p = 27
a = 0

for x in range(s):
    y = s - x
    if x + y == s and x * y == p:
        a += 1
        print(x, y)
        break
if a == 0:
    print('Вы ввели не корректные данные!')