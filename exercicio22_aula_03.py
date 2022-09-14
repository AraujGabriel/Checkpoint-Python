#22. Exibir o seguinte seletor de opções e em função de uma escolha, solicitar os dados necessários para o cálculo da respectiva área.
# Enviar mensagem de erro se o usuário escolher uma opção inexistente.
#Encerrar o programa somente quando selecionada a opção de finalização.
# (Fazer esse exercício utilizando If..Else e/ou Case)
#1 – Triângulo
#2 – Quadrado
#3 – Retângulo
#4 – Círculo
#5 – Fim de processo

from cmath import pi


o = int(input("Escolha uma das opcoes: \n1 – Triângulo\n2 – Quadrado\n3 – Retângulo\n4 – Círculo\n5 – Fim de processo\n "))

if o ==1:
    b = float(input("Insira a base do triangulo: "))
    h = float(input("Insira a altura do triangulo: "))
    r = (b*h)/2
    print("Area desse triangulo: ", r)
elif o ==2:
    l = float(input("Insira o lado do quadrado: "))
    t = l*l
    print("Area do quadrado: ", t)
elif o ==3:
    l1 = float(input("Insira o lado: "))
    l2 = float(input("Insira o outro lado: "))
elif o ==4:
    ra = float(input("Insira o raio:  "))
    ac = pi*(ra*ra)
    print("A area do circulo: ",ac)
elif o ==5:
    print("Fim do programa")
else: print("opcao invalida")
