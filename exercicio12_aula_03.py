#Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão digitados. 
#Se a área for maior que 100, exibir a mensagem “Terreno grande”, caso contrário, exibir a mensagem “Terreno pequeno”.
alt = float(input('Inserir altura do terreno: '))
base = float(input('Inserir base do terreno: '))

a = alt * base
print("area do terreno: ", a)

if a >= 100:
    print("Terreno grande")
else: print("Terreno pequeno")