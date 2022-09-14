#Entrar via teclado, com dois valores distintos. Exibir o maior deles,  se existir, caso contrário, enviar mensagem avisando que os números são idênticos.
 
v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))

if v1 > v2: 
    print("o maior valor é: ", v2)

elif v1==v2:
    print("Valores iguais")

else:
     print("O maior valor é: ", v1)