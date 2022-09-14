#Entrar via teclado, com dois valores distintos. Exibir o maior deles.#
v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))

if v1 > v2: 
    print("o menor valor é: ", v1)

elif v1==v2:
    print("Valores iguais")

else:
     print("O menor valor é: ", v2)