# entrada
#ler um numero
#se for igual a 1. Entrou com valor 1.
#se for igual a 2. Entrou com valor 2.
#se for menor que 1. Entrou com valor muito baixo.
#se for maior que 2. Entrou com valor muito alto.

dipse= int(input("Digite qualquer número, abestado: "))

if (dipse == 1):
    resultado = "Entrou com valor 1, melhore"
if (dipse == 2):
    resultado = "Entrou com valor de 2, aff"
if (dipse < 1):
    resultado = "Entrou com valor muito baixo, desiste menó"
if (dipse > 2):
    resultado = "Entrou com valor muito alto, parabéns está uma bosta"
print(resultado)