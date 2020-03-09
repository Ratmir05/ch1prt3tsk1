'''chisla = input('vvedite chisla 1:2:3').split(':')
chisla = int(chisla[0])+int(chisla[1])+int(chisla[2])
print(chisla)'''

def summ():
    num1 = int(input('1 chislo'))
    num2 = int(input('2 chislo'))
    num3 = int(input('3 chislo'))
    return f'rezultat {num1+num2+num3}'
print(summ())