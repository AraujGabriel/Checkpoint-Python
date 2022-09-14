#42. Calcular e exibir a soma dos “N” primeiros valores da sequência abaixo.
#O valor “N” será digitado, deverá ser positivo, mas menor que cinquenta.
# Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente.
#1/2  2/3  3/4  4/5

n=int(input("Insira um valor positivo:"))
while(n<=0):
    print("Numero invalido, digite novamente")
    n=int(input("Insira um valor positivo:"))
i=1
a=1
b=2
j=0
while(i<=n):
    c=a/b
    j=j+c
    
    print("{}/{}".format(a,b))
    print("+")
    print('')
    a=a+1
    b=b+1
    i=i+1
print("o resultado e:",j)


    