#21. Entrar via teclado com dois valores quaisquer. Após a digitação, exibir um seletor de opções (“menu”) com as seguintes opções:
# (Fazer esse exercício utilizando If..Else e/ou Case)
#1 – Multiplicação
#2 – Adição
#3 – Divisão
#4 – Subtração
#5 – Fim de processo (sair do programa)
#Solicitar uma opção por parte do usuário, verificar se é ou não uma opção válida (letras ou números) e processar a respectiva operação.
# Enviar mensagem de erro se a opção escolhida não existir no seletor.
#Encerrar o programa somente quando o usuário escolher a opção de finalização.
# Repare que a opção de número três é de divisão e o programa deverá enviar mensagem de erro, (somente nesta opção) se o denominador for zero.




a = float(input("Insira o primeiro valor: "))
b = float(input("insira o segundo valor: "))
c = int(input("Escolha uma operacao\n1 – Multiplicação \n2 – Adição \n3 – Divisão \n4 – Subtração \n5 - Fim do programa\n  "))

if c == 1:
   m = b*a 
   print("Resultado: ",m) 
elif c == 2:
    ad = b+a
    print("Resultado: ",ad)
elif c == 3:
    if b == 0:
        print("Valor invalido para divisao")
    else: 
        d = b*a
        print("Resultado: ",d)
elif c == 4:
    s = a-b
    print("Resultado: ",s)
elif c ==5:
    print("Fim do programa, obrigado por utilizar")
else: 
    print("Escolha invalida")
