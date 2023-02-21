
# Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
#  Sendo que o raio é passado por parâmetro.

def  volume_esfera (raio):
    return (4 * 3.1416 * raio ** 3) /3

raio1 = float (input("DIGITE O RAIO: "))
print ('%.2f' % volume_esfera(raio1))



#ok