#solicite o genero de uma pessoa
#identifique se o genero é valido ou não?-? se for M ou F a entrada é válida, se não inválido
genero = input("Digite o gênero: ")

if (genero == "F") or (genero == "M"):
    resultado = "Válido"
else:
    resultado = "Inválido"
print(resultado)