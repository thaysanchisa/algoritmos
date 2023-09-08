# um valor numerico inteiro
#Se o valor estiver na faixa 20-90, apresentar uma msg "o valor está dentro da faixa de corte"
#Se o valor estiver fora dessa faixa, apresentar uma msg "está fora da faixa de corte"

nota=(int(input("Digite a nota da prova: ")))

if (nota >= 20) and (nota <= 90):
    resultado= "Está dentro da faixa de corte!"
else:
    resultado = "Está fora da faixa de corte"
print(resultado)