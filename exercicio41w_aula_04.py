#41. Calcular e exibir a soma dos “N” primeiros valores da sequência abaixo. O valor “N” será digitado, deverá ser positivo, mas menor que cem.
# #Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente.
#A sequência: 2, 5, 10, 17, 26, ....




n = int(input("Digite um numero positivo menor que 100"))
while ((n>100)or(n<=0)):
    print("Numero invalido")
    n = int(input("Digite um numero positivo menor que 100"))
a=1
i=1
j=1
while(j<n):
    b=a+i
    print(b)
    a=b
    i=i+2
    j=j+1




