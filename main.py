reset_color = "\033[0m"
magenta = "\033[1;35;40m"

def imc(peso, altura):
    return peso / altura ** 2

print(magenta +'Vamos calcular o seu IMC!\n'+ reset_color)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

resultado = '%.2f' % (imc(peso, altura))

if imc(peso, altura) < 17:
    print(resultado,'Muito abaixo do peso')
elif 17 <= imc(peso, altura) < 18.5:
    print(resultado,'Abaixo do peso')
elif 18.5 <= imc(peso, altura) < 25:
    print(resultado,'Peso normal')
elif 25 <= imc(peso, altura) < 30:
    print(resultado,'Acima do peso')
elif 30 <= imc(peso, altura) < 35:
    print(resultado,'Obesidade I')
elif 35 <= imc(peso, altura) < 40:
    print(resultado,'Obesidade II (severa)')
else:
    print(resultado,'Obesidade III (mórbida)')
