#Entrar com o peso e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa está ou não com seu peso ideal.
#Fórmula: peso/altura².

peso = float(input('Insira o peso: '))
alt = float(input('Insira a altura: '))

ideal = peso/(alt*alt)

if ideal >= 25:
    print("acima do peso")
elif ideal < 25 and ideal >= 20:
    print("peso ideal")
else: print("Abaixo do peso")