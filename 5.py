#entrada ler dois numeros
#processamento somar os dois e atribuir o resultado a variavel
#processamento se o resultado for maior ou igual 10 adicionar 5 ao resultado se não, diminuir 7 do resultado
#exibir o resultado

nota_prova1 = int(input("Digite um numero: "))
nota_prova2 = int(input("Digite um numero: "))

resultado = nota_prova1+nota_prova2

if (resultado >= 10):
    resultado = resultado + 5
else:
    resultado = resultado - 7
print("resultado da adição = ",resultado)