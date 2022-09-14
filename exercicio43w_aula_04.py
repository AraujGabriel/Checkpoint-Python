#43. Calcular e exibir a soma dos “N” primeiros valores da sequência abaixo.
# O valor “N” será digitado, deverá ser positivo, mas menor que cinquenta.
# Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente.
#2, 5/8, 10/27, 17/64

n=int(input("Insira um valor positivo menor que 50:"))
while((n<=0)or-5(n>=50)):
    print("Numero invalido, digite novamente")
    n=int(input("Insira um valor positivo menor que 50:"))

a=1 #para parte de cima da fração
c=1 #para parte de baixo da fração
i=1
j=1 #conta a quantidade de vezes que o programa rodou
m=0 #acumula a soma
while(j<=n):
    #parte de cima da fração
    b=a+i
    a=b
    #parte de baixo da fração 
    d=c*c*c
    #resultado da fração
    e=b/d
    print("{}/{}".format(b,d))
    print("+")
    print('')
    i=i+2
    c=c+1
    m=m+e  
    j=j+1
print("o resultado da soma:{}".format(m))


