#25.Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar. Utilize o operador %
a = int(input("Insira um numero e descubra se e par ou impar:  "))

b = a%2

if (b==0):
    print("o numero e par:  ")
else: print("O numero e impar:  ")