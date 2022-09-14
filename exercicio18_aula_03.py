#18. A partir dos valores da aceleração (a em m/s2), da velocidade inicial (v0 em m/s) e do tempo de percurso
#(t em s). Calcular e exibir a velocidade final de automóvel em km/h. Exibir mensagem de acordo com a
#tabela:
#Fórmula para o cálculo da velocidade em m/s: V = v0 + a. t

a = float(input("Insira a aceleração m/s2: "))
vi = float(input("insira a velocidade inicial em m/s: "))
t = float(input("insira o tempo em s: "))

vm = vi + a*t
print("a velocidade em m/s é:  ",vm)
vk = vm * 3.6
print("A velocidade em k/h é:", vk)

if vk <= 40:
    print("Veiculo muito lento")
elif vk <= 60:
    print("Velocidade permitida")
elif vk <=80:
    print("Velocidade de cruzeiro")
    print("Veiculo rapido")
else: print("Veiculo muito rapido")