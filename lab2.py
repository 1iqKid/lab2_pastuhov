import math
print('==Типы нагрузки, значение cos==')
print('Активная, cos = 1.0 ')
print('Индуктивная, cos = 0.85')
print('Смешанная, cos = 0.75')
vvod = input('введите тип нагрузки: ')
match vvod:
    case 'активная':
        cos = 1.0
    case 'индуктивная':
        cos = 0.85
    case 'смешанная':
        cos = 0.75
    case _:
        print('значение не поддерживается')

f = True

while f:
    try:
        U = int(input('введите значение напряжения в В: '))
        if U >= 12 and U <= 1000:
            f = False
        else:
            print('недопустимое значение, значение В должно быть от 12 до 1000')
    except ValueError:
        print('ошибка, введите число')

f = True

while f:
    try:
        I = float(input('введите значение тока в А: '))
        if I >= 0.1 and I <= 500:
            f = False
        else:
            print('недопустимое значение, значение А должно быть от 0,1 до 500')
    except ValueError:
        print('ошибка, введите число')

raschet = (U * I * cos)/1000 
if U < 220:
    Vivod = 'низкое напряжение'
if 220 <= U <= 400:
    Vivod = 'нормальное напряжение'
if U > 400: 
    Vivod = 'высокое напряжение'


print(f'тип нагрузки: {vvod}')
print(f'значение cos: {cos}')
print(f'{raschet} кДж')
print(f'класс напряжения: {Vivod}')


