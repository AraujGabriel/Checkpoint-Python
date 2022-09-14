#Entrar via teclado com um valor qualquer.
# Travar a digitação, no sentido de aceitar somente valores positivos.
# Após a digitação, exibir a tabuada do valor solicitado, no intervalo de um a dez.


#n para numero de entrada, e i vai ser o valor incrementador
n = int(input("Insira um valor positivo para ver a tabuada desse numero até o 10:  "))
i = 1


while(n<=0):
    print("Valor invalido")
    n = int(input("Insira um valor positivo para ver a tabuada desse numero até o 10:  "))

while(i<=10):
    t=n*i
    print(t)
    i=i+1
print("fim da tabuada")

