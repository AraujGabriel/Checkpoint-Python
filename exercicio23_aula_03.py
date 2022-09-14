#23. Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

a = float(input("insira o valor de a:  "))
b = float(input("insira o valor de b:  "))
c = float(input("insira o valor de c:  "))

if (a+b>c):
    print("A soma de a+b e maior que c")
else:
    print("A soma de a+b nao e maior que c")