#Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo.
#Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

v1 = float(input("Insira o valor 1: "))
v2 = float(input("Insira o valor 2: "))
v3 = float(input("Insira o valor 3: "))

v12 = v1 * v1
v22 = v2 * v2
v32 = v3 * v3

if (v22+v32==v12) or (v12+v32==v22) or (v12+v22==v32):
    print("Formam um triangulo retangulo")
else: print("Negativo para traingulo reatangulo")