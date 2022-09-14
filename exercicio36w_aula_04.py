#Entrar via teclado com um valor (X) qualquer. Travar a digitação, no sentido de aceitar somente valores positivos. 
# Solicitar o intervalo que o programa que deverá calcular a tabuada do valor digitado, sendo que o segundo valor (B)
# deverá ser maior que o primeiro (A), caso contrário, digitar novamente somente o segundo. Após a validação dos dados
# exibir a tabuada do valor digitado, no intervalo decrescente, ou seja, a tabuada de X no intervalo de B para A.

a=int(input("Insira o numero a ser feito a tabuada:  "))

while a <=0:
    print("Insira um valor positivo")
    a=int(input("Insira o numero a ser feito a tabuada:  "))

b=int(input("Insira o primeiro valor do intervalo da tabuada:  "))
c=int(input("Insira o segundo valor do intervalo:   "))
i = b
while (c<b):
    print("Insira o segundo valor de intervalo maior que o primeiro")
    c=int(input("Insira o segundo valor do intervalo:   "))


while (i<=c):
    t = a * i
    print(t)
    i = i+1


