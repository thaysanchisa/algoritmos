#DUAS VARIÁVEIS QUEREM REALIZAR UM PAR PARA FESTA JUNINA
#PARES COM SEXO DIFERENTES
#O SISTEMA PRECISA VERIFICAR SE AS PESSOAS FORMAM O PAR NA ENTRADA E CASO FORMEM, APRESENTAR MENSAGEM INFORMANDO ESTA POSSIBILIDADE.
#Caso contrário o programa deve indicar a imposibildade de formação de par

genero1 = input("Digite o seu sexo: ")
genero2 = input("Digite o seu sexo: ")

#if ((genero1 == "F") and (genero2 == "M")) or ((genero1 == "M") and (genero2 == "F")):
if (genero1 == "F") ^ (genero2 == "F"):  
    resultado1 = "FORMAM PAR"
    print("Hetero top", resultado1)

else: 
    resultado2 = "PAR INVÁLIDO"
    print("gaydara apitou", resultado2)