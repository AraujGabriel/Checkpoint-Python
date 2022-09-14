#Calcular a area de um retangula a partir da altura e da base e caso seja maior que 100 exibir a mensagem "terreno grande"
alt = float(input('Inserir altura do terreno: '))
base = float(input('Inserir base do terreno: '))

a = alt * base
print("area do terreno: ", a)

if a >= 100:
    print("Terreno grande")