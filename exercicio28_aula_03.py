#28. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem crescente.
a = int(input("Insira o valor a:  "))
b = int(input("Insira o valor b:  "))
c = int(input("Insira o valor c:  "))

if ((a>b) and (a>c)):
    if( b>c):
        print(f"{a}\n{b}\n{c}")
    else: print(f"{a}\n{b}\n{c}")
elif ((b>a) and (b>c)):
    if(a>c):
        print(f"{b}\n{a}\n{c}")
    else: print(f"{b}\n{c}\n{a}")
else: 
    if a>c:
        print(f"{c}\n{a}\n{b}")
    else: print(f"{c}\n{b}\n{a}")