
# Faça uma função que receba dois números e retorne qual deles é o maior.

from time import sleep


def maior (*num):
    cont = maior = 0
    print ('-='*30)
    print ("valores informados..")
    for valor in num:
       
        print(f'{valor}', end='' , flush=True)
        sleep (0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
        print ('<')
    print(f'\nO maior valor foi {maior}')

maior (2 , 28)

# OK