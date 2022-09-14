#26. Encontrar o dobro de um número caso ele seja positivo
#e o seu triplo caso seja negativo, imprimindo o resultado.
a = float(input("Insira um numero>  "))

if (a>=0):
    t = a*2
    print(t)
else:
    t = a*3
    print(t)