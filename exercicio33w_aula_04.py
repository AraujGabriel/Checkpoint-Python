 #Entrar via teclado com o sexo de determinado usuário, aceitar somente “F” ou “M” como respostas válidas.
s = (input("Insira f para sexo femino e m para masculino:  "))

while (s != 'f')and (s != 'm'):
    print("Sexo invalido")
    s = (input("Insira f para sexo femino e m para masculino"))

print("Sexo Valido")