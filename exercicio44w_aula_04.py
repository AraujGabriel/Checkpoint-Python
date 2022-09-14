#44. Entrar via teclado com dez valores positivos. Consistir na digitação e enviar mensagem de erro, se necessário. Após a digitação, exibir:
#a) O maior valor;
#b) A soma dos valores;
#c) A média aritmética dos valores;

i=1

j=0 #para adicionar o valor das entradas
k=0 #para guardar o maior valor
while (i<=10):
    n=float(input("Digite um valor positivo:"))
    while(n<=0):
        print("Valor invalido:")
        n=float(input("Digite um valor positivo:"))
    if(k<n):
        k=n
    j=j+n
    i=i+1
m=j/10
print("O maior valor{}".format(k))
print("A soma dos valores{}".format(j))
print("A media{}".format(m))


        
