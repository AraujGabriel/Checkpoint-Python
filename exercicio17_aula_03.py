#Entrar com o peso, o sexo e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa
#está ou não com seu peso ideal. Fórmula: peso/altura².

p = float(input("Insira o peso: "))
a = float(input("Insira a altura: "))
s = str(input("Insira m para Masculino e f para feminino:"))
#"f" para feminino.
f = 'f' 


imc = (p/(a*a))

if (s==f):
    if imc >= 24:
        print("Acima do peso")
    elif imc < 19:
        print("Abaixo do peso")
    else:
        print("Peso ideal")
else: 
    if imc >=25:
        print("Acima do peso")
    elif imc < 20:
        print("Abaixo do peso")
    else: print("Peso ideal")































































































































































































































































