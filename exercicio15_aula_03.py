# 15. A partir de três valores que serão digitados, verificar se formam ou não um triângulo.
# Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou eqüilátero”.
# Um triângulo escaleno possui todos os lados diferentes, o isósceles, dois lados iguais e o eqüilátero, todos os lados iguais.
# Para existir triângulo é necessário que a soma de dois lados quaisquer seja maior que o outro, isto, para os três lados.

v1 = float(input("Insira o valor 1: "))
v2 = float(input("Insira o valor 2: "))
v3 = float(input("Insira o valor 3: "))

if (v1+v2>v3) and (v1+v3>v2) and (v2+v3>v1):
    print("Os lados formam um triangulo")
    if v1 == v2 == v3:
        print("Triangulo equilatero")
    elif (v1 == v2 != v3) or (v1 == v3 != v2) or (v2==v3!=v1):
        print ("Triangulo isosceles")
    else: print("Triangulo escaleno")
else: print("Os valores não formam um triangulo")