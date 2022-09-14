#inserir 3 valores e exibir o maior deles
a = float(input("Insira o primeiro valor: "))
b = float(input("Insira o segundo valor: "))
c = float(input("Insira o terceiro valor: "))

if a > b and c:
    print("o maior valor: ", a)
elif b > a and c:
    print("o maior valor: ", b)
elif c > a and b:
    print("o maior valor é ", c)
elif a==b==c:
    print("Valores iguais")
elif a==b > c:
    print("o maior valor: ", a)
elif b==c > b:
    print("o maior valor: ", c)
else:
    print("o maior valor: ", a)