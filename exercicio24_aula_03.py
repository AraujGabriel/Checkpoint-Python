#24. Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
# Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

name = str(input("Insira o seu nome: "))
s = str(input("Insira o seu sexo, sendo f para feminino e m para masculino:   "))
ec = str(input("Insira o estado civil\nCasado(a)\nSolteiro(a)\Divorciado(a)\nViuvo"))
f = 'f'
m ='m'
casada='casada'
if ((s==f)and(ec==casada)):
    tc = int(input("Insira o tempo de casada:  "))
    print(f"{name} e casada a {tc} anos")
else: print(f"Obrigado {name}")
    
