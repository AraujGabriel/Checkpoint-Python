# Uma escola com cursos em regime semestral, realiza duas avaliações durante o semestre e calcula a média do aluno
# da seguinte maneira: MEDIA = (P1 + 2P2) / 3
# Fazer um programa para entrar via teclado com os valores das notas (P1 e P2) e calcular a média.
# Exibir a situação final do aluno (“Aprovado ou Reprovado”), sabendo que a média de aprovação é igual a cinco.

p1=float(input("Insira a nota da p1:  "))
p2=float(input("Insira a nota da p2:  "))

m=(p1+(2*p2))/3
#verifica se a media é maior que 5 para aprovar o aluno
if m >= 5:
    print("Aluno aprovado")
else: print("Aluno reprovado")