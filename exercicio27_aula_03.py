#27. Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar
# imprimir o resultado desta operação.

a = int(input("Insira um numero:  "))
b = a%2
c = a + 5
d = a +8
if (b==0):
    print("Valor", c)
else:   print("Valor", d)