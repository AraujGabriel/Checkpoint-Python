#37. Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. Entre as tabuadas, solicitar que o usuário pressione uma tecla.
i = 1
j = 1

while (j<=20):
    while (i<=10):
        t = i*j
        print(j,'*',i,'=',t)
        i = i+1
    print('')
    print("FIm da tabuada") 
    print('')
    j=j+1
    i=0  
    a=input("Pressione qualquer tecla:")
print("Fim do programa")


        
