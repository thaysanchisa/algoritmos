#elaborar um programa de computador que leia três valores numericos
#nome das vartiaveis a,b,x
#se o valor de x não for maior que 5,será realizada a operação C = A+B
#Se não C= A-B
#imprima: C

a= int(input("Digite um valor numérico: "))
b= int(input("Digite um valor numérico: "))
x= int(input("Digite um valor numérico: "))

if not (x >= 5):
    c = a+b
else:
    c = a-b
print("Resultado:", c)