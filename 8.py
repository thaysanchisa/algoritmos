#entrada 
#calcule 3 notas e encontre a média, 
#se o resultado for menor que 6 "reprovado", maior que 6 "aprovado"

nota1= (int(input("Nota da AV1: ")))
nota2= (int(input("Nota da AV2: ")))
nota3= (int(input("Nota da AV3: ")))

soma=nota1+nota2+nota3
media = soma / 3
if(media >= 6):
    resultado = "Aprovado! Parabéns! :D"
elif(media < 6):
    resultado = "Reprovado. Estude mais!"
print(resultado)