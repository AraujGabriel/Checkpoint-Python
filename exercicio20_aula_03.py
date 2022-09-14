# Uma escola com cursos em regime semestral realiza duas avaliações
# durante o semestre e calcula a média do aluno, da seguinte maneira:
# MEDIA = (P1 + 2.P2) / 3
#Fazer um programa para entrar via teclado com o valor da primeira nota (P1)
# e o programa deverá calcular e exibir quanto o aluno precisa tirar na segunda nota
#  minimamente (P2) para ser aprovado, sabendo que a média de aprovação é igual a cinco.

#Sera inserido as notas de p1, unica entrada do programa, tendo em vista que a p2 tem que ser fornecida pelo programa.
p1 = float(input("Insira a nota da P1: "))

#A média é 5, e a P2 tendo peso duplo, sendo assim a nota final é como se fosse 3x a média sendo a nota p2 responsavel por duas dessas partes, de 15 pontos necessários para a média 5
# a p2 é responsavel por 10 deles, sendo assim, basta subtrair a p1 de 15 para termos a soma das duas partes da p2 necessária, dividindo por 2, temos o valor exato.
p2=(15-p1)/2

print("A nota necessária para a p2:  ", p2)